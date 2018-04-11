from abc import ABCMeta, abstractmethod

class NewsPublisher:
    def __init__(self):
        self._subscirbers = []
        self._latestNews = None
        
    def attach(self, subscriber):
        self._subscirbers.append(subscriber)

    def detach(self):
        return self._subscirbers.pop()

    def subscribers(self):
        return [type(x).__name__ for x in self._subscirbers]

    def notifySubscribers(self):
        for sub in self._subscirbers:
            sub.update()

    def addNews(self, news):
        self._latestNews = news

    def getNews(self):
        return 'Got news::', self._latestNews


class Subscriber(metaclass=ABCMeta):
    @abstractmethod
    def update(self):
        pass


class SMSSubscriber(Subscriber):
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.getNews())


class EmailSubscriber(Subscriber):
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.getNews())


class AnyOtherSubscriber(Subscriber):
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.getNews())


if __name__ == '__main__':
    news_publisher = NewsPublisher()
    for subscribers in [SMSSubscriber, EmailSubscriber, AnyOtherSubscriber]:
        subscribers(news_publisher)

    print('\nSubscribers:', news_publisher.subscribers())
    
    news_publisher.addNews('Hello world!')
    news_publisher.notifySubscribers()

    print('\nDetached:', type(news_publisher.detach()).__name__)
    print('\nSubscribers:', news_publisher.subscribers())

    news_publisher.addNews('My second news')
    news_publisher.notifySubscribers()
