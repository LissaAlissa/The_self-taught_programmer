class Horse():
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner

class Rider():
    def __init__(self, name):
        self.name = name

jakki = Rider('Jakki Chan')

grom = Horse('Grom', jakki)

print(grom.owner.name)