import pandas as pd
import numpy as np
import nltk
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report

# Download NLTK data (Run once)
nltk.download('stopwords')

# Load dataset (Replace with actual file)
df = pd.read_csv("customer_reviews.csv")

# Display first few rows
print(df.head())

# Data Preprocessing
def preprocess_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'\W', ' ', text)  # Remove special characters
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    text = ' '.join(word for word in text.split() if word not in stopwords.words('english'))  # Remove stopwords
    return text

df['cleaned_review'] = df['review_text'].apply(preprocess_text)

# Convert sentiment labels to numeric (Modify based on dataset)
df['sentiment'] = df['sentiment'].map({'positive': 1, 'neutral': 0, 'negative': -1})

# Split Data
X_train, X_test, y_train, y_test = train_test_split(df['cleaned_review'], df['sentiment'], test_size=0.2, random_state=42)

# Create NLP Model Pipeline
model = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('classifier', MultinomialNB())
])

# Train Model
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Accuracy & Report
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Word Cloud Visualization
positive_words = ' '.join(df[df['sentiment'] == 1]['cleaned_review'])
negative_words = ' '.join(df[df['sentiment'] == -1]['cleaned_review'])

plt.figure(figsize=(12,6))

plt.subplot(1,2,1)
plt.title("Positive Reviews Word Cloud")
plt.imshow(WordCloud(width=400, height=200, background_color='white').generate(positive_words))
plt.axis('off')

plt.subplot(1,2,2)
plt.title("Negative Reviews Word Cloud")
plt.imshow(WordCloud(width=400, height=200, background_color='black').generate(negative_words))
plt.axis('off')

plt.show()
