from pathlib import Path

def parse_dict(data: dict, datatype: type) -> dict:
    return {k: [datatype(cell) if cell != '' else None for cell in row] for k,row in data.items()}

def read_metadata(path: Path, delimiter=',',
              quotechar: str = '"') -> None | list[dict]:
    import csv

    try:
        with open(path, newline='\n') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=delimiter, quotechar=quotechar)
            return [row for row in reader]
    # rzekomo jest add_note ?
    except OSError as e:
            raise OSError("Wystapil problem - zla nazwa pliku / nie mozna otworzyc pliku\n"
                          "Wyjatek: \033[91m" + e.__str__())

class BadHeaderException(Exception):
    def __init__(self, message):
        super().__init__(message)

class BadDataException(Exception):
    def __init__(self, message):
        super().__init__(message)

# Jezeli ucinasz z headera linie, to musisz to uwzglednic przy splitowaniu na header i data
def read_data(path: Path, header_split=5, delimiter=',',
              quotechar: str = '"', skipped_lines=None) -> None | tuple[dict, dict]:

    import csv

    if header_split <= 0:
        raise BadHeaderException("\033[91mNiepoprawny naglowek - dlugosc naglowka musi byc dodatnia")

    skipped_lines_ = skipped_lines if skipped_lines is not None else []

    try:
        with open(path, newline='\n') as csvfile:
            reader = csv.reader(csvfile, delimiter=delimiter, quotechar=quotechar)
            lines = filter(lambda e:  True if e[0] not in skipped_lines_ else False,
                           enumerate([line for line in reader]))
            lines = list(map(lambda e: e[1], lines))
            header, data = lines[:header_split], lines[header_split:]

            if header == [] or len(header[0]) < 2:
                raise BadHeaderException("\033[91mNiepoprawny naglowek - nie wykryto kolumn")
            if data == [] or len(data[0]) < 2:
                raise BadDataException("\033[91mNiepoprawna zawartosc - nie wykryto kolumn")

            dict_data = parse_dict({row[0]: row[1:] for row in data}, float)
            dict_header = parse_dict(
                {id_: [h_info[int(id_)] for h_info in header[1:]] for id_ in header[0][1:]}, str)
            return dict_header, dict_data
    except OSError as e:
        raise OSError("Wystapil problem - zla nazwa pliku / nie moxna otworzyc pliku"
                      "\nWyjatek: \033[91m" + e.__repr__())



if __name__ == '__main__':
    # nie w kazdym pliku masz te same wskazniki - 2023 PrekursoryZielonka csv
    # czas pomiaru sie zgadza, wiec go usuwam
    path_d = Path('./measurements/1234_1234_1234.csv')
    path_h = Path('./stacje.csv')
    try:
        res_d = read_data(path_d, skipped_lines=[3])
        #res_h = read_metadata(path_h)
        print(res_d[0])
        #print(res_h[0])
    except Exception as e:
        print("\033[91m", e)
