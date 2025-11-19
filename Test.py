import streamlit as st

st.title("Test Multiple PDF Uploads")

files = st.file_uploader(
    "Upload PDF files",
    type=["pdf"],
    accept_multiple_files=True
)

if files:
    st.success(f"Uploaded {len(files)} files:")
    for f in files:
        st.write("📄 " + f.name)
