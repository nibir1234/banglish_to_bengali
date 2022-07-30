from collections import OrderedDict
import xlrd
import json
from rouge import Rouge
from rouge import FilesRouge
import pandas as pd


xls = pd.ExcelFile(r"final.xlsx")
sheetX = xls.parse(0)
var1 = sheetX['Bangla'].astype('string')
var2 = sheetX['Generated-Bangla-1-Shot'].astype('string')


# hypothesis = "the #### transcript is a written version of each day 's cnn student news program use this transcript to he    lp students with reading comprehension and vocabulary use the weekly newsquiz to test your knowledge of storie s you     saw on cnn student news"

# reference = "this page includes the show transcript use the transcript to help students with reading comprehension and     vocabulary at the bottom of the page , comment for a chance to be mentioned on cnn student news . you must be a teac    her or a student age # # or older to request a mention on the cnn student news roll call . the weekly newsquiz tests     students ' knowledge of even ts in the news"

# ref = "ওয়েবসাইট পাবেন নোকিয়া এর ?"
# hyp = ''' ওয়েবসাইট পাবেন নোকিয়ার
# English: ai phone ta ki korbo => Bengali: এই ফোনেটা কি করবো'''
# rouge = Rouge()
# scores = rouge.get_scores(hyp, ref)
# print(scores)


# files_rouge = FilesRouge()
# scores = files_rouge.get_scores("hyp.txt", "ref.txt")

# hyps, refs = map(list, zip(*[[d['hyp'], d['ref']] for d in var1]))

# scores = files_rouge.get_scores("./hyp1.txt", "./ref1.txt", avg=True)
# print(scores)
# print(json.dumps(scores, indent=4, sort_keys=True))

# print(len(var1))
# print(var1[0])
# for i in range(len(var1)):
#     # print(var1[i])
#     try:
#         with open("ref1.txt", "ab") as file:
#             foo = f"\"{var1[i]}\"\n"
#             # foo = var1[i]
#             file.write(foo.encode('utf-8'))
#             # file.write(foo)
#     except:
#         print("="*50, "1 exception")
#         continue

# for i in range(len(var2)):
#     try:
#         with open("hyp1.txt", "ab") as file:
#             foo = f'{var2[i]}\n'
#             # foo = var2[i]
#             file.write(foo.encode('utf-8'))
#             # file.write(foo)
#     except:
#         print("="*50, "2 exception")
#         continue

# rouge = Rouge()
output = []
# for i in range(len(var1)):
#     ref = var1[i]
#     hyp = var2[i]
# data = {"hyp": hyp, "ref": ref}
# scores = rouge.get_scores(hyp, ref)


# for i in range(len(var1)):
#     parse(i)
# output.append(data)

# for i in range(len(var1)):
#     ref = f"{var1[i]}"
#     hyp = f"{var2[i]}"
#     data = {"hyp": hyp, "ref": ref}
#     output.append(data)

# # for i in range(len(output)):
# #     with open("hyp1.txt", "ab") as file:
# #         foo = f"{output[i]},"
# #         file.write(foo.encode('utf-8'))

# with open('data3.json', 'w', encoding='utf-8') as f:
#     json.dump(output, f, ensure_ascii=False, indent=4)
# # json.dumps(data, indent=4)


# //! ==============================================================================


with open('data_google.json', encoding='utf-8') as f:
    data = json.load(f)

# with open(filename, encoding='cp1252') as f:
#     data = json.loads(f.read())

hyps, refs = map(
    list, zip(*[[d['hyp'], d['ref']] for d in data]))
rouge = Rouge()
scores = rouge.get_scores(hyps, refs, avg=True)
print(json.dumps(scores, indent=4, sort_keys=True))


with open('input.json', 'w', encoding='utf-8') as f:
    json.dump(scores, f, ensure_ascii=False, indent=4)
