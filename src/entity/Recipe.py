from unicodedata import name


class Recipe :

    def __init__(self, id, title, instructions) -> None:
        self.__id = id
        self.title = title
        self.instructions = instructions


    def getId(self):
        return self.id


    def __str__(self) -> str:
        return f"{self.__id}\n{self.title}\n{self.instructions}"