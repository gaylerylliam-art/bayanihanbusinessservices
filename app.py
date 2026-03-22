import streamlit as st
import os

st.set_page_config(
    page_title="Bayanihan Emirates Business Services",
    page_icon="🇦🇪",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit default UI chrome
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {
            padding: 0 !important;
            max-width: 100% !important;
        }
        [data-testid="stAppViewContainer"] {
            padding: 0 !important;
        }
        [data-testid="stVerticalBlock"] {
            gap: 0 !important;
        }
    </style>
""", unsafe_allow_html=True)

# Locate the HTML file — handles both local dev and Streamlit Cloud
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Common candidate filenames
candidates = [
    os.path.join(BASE_DIR, "index.html"),
    os.path.join(BASE_DIR, "bayanihan_emirates_landing.html"),
    os.path.join(BASE_DIR, "landing.html"),
]

html_file = None
for candidate in candidates:
    if os.path.isfile(candidate):
        html_file = candidate
        break

if html_file is None:
    st.error(
        "HTML file not found. Make sure index.html is in the same folder as app.py."
    )
    st.write("**Files found in directory:**")
    for f in sorted(os.listdir(BASE_DIR)):
        st.write(f"- `{f}`")
else:
    with open(html_file, "r", encoding="utf-8") as f:
        html_content = f.read()

    st.components.v1.html(html_content, height=8000, scrolling=True)
