from pathlib import Path


# globem duzo szybciej i przyjemniej, ale chce byc zgodny z wymaganiami
def group_measurment_files_by_key(dirpath: Path,
                                  fmt: str = r"(?<=/)[0-9]{4}(_.+){2}\.csv$",
                                  tokenizer: str = "_",
                                  ext: str = ".csv") -> dict[tuple, Path]:
    if not dirpath.exists():
        raise OSError("\033[91mPodany katalog nie istnieje")

    import re
    def search_predicate(fname: Path) -> bool:
        return re.search(fmt, str(fname)) is not None

    # nie wiem czy zadziala jak zmienisz format na "" ale chyba nas to nie obchodzi
    def get_signature(fname: Path) -> tuple:
        nq_name = re.search(fmt, str(fname))
        return tuple(nq_name.group(0).split(ext)[0].split(tokenizer))

    files = [f for f in dirpath.iterdir() if f.is_file() and search_predicate(f)]
    #print(get_signature(files[0]))
    return {get_signature(f): f for f in files}

if __name__ == '__main__':
    try:
        print(group_measurment_files_by_key(Path("./measurements")))
    except OSError as e:
        print(e)
    pass