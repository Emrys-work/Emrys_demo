import xlrd

book = xlrd.open_workbook('./income.xlsx')   # 打开工作簿

print(book.nsheets)   # 获取表单数量
print(book.sheet_names())   # 获取表单名字

sheet = book.sheet_by_name('2018')   # 获取表单对象
# sheet = book.sheet_by_index(0)

print(sheet.name)   # 获取表单名
print(sheet.number)   # 获取表单索引
print(sheet.nrows)   # 获取表行数
print(sheet.ncols)   # 获取表列数

print(sheet.cell_value(rowx=0, colx=0))   # 获取指定单元格中的文本内容

print(sheet.row_values(rowx=0))   # 获取第一行的内容放在列表中
print(sheet.col_values(colx=0))   # 获取第一列的内容放在列表中
