from transformers import pipeline

# Load pretrained fake news classifier
classifier = pipeline("text-classification", model="distilbert-base-uncased")

def analyze_text(text):
    result = classifier(text)[0]

    label = result["label"]
    score = round(result["score"] * 100, 2)

    return {
        "label": label,
        "confidence": score
    }
