# # Question 1
# 有一家電信公司提供3種資費方案:
# 方案A, 月繳基本費699元吃到飽, 不管通話多久都收基本費;
# 方案B, 月繳基本費399元可打120分鐘, 每超過1分鐘收2.4元;
# 方案C, 月繳基本費199元可打70分鐘, 每超過1分鐘收3.8元.

# 輸入:
#     (1) 方案: 字串, 內容為'A', 'B', 或 'C'
#     (2) 本月通話分鐘費: 整數

# 輸出: 本月應繳費用

# 處理:
#     (1) 假設方案的輸入值一定是'A', 'B', 'C'其中之一, 同學不必檢查是否輸入了其他值.
#     (2) 假設通話分鐘的輸入值一定整數, 同學不必檢查是否輸入了錯誤值.
#     (3) 本月應繳費用 = 基本費 + 超時通話費, 四捨五入至整數.
#     (4) 輸出金額以千分位逗號(3位一個逗號)修飾.
# -------------------------------------------------------------------------------------
project = input('方案： ')
minutes = int(input('通話分鐘數： '))

if project == 'A':
    print('本月應繳費用：699')
elif project == 'B':
    if minutes > 120:
        total_project_b = 399 + (minutes - 120) * 2.4
        total_project_b = round(total_project_b)
        total_project_b = format(total_project_b, ',')
        print('本月應繳費用：{total}'.format(total=total_project_b))
    else:
        total_project_b = 399
        print('本月應繳費用：399')
else:
    if minutes > 70:
        total_project_c = 199 + (minutes - 70) * 3.8
        total_project_c = round(total_project_c)
        total_project_c = format(total_project_c, ',')
        print('本月應繳費用：{total}'.format(total=total_project_c))
    else:
        total_project_c = 199
        print('本月應繳費用：199')
# -------------------------------------------------------------------------------------
