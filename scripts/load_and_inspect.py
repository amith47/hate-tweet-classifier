import pandas as pd
import os

# Load dataset
data_path = os.path.join('data', 'train_E6oV3lV.csv')
df = pd.read_csv(data_path)

# Data cleaning function
import re
def clean_tweet(text):
    text = text.lower()
    text = re.sub(r'http\S+|www\S+', '', text)  # Remove URLs
    text = re.sub(r'@\w+', '', text)  # Remove mentions
    text = re.sub(r'#', '', text)  # Remove hashtag symbol
    text = re.sub(r'[^a-z\s]', '', text)  # Remove special characters and numbers
    text = re.sub(r'\s+', ' ', text).strip()  # Remove extra spaces
    return text

# Show before/after cleaning for first 5 tweets
print('Before cleaning:')
print(df['tweet'].head())
df['clean_tweet'] = df['tweet'].apply(clean_tweet)
print('\nAfter cleaning:')
print(df['clean_tweet'].head())

# Show class distribution

print('\nClass distribution:')
print(df['label'].value_counts())

# --- Classification using Bag-of-Words and Logistic Regression ---
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

# Features and labels
X = df['clean_tweet']
y = df['label']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Bag-of-Words vectorization
vectorizer = CountVectorizer()
X_train_bow = vectorizer.fit_transform(X_train)
X_test_bow = vectorizer.transform(X_test)

# Train classifier
clf = LogisticRegression(max_iter=200)
clf.fit(X_train_bow, y_train)

# Predict
y_pred = clf.predict(X_test_bow)

# Results
print('\nClassification Report (Bag-of-Words + Logistic Regression):')
print(classification_report(y_test, y_pred, target_names=['Harmless','Hate']))
print('Accuracy:', accuracy_score(y_test, y_pred))
