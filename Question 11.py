# # Question 11
# 在m08.py中, 建立一個[珍珠奶茶]類別
# [1] 有個店家賣客製化珍珠奶茶, 客人可以:
# [2] 點一杯紅茶 (25元, 一定要點);
# [3] 只加粉圓 (加15元), 只加仙草 (加10元), 同時加粉圓及仙草 (加20元);
# [4] 加牛奶 (加12元).

# 例如, 有人加點粉圓及牛奶, 飲料價錢 = 25元 + 15元 + 12元 = 52元.
# -------------------------------------------------------------------------------------
from m08 import PearlMilkTea

pmt = []

# 編號, 是否加珍珠, 是否加仙草, 是否加牛奶
pmt.append(PearlMilkTea(1, True, True, True))
pmt.append(PearlMilkTea(2, True, True, False))
pmt.append(PearlMilkTea(3, True, False, True))
pmt.append(PearlMilkTea(4, True, False, False))
pmt.append(PearlMilkTea(5, False, True, True))
pmt.append(PearlMilkTea(6, False, True, False))
pmt.append(PearlMilkTea(7, False, False, True))
pmt.append(PearlMilkTea(8, False, False, False))

for p in pmt:
    print('編號:{}, 價格:{}元'.format(p.no, p.price()))
# -------------------------------------------------------------------------------------
