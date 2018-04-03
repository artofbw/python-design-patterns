from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    @abstractmethod
    def do_say(self):
        pass

    
class Dog(Animal):
    def do_say(self):
        print('Bhow bhow!!')


class Cat(Animal):
    def do_say(self):
        print('Meow meow!!')


## Forest factory defined
class ForestFactory:
    def make_sound(self, object_type):
        return eval(object_type)().do_say()


## Client code
if __name__ == '__main__':
    ff = ForestFactory()
    animal = input('Which animal should make_sound Dog or Cat?')
    ff.make_sound(animal)