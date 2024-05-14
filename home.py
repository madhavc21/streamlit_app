import streamlit as st
from PIL import Image

st.title("Virtual Wardrobe")
st.divider()
upload = st.file_uploader("Upload new", type=None, accept_multiple_files=True)
if upload is not None:
  for image in upload:
    images = Image.open(image)
    images.save('/workspaces/streamlit_app/upload')
# with open("/workspaces/streamlit_app/upload") as uploaded:
#   uploaded = upload.read()
lst2 = ['kurta_men', 'frock', 'jeans', 'shoes', 'gowns', 'pants', 'hoodie', 'saree', 'leggings_and_salwars', 'women_kurta', 'blouse', 'lehenga']
for class_name in lst2:
  s = str.capitalize(class_name.replace("_", " "))
  st.write(f"{s} \n")
  st.image(upload) 