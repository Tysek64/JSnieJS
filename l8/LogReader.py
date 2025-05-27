import datetime
import ipaddress

class LogReader:
    parseInfo = [
        (0, lambda x: datetime.datetime.fromtimestamp(float(x)), 'timestamp'), 
        (2, ipaddress.ip_address, 'remote IP'), 
        (4, ipaddress.ip_address, 'local IP'), 
        (7, str, 'method'), 
        (8, str, 'hostname'), 
        (9, str, 'URI'), 
        (13, lambda x: 0 if x == '-' else int(x), 'size'), 
        (14, lambda x: 0 if x == '-' else int(x), 'code')
    ]

    def __init__(self, path, filters = None):
        self.path = path
        self.fullLogs = []
        self.filters = [] if filters is None else filters

    def readMasterList(self):
        result = []
        self.fullLogs = []
        with open(self.path, mode='r') as file:
            for i, line in enumerate(file, start=1):
                success = True
                parsedLine = self.parseRecord(line)
                for f in self.filters:
                    if not f(parsedLine):
                        success = False
                if success:
                    result.append(('; '.join([str(elem) for elem in parsedLine]))[:100] + '...')
                    self.fullLogs.append(parsedLine)
        return result

    def readMasterRecord(self):
        self.fullLogs = []
        with open(self.path, mode='r') as file:
            for i, line in enumerate(file, start=1):
                success = True
                parsedLine = self.parseRecord(line)
                for f in self.filters:
                    if not f(parsedLine):
                        success = False

                if success:
                    self.fullLogs.append(parsedLine)
                    yield ('; '.join([str(elem) for elem in parsedLine]))[:100] + '...'
        return

    def getTotalRecords(self):
        with open(self.path, mode='r') as file:
            return sum(1 for _ in file)

    def getDetails(self, logIndex):
        return {k: v for (_, _, k), v in zip(self.parseInfo, self.fullLogs[logIndex])}

    def parseRecord(self, record):
        return tuple([fun(record.strip().split('\t')[index]) for index, fun, _ in self.parseInfo])

    @staticmethod
    def getDetail(record):
        return {k: v for (_, _, k), v in zip(LogReader.parseInfo, record)}

if __name__ == '__main__':
    import sys
    for elem in LogReader(sys.argv[1]).readMasterList():
        print(elem)
