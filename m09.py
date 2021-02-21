from collections import Counter


class PearlMilkTea():
    def __init__(self, no, isBig, addPearl, addGrass, addSimilo, addMilk):
        self.no = no
        self.isBig = isBig
        self.addPearl = addPearl
        self.addGrass = addGrass
        self.addSimilo = addSimilo
        self.addMilk = addMilk

    def price(self):
        detail = [self.addPearl, self.addGrass, self.addSimilo, self.addMilk]
        total = 0

        # Big or small
        if self.isBig:
            total += 30
        else:
            total += 25

        # Check ingredients
        if self.addPearl:
            total += 10

        if self.addGrass:
            total += 8

        if self.addSimilo:
            total += 7

        if self.addMilk:
            total += 9

        # Count True
        result = detail.count(True)

        if result == 2:
            total -= 6
        elif result == 3:
            total -= 11
        elif result == 4:
            total -= 17

        return total
