import streamlit as st
import os
from PIL import Image

st.title("Virtual Wardrobe")
st.divider()

# File uploader widget
uploaded_images = st.file_uploader("Choose images", accept_multiple_files=True, type=['jpg', 'png', 'jpeg'])

# Save uploaded files to 'upload' directory
if uploaded_images is not None:
  for uploaded_image in uploaded_images:
          # Construct the file path
          file_path = os.path.join('upload', uploaded_image)
          image = Image.open(uploaded_image)
          image.save(file_path)
     
for filename in os.listdir('upload'):
      st.write(filename)

lst2 = ['kurta_men', 'frock', 'jeans', 'shoes', 'gowns', 'pants', 'hoodie', 'saree', 'leggings_and_salwars', 'women_kurta', 'blouse', 'lehenga']
for class_name in lst2:
  s = str.capitalize(class_name.replace("_", " "))
  st.write(f"{s} \n")
  for image in os.listdir('upload'): 
    st.image(image) 