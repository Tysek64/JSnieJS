class PasswordGenerator:
    def __init__(self, length: int, count: int, charset: str | list[str] = "alphanum") -> None:
        self.length = length

        match charset:
            case "alphabet":
                import string
                self.charset = string.ascii_letters
            case "alphanum":
                import string
                self.charset = string.ascii_letters + string.digits
            case "alphanum_special":
                self.charset = \
                    "!@#$%@^&*()abcdefghijklmnopqrstuwvxyzABCDEFGHIJKLMNOPQRSTUWVXYZ"
            case _:
                self.charset = charset # bedzie dzialac tez dla stringow

        self.count = count

    def __iter__(self):
        return self

    def __next__(self):
        if self.count <= 0:
            raise StopIteration

        import random
        pwd = random.choices(self.charset, k=self.length)

        self.count -= 1
        return "".join(pwd)



def main() -> None:
    pg = PasswordGenerator(4, 4)
    for pwd in pg:
        print(pwd)

    pg = PasswordGenerator(10, 4)
    except_thrown = False
    while not except_thrown:
        try:
            pwd = next(pg)
            print(pwd)
        except StopIteration:
            except_thrown = True


if __name__ == '__main__':
    main()

        


