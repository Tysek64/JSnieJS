import z1
import re
import datetime

def getDates (data):
    def getYear (date):
        return re.search(r'^\d{4}(?=\-\d{2}\-\d{2})', date).group(0)
    def getMonth (date):
        return re.search(r'(?<=\d{4}\-)\d{2}(?=\-\d{2})', date).group(0)
    def getDay (date):
        return re.search(r'(?<=\d{4}\-\d{2}\-)\d{2}', date).group(0)

    result = list()
    for elem in data:
        try:
            year = int(getYear(elem['Data uruchomienia']))
            month = int(getMonth(elem['Data uruchomienia']))
            day = int(getDay(elem['Data uruchomienia']))

            result.append(datetime.date(year, month, day))
        except AttributeError:
            print('Invalid date: \'', elem['Data uruchomienia'], '\'', sep='')

        try:
            year = int(getYear(elem['Data zamknięcia']))
            month = int(getMonth(elem['Data zamknięcia']))
            day = int(getDay(elem['Data zamknięcia']))

            result.append(datetime.date(year, month, day))
        except AttributeError:
            print('Invalid date: \'', elem['Data zamknięcia'], '\'', sep='')

    return result

def getCoords (data):
    result = list()
    for elem in data:
        try:
            result.append((float(re.search(r'\d{2}\.\d{6}', elem['WGS84 φ N']).group(0)), float(re.search(r'\d{2}\.\d{6}', elem['WGS84 λ E']).group(0))))
        except AttributeError:
            print('Invalid coordinates: \'', elem['WGS84 φ N'], '\' N, ', elem['WGS84 λ E'], '\' W, ', sep='')
    return result

def getTwoPartNames (data):
    return [elem for elem in data if (re.match(r'^[^-]+\-[^-]+$', elem['Nazwa stacji']) != None)]

def replaceWeirgNames (data):
    def replaceChar (toReplace):
        replacements = {
            ' ': '_',
            'ę': 'e',
            'ó': 'o',
            'ą': 'a',
            'ś': 's',
            'ł': 'l',
            'ż': 'z',
            'ź': 'z',
            'ć': 'c',
            'ń': 'n',
        }
        newChar = replacements[toReplace.group(0).lower()]
        return newChar if toReplace.group(0).islower() else newChar.upper()
    result = list()
    for elem in data:
        elem['Nazwa stacji'] = re.sub(r'[ ęóąśłżźćń]', replaceChar, elem['Nazwa stacji'], flags = re.IGNORECASE)
        result.append(elem)
    return result

def verifyMobile (data):
    for elem in data:
        if (re.search(r'MOB$', elem['Kod stacji']) != None) and (re.search(r'mobilna', elem['Rodzaj stacji']) == None):
            return False
    return True

def getThreePartLocations (data):
    return [elem for elem in data if (re.match(r'^[^-]+\-[^-]+\-[^-]+$', elem['Adres']) != None)]

def getCommaStreets (data):
    return [elem for elem in data if (re.search(r',', elem['Adres']) != None) and (re.search(r'[ua]l\.', elem['Adres']) != None)]

if __name__ == '__main__':
    #print(verifyMobile(z1.readStationsAsDict()))
    import pathlib
    for elem in getTwoPartNames(z1.read_metadata(pathlib.Path('stacje.csv'))):
        print(elem['Nazwa stacji'])
