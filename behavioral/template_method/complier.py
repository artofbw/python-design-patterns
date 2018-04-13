from abc import ABCMeta, abstractmethod


class Complier(metaclass=ABCMeta):
    @abstractmethod
    def collectSource(self):
        pass

    @abstractmethod
    def compileToObject(self):
        pass

    @abstractmethod
    def run(self):
        pass

    def compileAndRun(self):
        self.collectSource()
        self.compileToObject()
        self.run()


class IOSComplier(Complier):
    def collectSource(self):
        print('Collecting Swift source code')

    def compileToObject(self):
        print('Compiling Swift code to LLVM bitcode')

    def run(self):
        print('Program running on runtime enviroment')


ios = IOSComplier()
ios.compileAndRun()