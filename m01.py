# [分數]由以下轉成[等第分數]
#     分數      等第分數
#    90-100       4.3
#    85-89        4.0
#    80-84        3.7
#    77-79        3.3
#    73-76        3.0
#    70-72        2.7
#    67-69        2.3
#    63-66        2.0
#    60-62        1.7
#    0-59         0


def score(exam1, exam2, exam3, exam4, exam5):
    score = [exam1, exam2, exam3, exam4, exam5]
    print('五次分數{score}'.format(score=score))

    total = 0
    for i in score:
        if i >= 90 and i <= 100:
            total += 4.3
        elif i >= 85 and i <= 89:
            total += 4.0
        elif i >= 80 and i <= 84:
            total += 3.7
        elif i >= 77 and i <= 79:
            total += 3.3
        elif i >= 73 and i <= 76:
            total += 3.0
        elif i >= 70 and i <= 72:
            total += 2.7
        elif i >= 67 and i <= 69:
            total += 2.3
        elif i >= 63 and i <= 66:
            total += 2.0
        elif i >= 60 and i <= 62:
            total += 1.7
        elif i >= 0 and i <= 59:
            total += 0
    return total
