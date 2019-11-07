# -*- coding: utf8 -*-
import pandas as pd
from io import open

data = pd.read_excel(r'data_vat_lieu_no.xlsx')
df = pd.DataFrame(data, columns=['Question', 'Answer'])

text_file = open("Output.txt", "w", encoding='utf-8')

for i in range(len(df)):
    q = df['Question'][i]
    a = df['Answer'][i]
    # total = 'Question:' + q + 'Answer:' + a + '\n'

    text_file.write(unicode('Question:' + str(q)))
    text_file.write(unicode('Answer:' + str(a)))

    # exit()

exit()
text_file.write(unicode(a))
