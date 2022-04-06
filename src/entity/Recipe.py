from unicodedata import name


class Recipe :

    def __init__(self, id, title, instructions) -> None:
        self.id = id
        self.title = title
        self.instructions = instructions


    def __str__(self) -> str:
        return f"{self.id}\n{self.title}\n{self.instructions}"