class Item:
    def __init__(self, name) -> None:
        self.name = name


def add_item(name, Class):
    return Class(name)


print(add_item('2 * 3 * 2', Item).name)
