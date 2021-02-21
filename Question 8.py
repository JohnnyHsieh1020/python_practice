# # Question 8
# 在m05.py中, 建立一個[傭金]類別
#     [1] 這家公司有北區與南區兩個銷售點, 傭金計算方式如下:

#     [2] 北區:
#         [2-1] 如果大於(含)500,000元, 有28%傭金率;
#         [2-2] 如果不到500,000元, 但是大於(含)300,000元, , 有23%傭金率;
#         [2-3] 如果不到300,000元, 但是大於(含)100,000元, , 有17%傭金率;
#         [2-4] 如果不到100,000元, 有12%傭金率.

#         例如:北區員工銷售400,000元, 傭金 = 400,000元 * 0.23 = 92,000元

#     [3] 南區:
#         [3-1] 如果大於(含)300,000元, 有22%傭金率;
#         [3-2] 如果不到300,000元, 有17%傭金率.

#         例如: 南區員工銷售300,000元, 傭金 = 300,000元 * 0.22 = 66,000元
# -------------------------------------------------------------------------------------
from m05 import Commission

commissions = []

# 編號, 產品1的銷售金額, 產品2的銷售金額
commissions.append(Commission(1, 500000, '北區'))
commissions.append(Commission(2, 300000, '北區'))
commissions.append(Commission(3, 100000, '北區'))
commissions.append(Commission(4, 80000, '北區'))
commissions.append(Commission(5, 300000, '南區'))
commissions.append(Commission(6, 200000, '南區'))
commissions.append(Commission(7, 100000, '南區'))

# 印出資料
for c in commissions:
    print('編號:{}, 傭金:{:,.0f}元'.format(c.no, c.total()))
# -------------------------------------------------------------------------------------