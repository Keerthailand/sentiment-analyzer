from transformers import pipeline

# Load pretrained sentiment analysis model
sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment-latest"
)

LABEL_MAP = {
    "positive": "Positive",
    "negative": "Negative",
    "neutral": "Neutral"
}

def analyze_sentiment(text: str):
    results = sentiment_pipeline(text, return_all_scores=True)
    
    # Handle nested list format [[{...}, {...}]]
    if isinstance(results[0], list):
        results = results[0]
    
    analyzed = []
    for result in results:
        label = result["label"].lower()
        analyzed.append({
            "label": LABEL_MAP.get(label, result["label"]),
            "confidence": round(result["score"] * 100, 2)
        })

    analyzed.sort(key=lambda x: x["confidence"], reverse=True)
    return analyzed