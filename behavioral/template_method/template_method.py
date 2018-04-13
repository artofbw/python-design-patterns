from abc import ABCMeta, abstractmethod


class AbstractClass(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def operation1(self):
        pass

    @abstractmethod
    def operation2(self):
        pass

    def template_method(self):
        print('Defining algorithm. Operation1 follows Operation2')
        self.operation2()
        self.operation1()


class ConcreteClass(AbstractClass):
    def operation1(self):
        print('My concrete operation1')

    def operation2(self):
        print('Operation2 remains same')


class Client:
    def main(self):
        self.concreate = ConcreteClass()
        self.concreate.template_method()


client = Client()
client.main()