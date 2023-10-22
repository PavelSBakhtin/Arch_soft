import random
from GoldGenerator import GoldGenerator
from GemGenerator import GemGenerator
from AnyGenerator import AnyGenerator


if __name__ == '__main__':
    fabricList = [GoldGenerator(), GemGenerator(), AnyGenerator()]
    for i in range(20):
        rnd = random.choice(fabricList).create_item().open()
