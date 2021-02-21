class ChineseChess():
    def __init__(self, no, player1, player2):
        self.no = no
        self.player1 = player1
        self.player2 = player2

    def winner(self):
        black = {'將': 1, '士': 2, '卒': 3}
        red = {'帥': 1, '仕': 2, '兵': 3}
        player1_toNum = []
        player2_toNum = []
        player1_win = 0
        player2_win = 0

        for i, j in zip(self.player1, self.player2):
            player1_toNum.append(black[i])
            player2_toNum.append(red[j])

        for a, b in zip(player1_toNum, player2_toNum):
            if a == b:
                continue
            elif a > b:
                player2_win += 1
            else:
                player1_win += 1
        
        if player1_win > player2_win:
            return 'player1'
        elif player1_win < player2_win:
            return 'player2'
        else:
            return 'draw'
