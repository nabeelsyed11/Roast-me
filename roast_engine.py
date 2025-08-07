import random
from textblob import TextBlob
from roast_bank import positive_roasts, neutral_roasts, negative_roasts

def detect_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.3:
        return "positive"
    elif polarity < -0.1:
        return "negative"
    else:
        return "neutral"

def smart_sentiment_roast(user_input, override_sentiment=None):
    """
    Returns a single roast based on sentiment or emoji mood slider.
    :param user_input: User input string
    :param override_sentiment: float (-1.0 to 1.0) or string override
    :return: Single roast string
    """
    # Strip and check input
    user_input = user_input.strip()
    if not user_input:
        return "No roast for silence, sweetie. Say something spicy! 🌶️"

    # Handle override from mood slider
    if isinstance(override_sentiment, float):
        if override_sentiment > 0.3:
            sentiment = "positive"
        elif override_sentiment < -0.1:
            sentiment = "negative"
        else:
            sentiment = "neutral"
    else:
        sentiment = detect_sentiment(user_input)

    # Select roast list based on sentiment
    if sentiment == "positive":
        roast_list = positive_roasts
    elif sentiment == "negative":
        roast_list = negative_roasts
    else:
        roast_list = neutral_roasts

    # Choose one single roast
    roast = random.choice(roast_list)
    return roast
