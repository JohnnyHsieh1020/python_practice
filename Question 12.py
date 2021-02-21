# # Question 12
# 在m09.py中, 建立一個[珍珠奶茶]類別
# [1] 有個店家賣客製化珍珠奶茶, 客人可以:
# [2] 點大杯紅茶 (30元), 點小杯紅茶 (25元);
# [3] 加粉圓 (加10元), 加仙草 (加8元), 加西米露 (加7元) , 加牛奶 (加9元);
# [4] 在項目[3]中, 點2樣可扣6元, 點3樣可扣11元, 點4樣可扣17元..

# 例如, 有人點小杯紅茶加粉圓及牛奶, 飲料價錢 = 25元 + 10元 + 9元 – 6元 = 38元.
# -------------------------------------------------------------------------------------
from m09 import PearlMilkTea

pmt = []
total = 0

# 編號, 是否點大杯, 加珍珠, 是否加仙草, 是否加西米露, 是否加牛奶
pmt.append(PearlMilkTea(1, True, True, True, True, True))
pmt.append(PearlMilkTea(2, True, True, True, True, False))
pmt.append(PearlMilkTea(3, True, True, True, False, False))
pmt.append(PearlMilkTea(4, True, False, True, False, True))
pmt.append(PearlMilkTea(5, False, True, False, False, False))
pmt.append(PearlMilkTea(6, False, True, True, False, True))
pmt.append(PearlMilkTea(7, False, False, True, False, True))
pmt.append(PearlMilkTea(8, False, True, False, False, False))

# 印出資料
for p in pmt:
    print('編號:{}, 價格:{}元'.format(p.no, p.price()))
    total += p.price()
print('今日銷售額：{}元'.format(total))
# -------------------------------------------------------------------------------------
