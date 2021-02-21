class ChineseChess():
    def __init__(self, no, piece):
        self.no = no
        self.piece = piece

    def lost(self):
        correct = {'將': 1, '士': 2, '象': 2, '車': 2,
                   '馬': 2, '包': 2, '卒': 5}

        found = {'將': 0, '士': 0, '象': 0, '車': 0,
                 '馬': 0, '包': 0, '卒': 0}

        result = []
        for i in self.piece:
            if i in found:
                found[i] += 1
            else:
                found[i] = 1

        for j in correct:
            if found[j] == correct[j]:
                continue
            else:
                for k in range(correct[j] - found[j]):
                    result.append(j)
        return result
