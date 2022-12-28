import json
from abc import ABC, abstractmethod


class Tableware(ABC):
    def __init__(self, brand: str, sharpness: bool, size: str, material: str, isContainer: bool, name: str):
        self.brand = brand
        self.sharpness = sharpness
        self.size = size
        self.material = material
        self.isContainer = isContainer
        self.name = name

    def __repr__(self) -> str:
        if self.isContainer == True:
            return f'<{self.name}: brand: {self.brand}, sharpness: {self.sharpness}, size: {self.size}, material: {self.material} this is the container>'
        else:
            return f'<brand: {self.brand}, sharpness: {self.sharpness}, size: {self.size}, material: {self.material} this is not the container>'

    @abstractmethod
    def Volume(self):
        pass


class Knife(Tableware):
    def __init__(self, brand: str, sharpness: bool, size: str, material: str):
        self.isContainer = False
        self.name = "Knife"
        super().__init__(brand, sharpness, size, material, self.isContainer, self.name)

    def Volume(self):
        return f"{self.name}: Don't have volume"


class Fork(Tableware):
    def __init__(self, brand: str, sharpness: bool, size: str, material: str):
        self.isContainer = False
        self.name = "Fork"
        super().__init__(brand, sharpness, size, material, self.isContainer, self.name)

    def Volume(self):
        return f"{self.name}: Don't have volume"


class Spoon(Tableware):
    def __init__(self, brand: str, sharpness: bool, size: str, material: str):
        self.isContainer = False
        self.name = "Spoon"
        super().__init__(brand, sharpness, size, material, self.isContainer, self.name)

    def Volume(self):
        return f"{self.name}: Don't have volume"


class Plate(Tableware):
    def __init__(self,D: int, H: int, brand: str, sharpness: bool, size: str, material: str):
        self.D = D
        self.H = H
        self.isContainer = True
        self.name = "Plate"
        super().__init__(brand, sharpness, size, material, self.isContainer, self.name)

    def Volume(self):
        return f'{self.name}: Volume: {self.H*3,14*self.D*self.D/4}'


class Pot(Tableware):
    def __init__(self, D: int, H: int, brand: str, sharpness: bool, size: str, material: str):
        self.D = D
        self.H = H
        self.isContainer = True
        self.name = "Pot"
        super().__init__(brand, sharpness, size, material, self.isContainer, self.name)

    def Volume(self):
        return f'{self.name}: Volume: {self.H*3,14*self.D*self.D/4}'


class Pan(Tableware):
    def __init__(self, D: int, H: int, brand: str, sharpness: bool, size: str, material: str):
        self.D = D
        self.H = H
        self.isContainer = True
        self.name = "Pan"
        super().__init__(brand, sharpness, size, material, self.isContainer, self.name)

    def Volume(self):
        return f'{self.name}: Volume: {self.H*3,14*self.D*self.D/4}'


def write(data):
    jsonstr = json.dumps(ensure_ascii=False, obj=data, indent=4)
    open('output.json', 'w').write(jsonstr)


def read_from_json():
    return json.load(open('output.json', 'r'))

if __name__ == '__main__':
    knife = Knife('Samura', True, 'big', 'silver')
    fork = Fork('Potrat', True, 'big', 'silver')
    spoon = Spoon('Lofolop', False, 'small', 'silver')
    plate = Plate(18, 2, 'MyHouse', False, 'big', 'ceramics')
    pot = Pot(25, 20, 'Exted', False, 'big', 'steel')
    pan = Pan(20, 4, 'OverCook', False, 'small', 'steel')
    Tablewares = [knife, fork, spoon, plate, pot, pan]
    data = {
        'amount': len(Tablewares),
        'obj': []
    }
    for elem in Tablewares:
        data['obj'].append(elem.__dict__)

    write(data)
    data.clear()
    Tablewares.clear()
    data = read_from_json()

    for elem in data['obj']:
        if elem['name'] == "Knife":
            obj = Knife(elem['brand'], elem['sharpness'], elem['size'], elem['material'])
        elif elem['name'] == "Fork":
            obj = Fork(elem['brand'], elem['sharpness'], elem['size'], elem['material'])
        elif elem['name'] == "Spoon":
            obj = Spoon(elem['brand'], elem['sharpness'], elem['size'], elem['material'])
        elif elem['name'] == "Plate":
            obj = Plate(elem['D'], elem['H'], elem['brand'], elem['sharpness'], elem['size'], elem['material'])
        elif elem['name'] == "Pot":
            obj = Pot(elem['D'], elem['H'], elem['brand'], elem['sharpness'], elem['size'], elem['material'])
        elif elem['name'] == "Pan":
            obj = Pan(elem['D'], elem['H'], elem['brand'], elem['sharpness'], elem['size'], elem['material'])
        Tablewares.append(obj)

    f = open("output.txt", 'w')
    try:
        for elem in Tablewares:
            f.write(elem.Volume()+'\n')
    finally:
        f.close()
