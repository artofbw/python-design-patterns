class EventManager:
    def __init__(self):
        print('Even Manager:: Let me talk to the folks\n')

    def arrange(self):
        self.hotelier = Hotelier()
        self.hotelier.bookHotel()

        self.florist = Florist()
        self.florist.setFlowerRequirements()

        self.caterer = Caterer()
        self.caterer.setCuisine()

        self.musician = Musician()
        self.musician.setMusicType()


class Hotelier:
    def __init__(self):
        print('Arranging the hotel for Marriage? --')

    def _isAvailable(self):
        print('Is hotel free for the event on given day?')
        return True

    def bookHotel(self):
        if self._isAvailable():
            print('Registered the Booking\n\n')


class Florist:
    def __init__(self):
        print('Flower decorations for the event? --')

    def setFlowerRequirements(self):
        print('Carnations, Roses and Lillies would be used for decorations\n\n')


class Caterer:
    def __init__(self):
        print('Food Arrangements for the Event? --')

    def setCuisine(self):
        print('Chinese & Continental Cuisine to be served\n\n')


class Musician:
    def __init__(self):
        print('Musical Arrangements for the event --')

    def setMusicType(self):
        print('Jazz and Classical will be played\n\n')


class You:
    def __init__(self):
        print('You:: Whoa! Marriage Arrangements??!!!')

    def askEventManager(self):
        print('You:: Let\'s contact the Event Manager\n\n')
        em = EventManager()
        em.arrange()

    def __del__(self):
        print('You:: Thanks to Event Manager, all preparations done! Phew!')


you = You()
you.askEventManager()