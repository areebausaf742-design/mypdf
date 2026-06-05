import streamlit as st
import pdfplumber
import io

st.title("🚀 Professional PDF to Paragraph Converter")
st.write("Convert your PDFs into clean, paragraph-formatted text instantly.")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    with pdfplumber.open(uploaded_file) as pdf:
        full_text = ""
        for page in pdf.pages:
            text = page.extract_text(layout=True)
            if text:
                # Logic to keep paragraphs clean
                paragraphs = text.replace('\n\n', '[[P]]').replace('\n', ' ').replace('[[P]]', '\n\n')
                full_text += paragraphs + "\n\n"

    st.text_area("Converted Text", full_text, height=300)
    st.download_button("Download Text File", full_text, file_name="converted_text.txt")
    st.markdown("---")
st.subheader("Why use this tool?")
st.write("Our converter preserves paragraph spacing, making it perfect for copying text into Word or Google Docs without messy line breaks.")

st.subheader("Privacy & Security")
st.info("Your privacy is our priority. We do not save, store, or share your PDF files. All processing happens instantly and safely.")

