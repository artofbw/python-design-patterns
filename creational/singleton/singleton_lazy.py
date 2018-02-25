class Singleton:
    __instance = None
    
    def __init__(self):
        if not Singleton.__instance:
            print(" __init__ method called.")
        else:
            print("Instance already created:", self.get_instance())
    
    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance
        
        
# s = Singleton()
# __init__ method called.
# s.get_instance()
# __init__ method called.
# <singleton_lazy.Singleton at 0x7f617300c748>
# s1 = Singleton()
# Instance already created: <singleton_lazy.Singleton object at 0x7f617300c748>