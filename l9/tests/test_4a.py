from Station import Station

class TestClass:
    def test_eq_1(self):
        station1 = Station({'Kod stacji': 'stacja', 'Nazwa stacji': 'Stacja testowa 1'})
        station2 = Station({'Kod stacji': 'stacja', 'Nazwa stacji': 'Stacja testowa 1'})
        assert (station1 == station2) == True
        assert (station2 == station1) == True

    def test_eq_2(self):
        station1 = Station({'Kod stacji': '', 'Nazwa stacji': 'Stacja testowa'})
        station2 = Station({'Kod stacji': '', 'Nazwa stacji': 'Stacja'})
        assert (station1 == station2) == True
        assert (station2 == station1) == True

    def test_eq_3(self):
        station1 = Station({'Kod stacji': 'Bing', 'Nazwa stacji': 'Stacja testowa'})
        station2 = Station({'Kod stacji': '', 'Nazwa stacji': 'Stacja testowa'})
        assert (station1 == station2) == False
        assert (station2 == station1) == False

    def test_eq_4(self):
        station1 = Station({'Kod stacji': 'Bing', 'Nazwa stacji': ''})
        station2 = Station({'Kod stacji': '!)($', 'Nazwa stacji': ''})
        assert (station1 == station2) == False
        assert (station2 == station1) == False
