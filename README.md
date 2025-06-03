# 🧠 AI Text Summarizer

A web-based AI summarization tool developed as part of the **Foundations of Artificial Intelligence Internship (April 2025)** conducted by **Edunet Foundation** in collaboration with **Microsoft** and **AICTE**. This project applies advanced NLP models to efficiently condense long texts, articles, or essays using Hugging Face Transformers and a Streamlit interface.

---

## 🚀 Features

- 📄 Summarize raw input or uploaded `.txt` files
- 🤖 Choose between pretrained models: `facebook/bart-large-cnn` or `t5-small`
- 🎛️ Control summary length with intuitive sliders
- 📥 Download generated summaries as `.txt` files
- 🎨 Stylish and responsive UI using Streamlit’s HTML/CSS features
- 💻 Optimized for CPU-based execution—no GPU needed

---

## 📁 Project Structure

```
AI-Text-Summarizer/
├── app.py              # Main Streamlit application
├── requirements.txt    # Required Python dependencies
├── README.md           # Documentation
└── sample.txt          # Sample text file for testing
```

---

## ⚙️ How It Works

1. **User Input**:
   - Upload `.txt` file or type/paste text.
2. **Preprocessing**:
   - Cleans and processes text.
3. **Model Selection**:
   - Choose between BART or T5 from Hugging Face.
4. **Summarization**:
   - Uses the `pipeline("summarization")` API.
5. **Customization**:
   - Adjust `min_length` and `max_length` sliders for control.
6. **Output**:
   - Display summary, view word count, and download result.

---

## 🧪 Example

**Input:**
> "Artificial Intelligence is the simulation of human intelligence processes by machines..."

**Summary:**
> "AI simulates human intelligence processes using machines..."

---

## 🎓 Internship Context

This project was created during a **4-week AI internship** (April 2025) organized by:

- 🏢 **Edunet Foundation**
- 🤝 **Microsoft (MS AI-NSI)**
- 🏛️ **AICTE (All India Council for Technical Education)**

Key Learnings:
- Fundamentals of AI, ML, DL, and Gen-AI
- Hands-on with supervised/unsupervised learning
- Computer Vision and Azure demos
- Deep learning and neural network implementation
- Project development with real-world application

---

## 🔮 Future Enhancements

- 📄 Support for `.pdf` and `.docx` formats
- 🌐 Multilingual summarization capabilities
- 📊 Summary quality metrics (ROUGE, BLEU)
- 🧵 Topic segmentation and highlighting
- 🗣️ Text-to-speech integration
- 🧪 Model benchmarking suite

---

## 📜 License

MIT License  
Free to use, modify, and distribute responsibly.

---

## 🙌 Credits

- **Framework**: [Streamlit](https://streamlit.io/)
- **NLP Models**: [Hugging Face Transformers](https://huggingface.co/)
- **Internship Program**: Microsoft, AICTE & Edunet Foundation
- **Developer**: [Aayush Raj Singh](https://github.com/Aayush-Raj-Singh)

---

## ⭐ Support

If this project helped you, give it a ⭐ on GitHub and connect with me on [LinkedIn](https://www.linkedin.com/in/](https://www.linkedin.com/in/aayush-raj-77a1bb237 
).
