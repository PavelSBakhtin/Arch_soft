import zope.interface
from abc import ABCMeta, abstractmethod
from IGameItem import IGameItem


@zope.interface.implementer(IGameItem)
class ItemFabric(metaclass=ABCMeta):

    @abstractmethod
    def create_item(self):
        pass
