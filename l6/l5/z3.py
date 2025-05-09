from z1 import read_metadata
from pathlib import Path

def get_addresses(path: Path, city: str, city_col: str = "Miejscowość",
                  wanted_data: list[str] = None) -> list[tuple]:

    def search_predicate(fname: Path) -> bool:
        import re
        return re.search(city, str(fname)) is not None

    if wanted_data is None:
        wanted_data = ["Województwo", "Miejscowość", "Adres"]

    try:
        data = read_metadata(path)
        print(list(map(lambda row: tuple([row[col] for col in wanted_data]),
                       (filter(lambda row: search_predicate(row[city_col]), data)))))
    except OSError as e:
        raise e


if __name__ == '__main__':
    try:
        get_addresses(Path("./stacje.csv"), "Hrubieszów")
    except Exception as e:
        print(e)
    pass