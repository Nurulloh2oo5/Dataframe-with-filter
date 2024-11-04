# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1a1fZckp2hP-xU_mghVmr-NyDG2EkTt2x
"""

import pandas as pd
baza = {
    "FISH":["Boymirzayev Ali","Toxtasinov Boynazar","Yusufjonov Muhsinjon","Abdurasulova Sarvinoz","Yolchiyeva Muxbira","Adhamova Farogat","Hasanboyeva Mubina","Hasanboyeva Bibiosiyo","Xonqulov Muhammadjon","Aminjonov Abdullox"],
    "YOSHI":["19","18","20","19","20","18","12","13","19","15"  ],
    "JINSI":["o'gil bola","o'gil bola","o'gil bola","qiz bola","qiz bola","qiz bola","qiz bola","qiz bola","o'gil bola","o'gil bola"  ],
    "MAKTAB raqami":["23","Prezident Maktabi","12","5","34","23","54","54","1","36"   ],

}
df=pd.DataFrame(baza)
print(df)
df.to_excel("baza.xlsx")



filtr = df.loc[df["JINSI"]=="qiz bola"]
print(filtr)

filtr = df.loc[df["JINSI"]=="o'gil bola"]
print(filtr)

filtr = df.loc[df["MAKTAB raqami"]=="Prezident Maktabi"]
print(filtr)

filtr = df.loc[df["YOSHI"]>"15"]
print(filtr)

filtr = df.loc[df["YOSHI"]>"15"]
filtr = df.loc[df["JINSI"]=="o'gil bola"]

print(filtr)

filtr=df.loc[(df["YOSHI"]<"15")&(df["JINSI"]=="qiz bola")]

print(filtr)



filtr = df["YOSHI"].max()
print(filtr)

filtr = df["YOSHI"].mean()
print(filtr)