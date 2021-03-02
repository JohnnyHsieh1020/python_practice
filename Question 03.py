# # Question 3
# 輸入: 一個學生的答案字串(20個字)

# 輸出: 與正確答案比對的結果
#       每個字依序表示該順序的問題是否答對, 若是顯示'.' (小數點), 若否顯示'*' (星號)

# 處理: (1) 如果學生的答案與正確答案相同, 該題就是答對;
#       (2) 如果正確答案是E, 學生答A或B也算對.
#       (3) 如果正確答案是F, 學生答C或D也算對.
#       (4) 不是以上情況之一, 該題就是答錯.
#       (5) 假設標準答案為: EBBDCCCDACBCBADAABCF
# -------------------------------------------------------------------------------------
correct_ans = 'EBBDCCCDACBCBADAABCF'
response = input('學生答案： ')
result = ''
count = 0
for i in range(len(correct_ans)):
    
    if response[i] == correct_ans[i]:
        result += '.'
    elif correct_ans[i] == 'E':
        if response[i] == 'A' or response[i] == 'B':
            result += '.'
        else:
            count += 1
            result += '*'
    elif correct_ans[i] == 'F':
        if response[i] == 'C' or response[i] == 'D':
            result += '.'
        else:
            count += 1
            result += '*'
    else:
        count += 1
        result += '*'

rate = (20-count)/20*100
print('正確答案： {correct_ans}'.format(correct_ans=correct_ans))
print('比對結果： {result}'.format(result=result))
print('正確率： {rate}%'.format(rate=rate))
# -------------------------------------------------------------------------------------
