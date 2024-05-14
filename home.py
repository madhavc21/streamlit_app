import streamlit as st

st.title("Virtual Wardrobe")
st.divider()
st.file_uploader("Upload new", type=None, accept_multiple_files=True, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")
