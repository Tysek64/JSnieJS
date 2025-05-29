class Station:
    def __init__ (self, dictRepr: dict) -> None:
        self.number: int = dictRepr.get('Nr', '0')
        self.code: str = dictRepr.get('Kod stacji', '')
        self.intCode: str = dictRepr.get('Kod międzynarodowy', '')
        self.name: str = dictRepr.get('Nazwa stacji', '')
        self.oldCode: str = dictRepr.get('Stary Kod stacji \r\n(o ile inny od aktualnego)', '')
        self.startDate: str = dictRepr.get('Data uruchomienia', '')
        self.closeDate: str = dictRepr.get('Data zamknięcia', '')
        self.stationType: str = dictRepr.get('Typ stacji', '')
        self.areaType: str = dictRepr.get('Typ obszaru', '')
        self.stationKind: str = dictRepr.get('Rodzaj stacji', '')
        self.voivodeship: str = dictRepr.get('Województwo', '')
        self.city: str = dictRepr.get('Miejscowość', '')
        self.address: str = dictRepr.get('Adres', '')
        self.latitude: float = dictRepr.get('WGS84 φ N', '0')
        self.longitude: float = dictRepr.get('WGS84 λ E', '0')

    def __str__ (self) -> str:
        return f'''=== STACJA {self.code} ''' + ('' if self.oldCode == '' else f' (ex {self.oldCode})') + f''' RODZAJU {self.stationKind} ===
Nazwa:\t\t\t{self.name}
Okres dzialania:\t{self.startDate} ~ {self.closeDate}
Adres:\t\t\t{self.address}, {self.city}, wojewodztwo {self.voivodeship}
Lokalizacja:\t\t{self.latitude}°N {self.longitude}°E'''

    def __repr__ (self) -> str:
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

    def __eq__ (self, o: object) -> bool:
        return isinstance(o, Station) and (self.code == o.code)

import l5.z1
if __name__ == '__main__':
    from pathlib import Path
    for stat in l5.z1.read_metadata(Path('stacje.csv')):
        print(Station(stat))
    test1: Station = Station({'Kod stacji': 'stacja', 'Nazwa stacji': 'Stacja testowa 1'})
    test2: Station = Station({'Kod stacji': 'stacja', 'Nazwa stacji': 'Stacja testowa 2'})
    print('', test1, test2, test1 == test2, sep='\n\n')

    test: Station = Station(l5.z1.read_metadata(Path('stacje.csv'))[0])
