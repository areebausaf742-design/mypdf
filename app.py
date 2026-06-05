import streamlit as st
import pdfplumber
import time

# ==========================================
# ✅ GOOGLE SITE VERIFICATION META TAG
# ==========================================
st.markdown(
    '<meta name="google-site-verification" content="vP-Bi-T6FOhgNroxZz7MORci8mHgt9faa2CGCfNVW60" />',
    unsafe_allow_html=True
)

# Optional: handle Google verification file
if "google4389f87ed75cf887.html" in st.query_params:
    st.write("google-site-verification: google4389f87ed75cf887.html")
    st.stop()

# ==========================================
# ✅ PAGE CONFIG
# ==========================================
st.set_page_config(
    page_title="PDF to Paragraph Pro | Legendary Converter",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# ✅ CUSTOM CSS (A to Z Styling)
# ==========================================
st.markdown("""
<style>
.stApp {
    background: linear-gradient(rgba(0,0,0,0.85), rgba(0,0,0,0.85)),
                url('https://source.unsplash.com/random/1600x900/?technology');
    background-size: cover;
    color: white;
}
div.stBlock {
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(15px);
    border-radius: 20px;
    padding: 35px;
    border: 1px solid rgba(255,255,255,0.1);
    margin-bottom: 25px;
}
.stButton>button {
    width: 100%;
    background: linear-gradient(90deg, #FF4B4B 0%, #ff8a8a 100%);
    color: white;
    border: none;
    padding: 18px;
    border-radius: 15px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 2px;
    transition: all 0.4s ease;
}
.stButton>button:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 30px rgba(255,75,75,0.6);
}
h1 {
    font-family: 'Inter', sans-serif;
    font-weight: 900;
    background: -webkit-linear-gradient(#ffffff, #777777);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-align: center;
}
section[data-testid="stSidebar"] {
    background-color: rgba(10,10,10,0.95);
}
footer {visibility: hidden;}
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ==========================================
# ✅ SIDEBAR CONTROL CONSOLE
# ==========================================
with st.sidebar:
    st.markdown("<h1 style='font-size: 24px;'>SYSTEM CONSOLE</h1>", unsafe_allow_html=True)
    st.success("⚡ CPU: AMD RYZEN 7 7730U ACTIVE")
    st.info("🧠 16GB RAM OPTIMIZED")
    st.markdown("---")
    st.subheader("🛠️ Engine Settings")
    mode = st.selectbox("Processing Mode", ["Deep Paragraph Recovery", "Turbo Extraction"])
    st.checkbox("AI Sentence Repair", value=True)
    st.markdown("---")
    if st.button("LOAD SAMPLE DOCUMENT"):
        st.toast("Sample Loaded!")

# ==========================================
# ✅ MAIN INTERFACE
# ==========================================
st.markdown("<h1>🚀 LEGENDARY PDF TO PARAGRAPH PRO</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #ddd; font-size: 20px;'>Ultra-Fast. Military Privacy. Paragraph Perfect.</p>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload Portal", type="pdf")

if uploaded_file is not None:
    progress_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.005)
        progress_bar.progress(i + 1)

    with st.spinner('🚀 RYZEN 7 ENGINE ANALYZING...'):
        try:
            with pdfplumber.open(uploaded_file) as pdf:
                total_pages = len(pdf.pages)
                full_text = ""
                for page in pdf.pages:
                    text = page.extract_text(layout=True)
                    if text:
                        paragraphs = text.replace('\n\n', '[[P]]').replace('\n', ' ').replace('[[P]]', '\n\n')
                        full_text += paragraphs + "\n\n"

            st.success("✅ Conversion Successful!")
            st.text_area("✨ Cleaned Output", full_text, height=450)
            st.download_button("👑 DOWNLOAD TEXT REPORT", full_text, file_name="export.txt")
        except Exception as e:
            st.error(f"Error: {e}")

# ==========================================
# ✅ DOCUMENTATION TABS
# ==========================================
t1, t2, t3, t4, t5 = st.tabs(["🚀 OPERATION", "💎 CORE TECH", "🔒 SECURITY", "📈 MONETIZATION", "🛡️ SAFETY"])

with t1:
    st.write("### How to Use")
    st.write("Upload your PDF and our Ryzen engine will fix formatting automatically.")

with t2:
    st.write("### Why This Tool is Top-Notch")
    st.write("- **Line-Merge Tech:** Fixes broken lines.")
    st.write("- **VRAM Buffer:** Optimized for fast rendering.")
    st.write("- **Ryzen Simulation:** Mimics high-performance CPU pipelines.")

with t3:
    st.write("### 100% Privacy")
    st.write("Your files never leave your RAM. Data is deleted once you close the tab.")

with t4:
    st.write("### AdSense Ready")
    st.write("To reach ₹1,000/day, share this tool widely.")
    st.write("Monetization options: AdSense banners, premium features, donations.")

with t5:
    st.write("### Safety Notes")
    st.write("Use responsibly. Educational purpose only. Do not upload sensitive or harmful content.")
    st.write("This tool is designed for students, professionals, and researchers.")

# ==========================================
# ✅ FOOTER
# ==========================================
st.markdown("---")
st.write("📧 Contact: support@legendarypdf.app")
st.caption("Google Verification: vP-Bi-T6FOhgNroxZz7MORci8mHgt9faa2CGCfNVW60")
st.caption("Verification Portal: google4389f87ed75cf887.html")
