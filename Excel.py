import openpyxl as xl

wb = xl.load_workbook("Python Intro Practices\sample2.xlsx")
sheet = wb['Sheet1']
cell = sheet['a1']
print(cell.value)