# 💬 Sentiment Analyzer

An AI-powered web app that analyzes the emotional tone of any text and classifies it as Positive, Negative, or Neutral — with confidence scores for each.

---

## Features

### 🧠 AI Sentiment Detection
Paste any text — a product review, tweet, message, or article — and the app instantly analyzes its emotional tone using a state-of-the-art NLP model.

### 📊 Confidence Scores
Get a breakdown of all three sentiment categories (Positive, Negative, Neutral) with color-coded confidence bars so you can see exactly how the model weighted each one.

### ✍️ Real-time Character Counter
A live character counter updates as you type, giving you a clear view of your input length.

---

## Tech Stack

- **Backend:** Python, FastAPI
- **AI Model:** RoBERTa (`cardiffnlp/twitter-roberta-base-sentiment-latest`) via HuggingFace Transformers
- **Frontend:** HTML, CSS, JavaScript

---

## Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/Keerthailand/sentiment-analyzer.git
cd sentiment-analyzer
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### 3. Install dependencies

```bash
pip install transformers fastapi uvicorn torch
```

### 4. Run the app

```bash
uvicorn main:app --reload
```

### 5. Open in browser

```
http://localhost:8000
```

> **Note:** The first run will automatically download the RoBERTa model (~500MB). This only happens once and is cached locally after that.

---

## How It Works

1. User types or pastes text into the web interface
2. JavaScript sends the text to the FastAPI backend as JSON
3. FastAPI validates the input using Pydantic and passes it to the model
4. RoBERTa analyzes the sentiment and returns confidence scores for all three categories
5. Results are displayed with color-coded confidence bars (green = Positive, red = Negative, yellow = Neutral)

---

## Project Structure

```
sentiment-analyzer/
├── main.py          # FastAPI server and API endpoints
├── model.py         # HuggingFace model loading and inference
└── static/
    └── index.html   # Frontend UI
```

---

## Future Plans

- Support for bulk text analysis (paste multiple reviews at once)
- Emoji and slang handling improvements
- Export results as CSV
- API endpoint for integration with other apps
