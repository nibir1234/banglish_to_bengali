# coding=utf-8
from bnbphoneticparser import BengaliToBanglish
from bnbphoneticparser import BanglishToBengali
import pandas as pd

output = []

# bengali2banglish = BengaliToBanglish()
# bengali_text = "আমি বাংলাদেশি"
# a = bengali2banglish.parse(bengali_text.strip())

xls = pd.ExcelFile(r"data2.xlsx")
sheetX = xls.parse(0)
var1 = sheetX['Banglish'].astype('string')


banglish2bengali = BanglishToBengali()
for verse in var1:
    a = banglish2bengali.parse(verse.strip())
    # print(a)
    output.append(a)

for o in output:
    with open("output4.csv", 'ab') as file:
        foo = f"\"{o}\",\n"
        file.write(foo.encode('utf8'))
