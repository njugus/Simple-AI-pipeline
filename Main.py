# define the blocks
# fetch the news

import re


def fetch_headline() -> str:
    return "   BREAKING: AI cures cancer! (but costs $1M)   "


# clean the headline
def clean_headline(text: str) -> str:
    return text.strip().lower()


# extract $1m from the string using regex
def extract_value(text: str) -> str:
    # Pattern to match $ followed by digits and optional M/m/K/k/B/b
    pattern = r'\$\d+\.?\d*[MKmkbB]?'  # Handles $1M, $1.5B, $100k, etc.
    match = re.search(pattern, text)
    return match.group() if match else None


# analyze the sentiments from the headline
def analyze_sentiments(text: str) -> str:
    if "cures" in text:
        return "positive"
    return "negative"


# summarize the headline( headline + sentiment)
def summarize_headline(text: str, sentiment_value: str, key_value: str) -> str:
    return f"Headline : {text} sentiment : {sentiment_value}  key_value : {key_value}"


# run the pipeline
# the blocks here run in order
headline = fetch_headline()
cleaned_headline = clean_headline(headline)
extracted_value = extract_value(cleaned_headline)
sentiment = analyze_sentiments(cleaned_headline)
summary = summarize_headline(cleaned_headline, sentiment, extracted_value)

print(summary)
