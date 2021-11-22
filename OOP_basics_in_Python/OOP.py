# Реализуйте классы animal, monkey, cat, dog.
# Пусть классы monkey, cat, dog наследуются от класса animal.
# Реализуйте методы, позволяющие животным назвать (say_name) и подать голос (voice).
# Задайте для классов атрибуты Weight (вес) и Height (рост).


class Animal:
    def say_name(self):
        print(f"{self.name}")

    def voice(self):
        print(f"{self.voice}")


class Monkey(Animal):
    name = "monkey"
    voice = "do not even dream"
    Weight = 50
    Height = 1500


class Cat(Animal):
    name = "cat"
    voice = "miui"
    Weight = 4
    Height = 300


class Dog(Animal):
    name = "dog"
    voice = "gav"
    Weight = 10
    Height = 600


Animal.voice(Monkey)
