What is Polarity in Sentiment Analysis?
When we use TextBlob(text).sentiment.polarity, it returns a score between:

-1.0 → very negative

0.0 → neutral

+1.0 → very positive



| Range         | Meaning             | Why this range?                              |
| ------------- | ------------------- | -------------------------------------------- |
| `> 0.3`       | Clearly positive    | Keeps out weak/flimsy positivity like “okay” |
| `< -0.1`      | Clearly negative    | Avoids overreacting to mild disappointment   |
| `-0.1 to 0.3` | Neutral / uncertain | Covers vague, meh, in-between responses      |
