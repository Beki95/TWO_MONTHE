class Animal:
    def __init__(self, color, size, brain):
        self.color = color
        self.size = size
        self.brain = brain


class Parrot(Animal):
    def __init__(self, color, size, brain, tail, beak, wings):
        super(Parrot, self).__init__(color, size, brain)
        self.tail = tail
        self.wings = wings
        self.beak = beak



