class Station:
    def __init__ (self, dictRepr):
        self.number = dictRepr.get('Nr', '0')
        self.code = dictRepr.get('Kod stacji', '')
        self.intCode = dictRepr.get('Kod międzynarodowy', '')
        self.name = dictRepr.get('Nazwa stacji', '')
        self.oldCode = dictRepr.get('Stary Kod stacji \r\n(o ile inny od aktualnego)', '')
        self.startDate = dictRepr.get('Data uruchomienia', '')
        self.closeDate = dictRepr.get('Data zamknięcia', '')
        self.stationType = dictRepr.get('Typ stacji', '')
        self.areaType = dictRepr.get('Typ obszaru', '')
        self.stationKind = dictRepr.get('Rodzaj stacji', '')
        self.voivodeship = dictRepr.get('Województwo', '')
        self.city = dictRepr.get('Miejscowość', '')
        self.address = dictRepr.get('Adres', '')
        self.latitude = dictRepr.get('WGS84 φ N', '0')
        self.longitude = dictRepr.get('WGS84 λ E', '0')

    def __str__ (self):
        return f'''=== STACJA {self.code} ''' + ('' if self.oldCode == '' else f' (ex {self.oldCode})') + f''' RODZAJU {self.stationKind} ===
Nazwa:\t\t\t{self.name}
Okres dzialania:\t{self.startDate} ~ {self.closeDate}
Adres:\t\t\t{self.address}, {self.city}, wojewodztwo {self.voivodeship}
Lokalizacja:\t\t{self.latitude}°N {self.longitude}°E'''

    def __repr__ (self):
        return f'''Station {{
    number = {self.number}
    code = {self.code}
    intCode = {self.intCode}
    name = {self.name}
    oldCode = {self.oldCode}
    startDate = {self.startDate}
    closeDate = {self.closeDate}
    stationType = {self.stationType}
    areaType = {self.areaType}
    stationKind = {self.stationKind}
    voivodeship = {self.voivodeship}
    city = {self.city}
    address = {self.address}
    latitude = {self.latitude}
    longitude = {self.longitude}
}}'''

    def __eq__ (self, o):
        return self.code == o.code

import l5.z1
if __name__ == '__main__':
    for stat in l5.z1.read_metadata('stacje.csv'):
        print(Station(stat))
    test1 = Station({'Kod stacji': 'stacja', 'Nazwa stacji': 'Stacja testowa 1'})
    test2 = Station({'Kod stacji': 'stacja', 'Nazwa stacji': 'Stacja testowa 2'})
    print('', test1, test2, test1 == test2, sep='\n\n')

test = Station(l5.z1.read_metadata('stacje.csv')[0])
