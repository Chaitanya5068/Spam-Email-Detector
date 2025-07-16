from flask import Flask, request, render_template
import pandas as pd
import os
import urllib.request
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

app = Flask(__name__)

# 📥 Download dataset if not present
DATA_URL = "https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv"
LOCAL_FILE = "spam.tsv"

if not os.path.exists(LOCAL_FILE):
    print("📥 Downloading dataset...")
    urllib.request.urlretrieve(DATA_URL, LOCAL_FILE)
    print("✅ Dataset downloaded.")

# ✅ Load and clean dataset
df = pd.read_csv(LOCAL_FILE, sep='\t', header=None, names=['label', 'text'])
df.dropna(inplace=True)
df['label'] = df['label'].map({'ham': 0, 'spam': 1})
df = df[df['label'].isin([0, 1])]

# ✅ Shuffle and split data
df = df.sample(frac=1, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.25, random_state=42)

# ✅ TF-IDF Vectorization
vectorizer = TfidfVectorizer(stop_words='english', max_df=0.9)
X_train_tf = vectorizer.fit_transform(X_train)
X_test_tf = vectorizer.transform(X_test)

# ✅ Train model
model = MultinomialNB()
model.fit(X_train_tf, y_train)

# ✅ Accuracy check (optional for dev)
print("Training accuracy:", model.score(X_train_tf, y_train))
print("Testing accuracy:", model.score(X_test_tf, y_test))


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    is_spam = None
    if request.method == 'POST':
        message = request.form.get('message', '')
        if message.strip():
            msg_tf = vectorizer.transform([message])
            prediction = model.predict(msg_tf)[0]
            is_spam = prediction == 1
            result = "🚫 SPAM" if is_spam else "✅ NOT SPAM"
    return render_template('index.html', result=result, is_spam=is_spam)


if __name__ == '__main__':
    print("✅ Flask app running at http://127.0.0.1:5000")
    app.run(debug=True)
