import streamlit as st
import os

# ── Page config ──────────────────────────────────────────────────
st.set_page_config(
    page_title="Bayanihan Emirates Business Services",
    page_icon="🇦🇪",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Hide Streamlit chrome for a clean full-page look ─────────────
st.markdown("""
    <style>
        #MainMenu, header, footer { visibility: hidden; }
        .block-container { padding: 0 !important; max-width: 100% !important; }
        iframe { border: none; }
    </style>
""", unsafe_allow_html=True)

# ── Load the HTML file ───────────────────────────────────────────
html_file = os.path.join(os.path.dirname(__file__), "index.html")

if os.path.exists(html_file):
    with open(html_file, "r", encoding="utf-8") as f:
        html_content = f.read()
    st.components.v1.html(html_content, height=6000, scrolling=True)
else:
    st.error("index.html not found. Place it in the same folder as app.py")
