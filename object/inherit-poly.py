# -*- coding: utf-8 -*-
class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eatting meat...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')

    def eat(self):
        print('Eatting fish...')


dog = Dog()
dog.run()

cat = Cat()
cat.run()

b = Animal()
print(isinstance(cat, Animal))
print(isinstance(b, Dog))


class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')


def run_twice(animal):
    animal.run()
    animal.run()


run_twice(Animal())
run_twice(Dog())
run_twice(Cat())
run_twice(Tortoise())
