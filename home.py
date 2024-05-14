import streamlit as st

st.title("Virtual Wardrobe")
st.divider()
st.file_uploader("Upload new", type=None, accept_multiple_files=True)

lst2 = ['kurta_men', 'frock', 'jeans', 'shoes', 'gowns', 'pants', 'hoodie', 'saree', 'leggings_and_salwars', 'women_kurta', 'blouse', 'lehenga']
for class_name in lst2:
  s = str.capitalize(class_name.replace("_", " "))
  st.write(f"{class_name} \n")
