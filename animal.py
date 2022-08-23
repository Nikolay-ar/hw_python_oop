class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f'{self.name} eating')


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)

        self.breed = breed

    def bark(self):
        print(f'Dog named {self.name} is barkinq')


class Cat(Animal):
    def meow(self):
        print(f'{self.name} says Meow')


class Frog(Animal):
    def eat(self):
        print(f'Frog with name {self.name} is eating')


d1 = Dog('Druzhok', 'Bulldog')
c1 = Cat('Barsic')
f1 = Frog('Rwakwa')
a1 = Animal('Vasya')
print(a1.name)
d1.eat()
print(d1.breed)
d1.bark()
f1.eat()
print(c1.name)
print()

animal_arr = [a1, d1, c1, f1]


def introduse(animal):
    print(f'{animal.name}, will say Hello')
    animal.eat()


for animal in animal_arr:
    introduse(animal)

a = 100
b = 0
c = 0
try:
    c = a / b
except:
    print(f'Ошибка деления на 0')
print(c)

d = [1, 2, 3]
print(*d)

print(*animal_arr)
for i in animal_arr:
    print(f'{i.name}')
