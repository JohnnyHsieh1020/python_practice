# # Question 10
# 在m07.py中, 建立一個[象棋]類別
# 兩人比棋, 「玩家1」拿「將士卒」3顆棋子, 「玩家2」拿「帥仕兵」.
# 遊戲規則是兩人先排好自己棋子的順序, 再依照順序逐次比大小.

# 在3次比較後, 贏的次數多者是贏家, 相同就是平手. 已知:
# 「將」和「帥」是1, 「士」和「仕」是2, 「卒」和「兵」是3.
# 而且, 「1贏2」,  「2贏3」,  「3贏1」; 如果「數字相同」就沒有輸贏.

# 例如,「玩家1」出「卒士將」,
#      「玩家2」出「兵帥仕」.
#       第1顆棋「卒vs兵」, 第2顆棋「士vs帥」, 第3顆棋「將vs仕」.
#       總計「玩家1」贏1次, 「玩家2」也贏1次, 所以最後是「平手」.
# -------------------------------------------------------------------------------------
from m07 import ChineseChess

cc = []

# 編號, 玩家1的順序, 玩家2的順序
cc.append(ChineseChess(1, '將卒士', '帥仕兵'))
cc.append(ChineseChess(2, '卒士將', '仕帥兵'))
cc.append(ChineseChess(3, '將卒士', '仕帥兵'))
cc.append(ChineseChess(4, '卒士將', '帥兵仕'))
cc.append(ChineseChess(5, '將卒士', '兵帥仕'))
cc.append(ChineseChess(6, '卒士將', '仕帥兵'))
cc.append(ChineseChess(7, '卒將士', '帥兵仕'))
cc.append(ChineseChess(8, '卒將士', '仕兵帥'))

# 印出資料
for c in cc:
    print('編號:{}, 贏家:{}'.format(c.no, c.winner()))
# -------------------------------------------------------------------------------------
