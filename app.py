import streamlit as st
import pathlib

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

html_path = pathlib.Path(__file__).resolve().parent / "index.html"

if html_path.is_file():
    html_content = html_path.read_text(encoding="utf-8")
    st.components.v1.html(html_content, height=9000, scrolling=True)
else:
    st.error("index.html not found.")
    st.write([str(p) for p in pathlib.Path(__file__).resolve().parent.iterdir()])
