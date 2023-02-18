import openpyxl

name2Age = [
    ['张飞',  38],
    ['赵云',  27],
    ['许褚',  36],
    ['典韦',  38],
    ['关羽',  39],
    ['黄忠',  49],
    ['徐晃',  43],
    ['马超',  23]
]

# 创建一个Excel workbook 对象
book = openpyxl.Workbook()
sh = book.active
sh.title = '年龄表'

# 写标题栏
sh['A1'] = '姓名'
sh['B1'] = '年龄'

for row in name2Age:
    # 添加到下一行的数据
    if '黄' in row[0]:
        break
    sh.append(row)
# 保存文件
book.save('信息.xlsx')
