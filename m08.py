class PearlMilkTea():
    def __init__(self, no, addPearl, addGrass, addMilk):
        self.no = no
        self.addPearl = addPearl
        self.addGrass = addGrass
        self.addMilk = addMilk

    def price(self):
        check = [self.addPearl, self.addGrass, self.addMilk]
        total = 25

        if check[0] and check[1]:
            total += 20
            if check[2]:
                total += 12
        else:
            for i in range(len(check)):
                if i == 0:
                    if check[i]:
                        total += 15
                    else:
                        continue
                elif i == 1:
                    if check[i]:
                        total += 10
                    else:
                        continue
                else:
                    if check[i]:
                        total += 12
                    else:
                        break
        return total
