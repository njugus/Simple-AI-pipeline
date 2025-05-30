# define the blocks
# fetch the news
def fetch_headline() -> str:
    return "   BREAKING: AI cures cancer! (but costs $1M)   "


# clean the headline e.g by removing spaces
def clean_headline(headline: str) -> str:
    return headline.strip().lower()


# analyze the sentiments from the headline
def analyze_sentiments(headline: str) -> str:
    if "cures" in headline:
        return "positive"
    return "negative"


# summarize the headline( headline + sentiment)
def summarize_headline(headline: str, sentiment: str) -> str:
    return f"Headline : {headline} sentiment : {sentiment}"


# run the pipeline
# the blocks here run in order
headline = fetch_headline()
cleaned_headline = clean_headline(headline)
sentiment = analyze_sentiments(cleaned_headline)
summary = summarize_headline(cleaned_headline, sentiment)

print(summary)

