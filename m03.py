def credit(score):
    each_credits = [2, 2, 3, 3, 2, 2.5, 3, 2, 2, 3, 1.5]
    total_credit = 0
    total_got = 0
    failed = 0
    
    if score[-1] == -1:
        total_credit = sum(each_credits) - 1.5
    else:
        total_credit = sum(each_credits)

    for i in range(len(score)):
        if score[i]>= 60:
            total_got += each_credits[i]
        elif score[i] < 60:
            failed += 1
        else:
            return total_credit, total_got, failed
    return total_credit, total_got, failed
