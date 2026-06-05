import streamlit as st
import pdfplumber
import io

# 1. SETTINGS & STYLING
st.set_page_config(page_title="PDF to Paragraph Pro", page_icon="📄", layout="centered")

# --- BEAUTIFUL INTERFACE CSS (FIXED) ---
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        height: 3em;
        background-color: #FF4B4B;
        color: white;
        font-weight: bold;
    }
    .stTextArea>div>div>textarea {
        border-radius: 10px;
    }
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 2. GOOGLE VERIFICATION CODE
# This text at the bottom helps Google verify your ownership
verification_code = "google-site-verification: vP-Bi-T6FOhgNroxZz7MORci8mHgt9faa2CGCfNVW60"

# 3. HEADER SECTION
st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>🚀 PDF to Paragraph Pro</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>The fastest way to clean up messy PDF text for Word or Google Docs.</p>", unsafe_allow_html=True)
st.markdown("---")

# 4. THE CONVERTER TOOL
st.subheader("📤 Upload your PDF")
uploaded_file = st.file_uploader("Drop your file here", type="pdf")

if uploaded_file is not None:
    with st.spinner('Fixing paragraphs...'):
        with pdfplumber.open(uploaded_file) as pdf:
            full_text = ""
            for page in pdf.pages:
                text = page.extract_text(layout=True)
                if text:
                    # Smart Paragraph Logic
                    paragraphs = text.replace('\n\n', '[[P]]').replace('\n', ' ').replace('[[P]]', '\n\n')
                    full_text += paragraphs + "\n\n"

    st.success("Conversion Successful!")
    st.text_area("✨ Cleaned Text Preview", full_text, height=400)
    
    st.download_button(
        label="📥 Download Cleaned Text",
        data=full_text,
        file_name="converted_paragraphs.txt",
        mime="text/plain"
    )

# 5. SEO & GOOGLE CONTENT
st.markdown("---")
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📖 How to Use")
    st.write("""
    1. Upload your PDF file.
    2. Wait for the Ryzen-speed engine.
    3. Copy the clean text above.
    """)

with col2:
    st.markdown("### 💡 Why us?")
    st.write("""
    - **No messy lines**
    - **100% Private**
    - **Super Fast**
    """)

st.markdown("---")
st.markdown("### 🔒 Privacy & Security")
st.info("We do not store your data. All processing is done instantly and securely in your session.")

# 6. VERIFICATION TAG (Bottom of the page)
st.caption(verification_code)
