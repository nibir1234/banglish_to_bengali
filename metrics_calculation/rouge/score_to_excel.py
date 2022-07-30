import pandas as pd


# //* writing first time
# with pd.ExcelWriter('output.xlsx', mode='w') as writer:
#     pd.read_json("input.json").to_excel(writer,
#                                         sheet_name="Sheet1",)


# //* appending
with pd.ExcelWriter('output.xlsx', mode='a', if_sheet_exists="overlay") as writer:
    pd.read_json("input.json").to_excel(writer,
                                        index=False,
                                        sheet_name="Sheet1",
                                        startcol=writer.sheets["Sheet1"].max_column,)
