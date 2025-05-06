import streamlit as st
import torch
from transformers import pipeline

st.set_page_config(
    page_title="AI based Smart Text Summarizer",
    page_icon="📝",
    layout="centered",
    initial_sidebar_state="auto"
)


torch.device("cpu")

@st.cache_resource
def load_model(model_name="facebook/bart-large-cnn"):
    print(f"Hey, loading up the '{model_name}' model...")
    return pipeline("summarization", model=model_name)

st.markdown(
    """
    <style>
    .main {background-color: #f9f9f9;}
    h1 {text-align: center; color: #3E64FF;}
    .block-container {padding-top: 2rem;}
    .stTextArea label, .stFileUploader label {
        font-weight: bold;
        font-size: 1.1rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title(" 🤖 Smart Text Summarizer")
st.subheader("Got a long piece of text? Let me help you get the gist in seconds!")

uploaded_file = st.file_uploader("📄 Got a .txt file? Upload it here:", type=["txt"])
input_text = ""

if uploaded_file:
    input_text = uploaded_file.read().decode("utf-8")
    st.text_area("📚 Here's what's in your file:", input_text, height=250)
else:
    input_text = st.text_area("✍️ Or just paste your text right here:", height=250)

# Quick word count for the curious
word_count = len(input_text.split())
if input_text:
    st.write(f"Word count: `{word_count}` words")

# Let's add some controls for how the summary is made
st.markdown("---")
st.subheader("⚙️ Tweak the Summary Settings")

model_name = st.selectbox(
    "Pick a summarization engine:",
    ["facebook/bart-large-cnn", "t5-small"],
    help="Different models have different strengths. Give them a try!"
)

max_len = st.slider("📏 Maximum Summary Length", 50, 1000, 130)
min_len = st.slider("🤏 Minimum Summary Length", 10, 100, 30)

summarizer = load_model(model_name)

st.markdown("---")
if st.button("✨ Generate Summary"):
    if word_count < 10:
        st.warning("Hmm, that text looks a bit short. Maybe paste something longer?")
    else:
        with st.spinner("Thinking hard and summarizing..."):
            cleaned_text = input_text.strip()
            result = summarizer(cleaned_text, max_length=max_len, min_length=min_len, do_sample=False)
            summary = result[0]['summary_text']

        st.success("✅ Let's! Here's your summary:")
        st.text_area("📄 The Summary", summary, height=200)

        st.download_button("💾 Download this summary as a .txt file", summary, file_name="summary.txt", mime="text/plain")

st.markdown("---")
st.markdown(
    "<center>Made with lots of ❤️ and 🦾 using <b>Streamlit</b> and the magic of <b>Hugging Face Transformers</b>!</center>",
    unsafe_allow_html=True
)