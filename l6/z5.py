from pathlib import Path

class Measurements:
    def __init__(self, data_path: Path):
        self.path = data_path



if __name__ == '__main__':
    import l5.z1
    import z2
    data_path = Path('./measurements/2023_C6H6_1g.csv')
    res = l5.z1.read_data(data_path, header_split=6)
    res = z2.readCSVtoTS(res)
    print(res)
