import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from PIL import Image

anime1 = Image.open("static/images/anime1.jpg")
anime2 = Image.open("static/images/anime2.jpg")
anime3 = Image.open("static/images/anime3.jpg")

st.title("Anime Stats Analysis")

st.subheader("Data Info")
df = pd.read_csv("static/datasets/Anime.csv")
st.dataframe(df)


st.subheader("Release vs Rating")
fig, ax = plt.subplots(1, 1)
ax.scatter(df["Release_year"], df["Rating"])
st.pyplot(fig)

st.markdown("""<hr style="height:5px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

st.image(anime1)

st.markdown("""<hr style="height:5px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

type_list = list(df["Type"].unique())
type_values = []
for i in range(len(df["Type"].unique())) :
    type_values.append(df["Type"].value_counts().iloc[i])

st.subheader("Anime Types")

fig, ax = plt.subplots(1, 1)
_, _, per_labels = ax.pie(x=type_values, labels=df["Type"].unique(), autopct="%1.0f%%", pctdistance=0.7, labeldistance=1.2)
for i in range(len(per_labels)):
  per_labels[i].set_color("white")
st.pyplot(fig)

st.markdown("""<hr style="height:5px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)
st.image(anime2)
st.markdown("""<hr style="height:5px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)
studio_list = df.groupby("Studio")[["Studio", "Episodes"]].agg("mean").sort_values(by="Episodes", ascending=False).reset_index().head(10)
studio_list
st.markdown("""<hr style="height:5px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)
st.subheader("Studio vs Episodes")

fig, ax = plt.subplots(1, 1)
ax.bar(studio_list["Studio"], studio_list["Episodes"])
ax.set_xlabel("Studio")
ax.set_ylabel("Episodes")
plt.xticks(rotation=45)
st.pyplot(fig)
st.markdown("""<hr style="height:5px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)
st.image(anime3)
st.markdown("""<hr style="height:5px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)