class Genre:
    def __init__(self, name, description, category):
        self._name = name
        self._description = description
        self._category = category


    def name(self):
        return self._name


    def description(self):
        return self._description

    def category(self):
        return self._category

    def __str__(self):
        return f"Name: {self.name}, Description: {self.description}, Category: {self.category}"
