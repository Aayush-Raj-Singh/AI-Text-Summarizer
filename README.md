# 🧠 AI Text Summarizer

A powerful AI-based web application that intelligently summarizes long texts, articles, or essays using cutting-edge NLP models from Hugging Face. Built with Streamlit for a sleek user interface and designed to run on CPU.

---

## 🚀 Features

- 📄 Summarize plain text or `.txt` file uploads
- 🤖 Choose from models: `facebook/bart-large-cnn`, `t5-small`
- 🎛️ Adjustable summary length via sliders
- 📥 Download the summary in `.txt` format
- 🎨 Custom-styled UI with HTML & CSS via Streamlit
- 🧠 Powered by Hugging Face Transformers
- 💻 CPU-friendly, no GPU required

---

## 📁 Project Structure

<pre lang="markdown">
   ``` AI-Text-Summarizer/ 
   │ ├── app.py # Main Streamlit application script
   ├── requirements.txt # List of required Python packages
   ├── README.md # Project documentation
   └── example_summary.txt # Optional: example output file ``` 
</pre>

---

## ⚙️ How It Works

1. **User Input**:
   - Upload a `.txt` file or manually enter text.
2. **Preprocessing**:
   - Cleans and prepares text input.
3. **Model Selection**:
   - Choose between BART (`facebook/bart-large-cnn`) or T5 (`t5-small`).
4. **Summarization**:
   - Uses Hugging Face’s `pipeline` with selected model.
5. **Customization**:
   - User adjusts `min_length` and `max_length` sliders.
6. **Output**:
   - Display summary, download option, word count feedback.

---

## 🔧 Future Features

- 📝 Support for `.pdf` and `.docx` file formats
- 🌐 Multilingual summarization support
- 📊 Summary quality metrics
- 🧵 Text segmentation and topic highlighting
- 🗣️ Text-to-speech for summaries
- 🧪 Model benchmarking (ROUGE, BLEU scoring)

---

## 🙌 Credits

- **Framework**: [Streamlit](https://streamlit.io/)
- **NLP Models**: [Hugging Face Transformers](https://huggingface.co/)
- **Design Inspiration**: OpenAI, Hugging Face community
- **Developer**: [Aayush Raj Singh](https://github.com/Aayush-Raj-Singh)

---

## 📜 License

This project is licensed under the MIT License.  
Feel free to use, modify, and share responsibly.

---

## ⭐ Support

If you found this helpful, please consider giving a ⭐ on GitHub!
