from pathlib import Path
from l5.z1 import BadDataException, BadHeaderException, parse_dict
from TimeSeries import TimeSeries

class LazyReader:
    def __init__(self, path: Path, header_split=5, delimiter=',',
              quotechar: str = '"', skipped_lines=None) -> None:

        if header_split <= 0:
            raise BadHeaderException("\033[91mNiepoprawny naglowek - dlugosc naglowka musi byc dodatnia")

        self.path = path
        self.header_split = header_split
        self.delimiter = delimiter
        self.quotechar = quotechar
        self.skipped_lines = skipped_lines if skipped_lines is not None else []
        self.metadata_read = False
        self.reader = None
        self.position = 0


    def open(self) -> None:
        import csv
        try:
            self.csvfile = open(self.path)
            self.reader = csv.reader(self.csvfile, delimiter=self.delimiter, quotechar=self.quotechar)
        except OSError as e:
            raise OSError("Wystapil problem - zla nazwa pliku / nie mozna otworzyc pliku"
                          "\nWyjatek: \033[91m" + e.__repr__())

    def close(self) -> None:
        self.csvfile.close()
        self.reader = None
        self.position = 0

    def __iter__(self):
        return self.ReaderIterator(self).__iter__()

    class ReaderIterator:
        def __init__(self, ctx):
            self.ctx = ctx

        def __iter__(self):
            if self.ctx.reader is None:
                print('file must be opened first')
                return

            import datetime
            metadata = []
            data = []

            for row in self.ctx.reader:
                if not self.ctx.position in self.ctx.skipped_lines and self.ctx.position >= self.ctx.header_split:
                    try:
                        date = row[0]
                        for index, m in enumerate(row[1:]):
                            data.append((datetime.datetime.strptime(date, '%m/%d/%y %H:%M'),
                                         float(m) if m != '' else None))

                        yield data
                        data = []
                    except ValueError as e:
                        print(date)
                        raise ValueError(e, f"Plik: {self.ctx.path}")

                elif self.ctx.position not in self.ctx.skipped_lines and self.ctx.position < self.ctx.header_split - 1:
                    metadata.append(row)
                else:
                    metadata.append(row)
                    if metadata == [] or len(metadata[0]) < 2:
                        raise BadHeaderException("\033[91mNiepoprawny naglowek - nie wykryto kolumn")

                    metadata = parse_dict(
                        {id_: [h_info[int(id_)] for h_info in metadata[1:]] for id_ in metadata[0][1:]}, str)

                    from TimeSeries import readMetadata
                    series = []
                    readMetadata(series, metadata)
                    yield series

                self.ctx.position += 1

            return




class LazyMerger:
    def __init__(self, readers: list[LazyReader]) -> None:
        self.readers = readers
        self.prefetch_metadata()

    def open(self):
        for r in self.readers:
            r.open()

    def close(self):
        for r in self.readers:
            r.close()

    def prefetch_metadata(self):
        for reader in self.readers:
            reader.open()
        self.data = [next(i.__iter__()) for i in self.readers]
        for reader in self.readers:
            reader.close()

    def __iter__(self):
        return self.MergeIterator(self).__iter__()

    class MergeIterator:
        def __init__(self, ctx):
            self.ctx = ctx

        def __iter__(self):
            for reader in self.ctx.readers:
                reader.close()
                reader.open()

            iters = [i.__iter__() for i in self.ctx.readers]
            for i in iters:
                next(i)
            lengths = [len(i) for i in self.ctx.data]
            buffers = [None] * len(self.ctx.data)

            def calc_id(id):
                ctr = 0
                for l in lengths:
                    if id - l < 0:
                        return ctr, id
                    else:
                        id -= l
                        ctr += 1

            id_to_series = {id_n: calc_id(id_n) for id_n in range(sum(lengths))}

            while True:
                for id, (iter, buffer) in enumerate(zip(iters, buffers)):
                    if buffer is None:
                        try:
                            buffers[id] = next(iter)
                        except StopIteration:
                            buffers[id] = None

                min_ids = []
                min_date = None

                finished = True
                for id, buffer in enumerate(buffers):
                    if buffer is not None:
                        finished = False

                        if min_date is None or buffer[0][0] < min_date:
                            min_date = buffer[0][0]
                            min_ids = [id]
                        elif buffer[0][0] == min_date:
                            min_ids.append(id)

                if finished: return

                result = []
                for id, buffer in enumerate(buffers):
                    if id in min_ids:
                        result.extend(buffer)
                        buffers[id] = None
                    else:
                        result.extend([(min_date, None)] * lengths[id])

                for id, data in enumerate(result):
                    #print(self.ctx.data[id])
                    self.ctx.data[id_to_series[id][0]][id_to_series[id][1]].append(data[0], data[1])
                    #self.ctx.data[id].append(data[0], data[1])

                yield result

    def __len__(self):
        return len(self.get_series())

    def __contains__(self, parameter_name):
        data_flattened = self.get_series()
        for series in data_flattened:
            if series.name == parameter_name:
                return True
        return False

    def __getitem__(self, key) -> TimeSeries:
        if isinstance(key, int) or isinstance(key, slice):
            data_flattened = self.get_series()
            return data_flattened[key]

    def __str__(self) -> str:
        buff = "LazyMerger status:\n"
        for i in self.data:
            for j in i:
                buff += str(j) + "\n"
        return buff

    def get_by_param(self, param_name: str) -> list[TimeSeries]:
        data_flattened = self.get_series()
        return [series for series in data_flattened if series.name == param_name]

    def get_by_code(self, station_name: str) -> list[TimeSeries]:
        data_flattened = self.get_series()
        return [series for series in data_flattened if series.code == station_name]

    def get_series(self) -> list[TimeSeries]:
        return [data for data_list in self.data for data in data_list]

if __name__ == '__main__':
    data_pathl = Path('./measurements/2023_formaldehyd_1g.csv')
    data_pathr = Path('./measurements/2023_SO2_24g.csv')
    data_pathm = Path('./measurements/2023_BaA(PM10)_24g.csv')
    readerl = LazyReader(data_pathl, header_split=6)
    readerr = LazyReader(data_pathr, header_split=6)
    readerm = LazyReader(data_pathm, header_split=6)
    merger = LazyMerger([readerl, readerr, readerm])
    print(merger)
    merger.open()
    try:
        '''
        #print(next(reader.__iter__()))
        for ind, row in zip(range(11), readerr):
            if ind == 10:
                print(row)

        #reader.read_data()
        '''
        for ind, row in zip(range(10000), merger.__iter__()):
            pass
        print(merger)
    except Exception as e:
        raise e
    merger.close()
