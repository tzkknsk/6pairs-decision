import streamlit as st
from PIL import Image
import random
import pandas as pd

st.header("【第１部―１】")
st.header(" サイコロβおよびγの出目の決定")

buttom = st.button('決定')
st.subheader("")

dic = {} 

def get_color(n):

    if n % 2 == 0:
        color = "緑"
        color_en = "Green"
        return [color, color_en]

    elif n % 2 == 1:
        color = "赤"
        color_en = "Red"
        return [color, color_en]

if buttom:
    for i in range(1, 25):
        dice_b = random.randint(1, 6)
        dice_g = random.randint(1, 6)
        dice_g_color_ls = get_color( dice_g )

        st.header(f"【 NO. {i} 】")

        st.subheader(f"サイコロ β : {dice_b}")
        st.subheader(f"サイコロ γ : {dice_g} ({dice_g_color_ls[0]})")
        
        dic[i] = [dice_b, dice_g, dice_g_color_ls[1]]

st.subheader("")

## ---------- 回答結果の出力 ---------- ##

def convert_df(df):
     # IMPORTANT: Cache the conversion to prevent computation on every rerun
     return df.to_csv().encode('utf-8')

output_dict={}
for k,v in dic.items():   # 一度pd.Seriesに変換
    output_dict[k]=pd.Series(v)

df = pd.DataFrame(output_dict)

def convert_df(df):
     # IMPORTANT: Cache the conversion to prevent computation on every rerun
     return df.to_csv(index=False).encode('utf-8')

csv = convert_df(df)

st.download_button(
     label="結果を出力(csv)",
     data=csv,
     file_name= f'Question1-1.csv',
     mime='text/csv',
 )
