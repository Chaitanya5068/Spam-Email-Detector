## 📧 SPAM MAIL DETECTOR
A Deep Learning–Powered Real-Time Email Classifier

Detect and block unwanted messages instantly with high accuracy using a transformer-based NLP model.
Built with Hugging Face's DistilBERT and Flask, this app intelligently identifies phishing, promotional, and spam emails to keep your inbox clean and secure.

## 🎯 Purpose

The SPAM MAIL DETECTOR is a machine learning-powered web application designed to identify whether a given email message is SPAM or NOT SPAM. 
It leverages state-of-the-art transformer models (DistilBERT) to achieve high accuracy in real-time email spam detection.

## 🧠 Core Features

- 🚀 Uses Hugging Face's pretrained transformer model (DistilBERT)
- 📈 Highly accurate text classification (95%+ accuracy)
- 🧠 NLP-powered semantic understanding of spam content
- 🌐 Intuitive web interface with color-coded results
- 📩 Real-time email input analysis
- 📊 Confidence score display for each prediction

## ⚙️ Technologies Used

- 🐍 Python 3.9+
- 🔥 Hugging Face transformers (DistilBERT)
- 🧠 PyTorch
- 🌐 Flask
- 🎨 HTML/CSS (with gradient UI)
- 🐼 Pandas
- ⚙️ Scikit-learn (optional)

## 📁 Folder Structure

SPAM MAIL DETECTOR/

├── app.py                   # Flask app main file

├── model_utils.py           # Loads transformer model and predicts

├── requirements.txt         # Python dependencies

├── templates/

│   └── index.html           # UI template for input and result


## 📦 requirements.txt

flask

transformers

torch

pandas

scikit-learn

## ⚙️ How It Works

1. Loads a pretrained spam detection model (mrm8488/bert-tiny-finetuned-sms-spam-detection).
2. User submits an email/message via a web form.
3. The message is passed to the model for classification.
4. Model returns:
   - spam or ham
   - Confidence score
5. Flask renders the result with appropriate color.

## 💬 Sample Questions / Inputs

Try these test messages:

Message: "Win a brand-new iPhone 15 now!" → 🚫 SPAM

Message: "Meeting with team at 3 PM today" → ✅ NOT SPAM

Message: "Update your KYC now to avoid deactivation" → 🚫 SPAM

Message: "Assignment deadline extended to tomorrow" → ✅ NOT SPAM

## 📦 Installation & Run Instructions

1. Clone the repo:
   git clone https://github.com/your-username/spam-mail-detector.git
   cd spam-mail-detector

2. Install dependencies:
   pip install -r requirements.txt

3. Run the Flask app:
   python app.py

Then open your browser and go to: http://127.0.0.1:5000

## 📄 Sample Output

📧 Message:
"Your PAN card will be blocked. Click here to verify."

✅ Prediction:
🚫 SPAM

🔍 Confidence:
98.3%

## 📜 License

This project is licensed under the MIT License — you are free to use, modify, and distribute it with proper credit.

## 👨‍💻 Developed By

Chaitanya Bhosale

🔗 GitHub: https://github.com/Chaitanya5068

🔗 LinkedIn: www.linkedin.com/in/chaitanya-bhosale

## 🔗 Related Projects

-AARAMBHA CHATBOT

  GITHUB: https://github.com/Chaitanya5068/python_chatbot

-AUTO REPORT GENERATOR 

  GITHUB: https://github.com/Chaitanya5068/Auto_report

-WEATHER API

   GITHUB: https://github.com/Chaitanya5068/Python-Weather-Api


