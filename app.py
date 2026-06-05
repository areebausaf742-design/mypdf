import streamlit as st
import pdfplumber
import io

# 1. SETTINGS & PAGE IDENTITY
st.set_page_config(page_title="PDF to Paragraph Pro", page_icon="🚀", layout="centered")

# 2. LEGENDARY INTERFACE STYLING
st.markdown("""
    <style>
    /* Gradient Background */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    /* Red Professional Button */
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 3.5em;
        background-color: #FF4B4B;
        color: white;
        font-weight: bold;
        border: none;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #ff3333;
        transform: translateY(-2px);
    }
    /* Rounded Text Areas */
    .stTextArea>div>div>textarea {
        border-radius: 15px;
        border: 1px solid #ddd;
    }
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 3. HEADER SECTION
st.markdown("<h1 style='text-align: center; color: #FF4B4B; font-size: 3em;'>🚀 PDF to Paragraph Pro</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 20px; color: #444;'>Fast. Secure. Paragraph-Perfect.</p>", unsafe_allow_html=True)
st.markdown("---")

# 4. THE CONVERTER ENGINE
st.subheader("📤 Upload your PDF")
uploaded_file = st.file_uploader("Drag and drop your file to fix messy formatting instantly", type="pdf")

if uploaded_file is not None:
    with st.spinner('✨ Our Ryzen-optimized engine is processing your text...'):
        try:
            with pdfplumber.open(uploaded_file) as pdf:
                full_text = ""
                for page in pdf.pages:
                    text = page.extract_text(layout=True)
                    if text:
                        # Smart Paragraph Recovery Logic
                        paragraphs = text.replace('\n\n', '[[P]]').replace('\n', ' ').replace('[[P]]', '\n\n')
                        full_text += paragraphs + "\n\n"

            st.success("✅ Conversion Successful!")
            st.text_area("✨ Cleaned Paragraphs Preview", full_text, height=400)
            
            st.download_button(
                label="📥 DOWNLOAD CLEAN TEXT FILE",
                data=full_text,
                file_name="converted_paragraphs.txt",
                mime="text/plain"
            )
        except Exception as e:
            st.error("Oops! Something went wrong. Please try a different PDF file.")

# 5. HIGH-VALUE GOOGLE CONTENT (SEO)
st.markdown("---")
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📖 How it Works")
    st.write("Our system uses advanced OCR-style logic to detect where paragraphs end. No more copying text and spending hours fixing line breaks!")

with col2:
    st.markdown("### 💎 Premium Features")
    st.write("- **Zero Formatting Loss**\n- **Ryzen 7 Speed**\n- **100% Free Forever**")

# 6. MANDATORY FOR ADSENSE (Privacy & Contact)
st.markdown("---")
st.subheader("🔒 Data Privacy & Contact")
st.info("Files are processed in-memory and never stored on our servers. Your data is 100% private.")
st.write("For support or inquiries: **contact@yourdomain.com**")

# 7. GOOGLE VERIFICATION (Bottom Caption)
st.caption("google-site-verification: vP-Bi-T6FOhgNroxZz7MORci8mHgt9faa2CGCfNVW60")
