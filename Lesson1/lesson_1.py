class Human:
    age = 17

    def __init__(self, name, gender, race):
        self.name = name
        self.gender = gender
        self.race = race

    def fly(self):
        pass


human = Human(name="Beki", gender="male", race='Mongol')
print(human.name, human.gender, human.race)
