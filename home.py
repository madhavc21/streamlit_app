import streamlit as st
import os
from PIL import Image

st.title("Virtual Wardrobe")
st.divider()

# File uploader widget
image_file = st.file_uploader("Choose images", accept_multiple_files=True, type=['jpg', 'png', 'jpeg'])

# if image_file is not None:
#     st.image(image_file)
#     with open(os.path.join("upload",image_file),"wb") as f: 
#       f.write(image_file.getbuffer())         
#     st.success("Saved File")

lst2 = ['kurta_men', 'frock', 'jeans', 'shoes', 'gowns', 'pants', 'hoodie', 'saree', 'leggings_and_salwars', 'women_kurta', 'blouse', 'lehenga']
count = 0
for class_name in lst2:
  s = str.capitalize(class_name.replace("_", " "))
  st.write(f"{s} \n")
  
  for i in image_file:
    col = st.columns(1)
    with col: 
      st.image(i, width = 100)