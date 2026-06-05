import streamlit as st
import pdfplumber
import io
# GOOGLE VERIFICATION CODE - Keep this at the top
st.set_page_config(page_title="PDF to Paragraph Converter", page_icon="🚀")

# This invisible component tells Google you own the site
st.components.v1.html(
    """
    <meta name="google-site-verification" content="vP-Bi-T6FOhgNroxZz7MORci8mHgt9faa2CGCfNVW60" />
    """,
    height=0,
    
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

st.markdown("---")

# 1. THE GUIDE (Google loves this for SEO)
st.subheader("📖 How to Use This Converter")
st.write("""
1. **Upload:** Click the 'Browse files' button to select your PDF.
2. **Convert:** Our engine automatically identifies and preserves your paragraphs.
3. **Copy or Download:** View the text in the window above or click 'Download Text File' to save it to your computer.
""")

# 2. THE VALUE (Why your site is better)
st.subheader("💡 Why use this tool?")
st.write("Most converters create messy line breaks. Our tool uses smart paragraph detection to ensure your text is ready for Word or Google Docs immediately.")

# 3. THE PRIVACY (Keep this at the very bottom)
st.subheader("🔒 Privacy & Security")
st.info("Your privacy is our priority. We do not save, store, or share your PDF files. All processing happens instantly in your session and files are deleted immediately after.")


