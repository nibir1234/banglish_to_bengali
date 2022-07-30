
import pandas as pd

output = []
output2 = []

xls = pd.ExcelFile(r"final_1.xlsx")
sheetX = xls.parse(0)
var1 = sheetX['Generated-Bangla-1-Shot'].astype('string')
var2 = sheetX['Generated-Bangla-10-Shot'].astype('string')


for verse in var1:
    a = verse.strip()
    # print(a)
    output.append(a)
for verse in var2:
    a = verse.strip()
    # print(a)
    output2.append(a)

# for o in output:
#     with open("output4.csv", 'ab') as file:
#         foo = f"\"{o}\",\n"
#         file.write(foo.encode('utf8'))

df = pd.DataFrame([output, output2]).T
# print(df)
df.to_excel("stripped.xlsx", index=False)
