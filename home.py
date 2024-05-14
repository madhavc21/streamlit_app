import streamlit as st
import os
from PIL import Image

st.title("Virtual Wardrobe")
st.divider()

# File uploader widget
image_file = st.file_uploader("Choose images", accept_multiple_files=True, type=['jpg', 'png', 'jpeg'])

if image_file is not None:
    img = Image.open(image_file)
    st.image(img,height=250,width=250)
    with open(os.path.join("upload",image_file.name),"wb") as f: 
      f.write(image_file.getbuffer())         
    st.success("Saved File")

lst2 = ['kurta_men', 'frock', 'jeans', 'shoes', 'gowns', 'pants', 'hoodie', 'saree', 'leggings_and_salwars', 'women_kurta', 'blouse', 'lehenga']
for class_name in lst2:
  s = str.capitalize(class_name.replace("_", " "))
  st.write(f"{s} \n")
  for i in os.listdir("upload"):
    img = Image.open(i)
    st.image(img)