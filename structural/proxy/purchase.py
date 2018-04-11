from abc import ABCMeta, abstractmethod


class You:
    def __init__(self):
        print('You:: Lets buy the Denim shirt')
        self.debitCard = DebitCard()
        self.isPurchased = None

    def makePayment(self):
        self.isPurchased = self.debitCard.do_pay()

    def __del__(self):
        if self.isPurchased:
            print('You:: Wow! Denim shirt is mine')
        else:
            print('You:: I should earn more')


class Payment(metaclass=ABCMeta):
    @abstractmethod
    def do_pay(self):
        pass


class Bank(Payment):
    def __init__(self):
        self.card = None
        self.account = None

    def _getAccount(self):
        self.account = self.card # Assume card number is account number
        return self.account

    def _hasFunds(self):
        print('Bank:: Checking if account', self._getAccount(), 'has enought funds')
        return True

    def setCard(self, card):
        self.card = card

    def do_pay(self):
        if self._hasFunds():
            print('Bank:: Paying the merchant!')
            return True
        else:
            print('Bank:: Sorry, not enought funds!')
            return False


class DebitCard(Payment):
    def __init__(self):
        self.bank = Bank()

    def do_pay(self):
        card = input('Bank:: Punch in card number: ')
        self.bank.setCard(card)
        return self.bank.do_pay()


if __name__ == '__main__':
    you = You()
    you.makePayment()