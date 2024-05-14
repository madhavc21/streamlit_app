import streamlit as st

st.title("Virtual Wardrobe")
st.divider()
st.file_uploader("Upload new", type=None, accept_multiple_files=True, key=ImgUpload, help="Upload a new item to your wardrobe", on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")
