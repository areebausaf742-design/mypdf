import streamlit as st
import pdfplumber
import time
import base64

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="PDF Master Pro | AI Cleaner Tool",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# SIMPLE STATE (for virality tracking)
# =========================
if "usage" not in st.session_state:
    st.session_state.usage = 0

st.session_state.usage += 1

# =========================
# CUSTOM UI STYLE
# =========================
st.markdown("""
<style>
.stApp {
    background: linear-gradient(120deg, #0f172a, #1e293b);
    color: white;
}

.title {
    font-size: 42px;
    text-align: center;
    font-weight: 900;
    background: linear-gradient(90deg, #60a5fa, #a78bfa);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    opacity: 0.8;
    margin-bottom: 20px;
}

.card {
    background: rgba(255,255,255,0.06);
    padding: 20px;
    border-radius: 15px;
    margin: 10px 0;
}

button {
    border-radius: 10px !important;
}

footer {visibility: hidden;}
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR DASHBOARD
# =========================
with st.sidebar:
    st.title("📊 Dashboard")

    st.metric("👁️ App Opens", st.session_state.usage)

    st.markdown("---")
    st.subheader("💎 Premium Plan")

    st.write("Unlock Pro Features:")
    st.write("• Unlimited PDF pages")
    st.write("• Faster processing")
    st.write("• Clean formatting AI")

    st.code("UPI: yourupi@okaxis")

    if st.button("I PAID (Unlock Premium)"):
        st.success("Premium unlocked (manual verification)")

    st.markdown("---")
    st.subheader("🔥 Affiliate Tools")

    st.write("Recommended:")
    st.write("• Canva Pro")
    st.write("• Grammarly")
    st.write("• Adobe PDF tools")

    st.markdown("---")
    st.info("Share this app to earn traffic 🚀")

# =========================
# HEADER
# =========================
st.markdown('<div class="title">📄 PDF MASTER PRO</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI-powered PDF cleaner • Fast • Clean • Student friendly</div>', unsafe_allow_html=True)

# =========================
# VIRAL SHARE BLOCK
# =========================
share_url = "https://khebhy46t6ong8w9swbnlu.streamlit.app/"

st.markdown("### 🔥 Share & Earn Reach")
st.code(share_url)

st.write("Copy & share this link in WhatsApp / Telegram / Instagram")

# =========================
# FILE UPLOAD
# =========================
uploaded_file = st.file_uploader("📤 Upload your PDF", type="pdf")

# =========================
# PROCESSING
# =========================
if uploaded_file:

    progress = st.progress(0)

    for i in range(100):
        time.sleep(0.003)
        progress.progress(i + 1)

    full_text = ""

    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                clean = text.replace("\n\n", "\n").replace("\n", " ")
                full_text += clean + "\n\n"

    st.success("✅ PDF Converted Successfully!")

    # OUTPUT BOX
    st.text_area("📄 Clean Output", full_text, height=400)

    # DOWNLOAD BUTTON
    st.download_button(
        "⬇️ Download Text",
        full_text,
        file_name="pdf_output.txt"
    )

    # COPY FEATURE
    st.code(full_text[:1000] + "...")

# =========================
# FEATURES SECTION
# =========================
st.markdown("## ⚡ Features")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    ### 🚀 Fast Processing
    Clean text extraction in seconds
    """)

with col2:
    st.markdown("""
    ### 💎 Premium Upgrade
    Unlock advanced formatting tools
    """)

with col3:
    st.markdown("""
    ### 🔒 Privacy First
    Files processed in session memory
    """)

# =========================
# MONETIZATION SECTION
# =========================
st.markdown("## 💰 Earn With This Tool")

st.markdown("""
### 1. Premium Upgrade (₹49)
- Unlimited PDFs
- Faster processing
- No limits

### 2. Affiliate Income
- Recommend tools like Canva, Grammarly
- Earn commission per signup

### 3. Donations
- Small support from users
""")

# =========================
# VIRAL CTA
# =========================
st.markdown("## 🔥 Help This Tool Grow")

if st.button("⭐ Share This Tool"):
    st.success("Copy link and share it in 5 groups to grow faster!")
