import zope.interface
from IGameItem import IGameItem


@zope.interface.implementer(IGameItem)
class AnyReward:
    def open(self):
        print("Открыли сундук с чем-то ещё")
