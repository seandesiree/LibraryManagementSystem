class Author:
    def __init__(self, name, biography):
        self._name = name
        self._biography = biography

    
    def name(self):
        return self._name

  
    def biography(self):
        return self._biography

    def __str__(self):
        return f"Name: {self.name}, Biography: {self.biography}"
