import streamlit as st
import os

st.set_page_config(
    page_title="Bayanihan Emirates Business Services",
    page_icon="🇦🇪",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container { padding: 0 !important; max-width: 100% !important; }
        [data-testid="stAppViewContainer"] { padding: 0 !important; }
    </style>
""", unsafe_allow_html=True)

# Try every possible location Streamlit Cloud might use
possible_paths = [
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html"),
    "/mount/src/bayanihanbusinessservices/index.html",
    os.path.join(os.getcwd(), "index.html"),
    "index.html",
]

html_content = None
for path in possible_paths:
    if os.path.isfile(path):
        with open(path, "r", encoding="utf-8") as f:
            html_content = f.read()
        break

if html_content:
    st.components.v1.html(html_content, height=9000, scrolling=True)
else:
    st.error("Could not load index.html")
