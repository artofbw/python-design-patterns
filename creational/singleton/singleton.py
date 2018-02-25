class Singleton:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
            
        return cls.instance


# s = Singleton()
# <singleton.Singleton at 0x7f453f344898>
# s1 = Singleton()
# <singleton.Singleton at 0x7f453f344898>