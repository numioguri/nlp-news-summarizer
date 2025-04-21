# 📰 News Translation and Summarization

A Natural Language Processing (NLP) project that translates and summarizes multilingual news articles using state-of-the-art transformer models. It features a simple Flask-based UI for user interaction and provides evaluation metrics using ROUGE and BLEU.

---

## 🚀 Features

- 🌐 **Translation**: Converts text from source to target language using **MarianMT**.
- 🧠 **Summarization**: Generates concise summaries using **BART**.
- 📊 **Evaluation**: Includes ROUGE and BLEU score computation for quality assessment.
- 💻 **UI**: Interactive web interface built with **Flask**.
- 📦 **Lightweight**: No need for GPU; works with CPU too.

---

## 🧰 Tech Stack

| Feature         | Technology        |
|----------------|-------------------|
| Translation     | MarianMT (Hugging Face) |
| Summarization   | BART (Hugging Face)     |
| Evaluation      | ROUGE, BLEU        |
| Web Framework   | Flask              |
| Tokenization    | NLTK               |

---

## 📁 Project Structure

news-translation-summarization/ ├── app.py # Flask app entry point ├── translate.py # MarianMT translation logic ├── summarize.py # BART summarization logic ├── evaluate.py # ROUGE/BLEU evaluation logic ├── download_nltk.py # Downloads punkt tokenizer ├── requirements.txt # Project dependencies ├── templates/ │ └── index.html # UI template ├── static/ │ └── style.css # Custom styling

1. Clone the repo  
   ```bash
   git clone https://github.com/numioguri/nlp-news-summarizer.git
   cd nlp-news-summarizer

2. Install dependencies
pip install -r requirements.txt


3. Download NLTK tokenizer

python download_nltk.py

4 Run the Flask app
python app.py
Then go to http://127.0.0.1:5000 in your browser.

Licence

---
This project is licensed under the MIT License. See LICENSE for details
