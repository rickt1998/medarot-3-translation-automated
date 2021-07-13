import pandas as pd
from googletrans import Translator
pd.options.mode.chained_assignment = None  # default='warn'

dfs = pd.read_excel("sheet.xlsx", sheet_name=None)

translator = Translator()

for sheet_name, df in dfs.items():
    try:
        print(sheet_name)
        original = df['Original']
        for row_number, line in enumerate(original):
            print(line)
            if line == '<FINAL>':
                break
            translated = translator.translate(line, dest='ja', src='en')
            print(translated)
            df.loc[row_number, 'Translated'] = translated
    except KeyError:
        pass
    writer = pd.ExcelWriter('output.xlsx')
    df.to_excel(writer, sheet_name=sheet_name)
    writer.save()
