import xlwt
import xlrd

workbook = xlrd.open_workbook('input.xls')
sheet = workbook.sheet_by_index(0)

data = [sheet.cell_value(0, col) for col in range(sheet.ncols)]

workbook = xlwt.Workbook()
sheet = workbook.add_sheet('test')

for index, value in enumerate(data):
    sheet.write(0, index, value)

workbook.save('output.xls')
