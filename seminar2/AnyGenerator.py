from ItemFabric import ItemFabric
from AnyReward import AnyReward


class AnyGenerator(ItemFabric):

    def create_item(self):
        print("Создали сундук (что-то ещё)")
        return AnyReward()
