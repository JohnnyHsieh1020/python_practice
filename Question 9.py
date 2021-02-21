# # Question 9
#      在m06.py中, 建立一個[象棋]類別
#     一副完整象棋的黑子, 有「將士士象象車車馬馬包包卒卒卒卒卒」.
#     現在它們掉到地上, 也找回來了一些, 到底還有哪些黑子沒找到?

#     例如, 找到「象包卒馬馬將卒卒象車車包卒」,
#           遺失的黑子為['士', '士', '卒']
# -------------------------------------------------------------------------------------
from m06 import ChineseChess

cc = []

# 編號, 找回的黑子
cc.append(ChineseChess(1, '將士士象象車車馬馬包包卒卒卒卒卒'))
cc.append(ChineseChess(2, '象包卒馬馬將卒卒象車車包卒'))
cc.append(ChineseChess(3, '車車馬包士象象將士卒卒包卒卒'))
cc.append(ChineseChess(4, '將包包卒馬馬卒卒卒士士象象車'))
cc.append(ChineseChess(5, '馬象車卒將士士卒包包卒象'))
cc.append(ChineseChess(6, '車卒卒象將象車包卒士'))
cc.append(ChineseChess(7, '車馬包士士象將象車卒卒馬包'))
cc.append(ChineseChess(8, '象馬卒卒卒車包包馬士卒車'))

for c in cc:
    print('編號:{}, 遺失的棋子:{}'.format(c.no, c.lost()))
# -------------------------------------------------------------------------------------
