"""
! pip install datasets transformers[sentencepiece]
! pip install pandas openpyxl
"""


import numpy as np
import pandas as pd
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from google.colab import drive


drive.mount('/content/drive/')


# ===================================English====================================

# model = AutoModelForCausalLM.from_pretrained("gpt2")
# tokenizer = AutoTokenizer.from_pretrained("gpt2")

# ===================================Bengali====================================

model = AutoModelForCausalLM.from_pretrained("flax-community/gpt2-bengali")
tokenizer = AutoTokenizer.from_pretrained("flax-community/gpt2-bengali")

# ==============================================================================


# inputs = tokenizer("Hugging Face is a startup based in New York City and Paris",
#                   return_tensors="pt")

xls = pd.ExcelFile(r"final_revision.xlsx")
sheetX = xls.parse(0)
var1 = sheetX['auvipy/PyAvroPhonetic'].astype('string')

output = []

# for i in range(10):
for i in range(len(var1)):
    inputs = tokenizer(f"{var1[i]}", return_tensors="pt")

    loss = model(input_ids=inputs["input_ids"],
                 labels=inputs["input_ids"]).loss

    ppl = torch.exp(loss)
    val = f"{ppl.item():.2f}"

    output.append(val)
    print(f"{i}: {val}")


out1 = np.array(output).astype('float')
# print(out1)
min = np.min(out1)
max = np.max(out1)


df = pd.DataFrame([output, var1]).T
# output_file = '/content/drive/My Drive/Data712/perplexity.xlsx'
# sheet_name = 'Sheet1'
# df.to_excel('/content/drive/My Drive/Data712/perplexity.xlsx',index=False)

# with pd.ExcelWriter(output_file, mode='a', if_sheet_exists="overlay") as writer:
#             df.to_excel(writer, sheet_name=sheet_name,
#                          startcol=writer.sheets[sheet_name].max_column, header=f"{min} | {max}")


# loss = model(input_ids=inputs["input_ids"],
#             labels=inputs["input_ids"]).loss

# ppl = torch.exp(loss)
# val = f"{ppl.item():.2f}"
# print(f"Perplexity: {ppl.item():.2f}")
# print(f"Perplexity: {val}")

print(min)
print(max)

ind = np.argpartition(out1, 50)[0:50]
ind1 = np.argpartition(out1, -50)[-50:]

top_4 = out1[ind1]
top_4.sort()
top4 = out1[ind]
top4.sort()
print(top4)
print(top_4)

# ind2 = np.argpartition(out1, -50)[0:-50]
# val = np.average(out1[ind2])
output2 = np.array(output).astype('float')
out3 = np.sort(output2)
# print(output2[-50:])
# print(out3[600:704])
print(out3[800:1006])
# out4 = np.average(out3[:])

output_file = '/content/drive/My Drive/Data712/1.xlsx'
sheet_name = 'Sheet1'

with pd.ExcelWriter(output_file, mode='w') as writer:
    df.to_excel(writer, header=[f"{min} | {max}", "Bangla"], index=False)

# with pd.ExcelWriter(output_file, mode='a', if_sheet_exists="overlay", engine="openpyxl") as writer:
#             df.to_excel(writer, sheet_name=sheet_name,
#                          startcol=writer.sheets[sheet_name].max_column, header=[f"{min} | {max}", "Generated-Bangla-1-Shot"], index=False)
