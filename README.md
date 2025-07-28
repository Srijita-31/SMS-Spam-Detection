
# 📩 SMS Spam Detection Web App

A simple web application that classifies text messages (SMS) as **Spam** or **Not Spam** using Natural Language Processing and Machine Learning.

🔗 **Live Demo:** [https://sms-spam-detection-v6qq.onrender.com/](https://sms-spam-detection-v6qq.onrender.com/)

---

##  Introduction

This project is a Streamlit-based SMS Spam Detection System that leverages the power of NLP and Machine Learning to predict whether a given message is spam or not.  
It uses the **TF-IDF vectorization** technique to convert messages into numerical features and a trained classification model to determine the output.

---

## 🛠 Technologies Used

| Category             | Tools / Libraries                           |
|----------------------|----------------------------------------------|
| Programming Language | Python                                       |
| Web Framework        | Streamlit                                    |
| NLP                  | NLTK, Scikit-learn (TF-IDF Vectorizer)       |
| ML Model             | Trained classification model (pickle)        |
| Visualization        | Streamlit                                    |
| Deployment           | Render                                        |

---

##  Features

-  Classifies SMS messages into **Spam** or **Not Spam**
-  Simple and intuitive **Streamlit UI**
-  Lightweight and fast – works in real-time
-  Deployed and accessible online via Render
-  Clean and minimal design

---

##  Screenshots

### ✅ Not Spam Message Output  
[![Not Spam](not%20spam%20message.png)](not%20spam%20message.png)

### 🚫 Spam Message Output  
[![Spam](spam%20message.png)](spam%20message.png)



##  How to Run Locally

```bash
# Clone the repository
git clone https://github.com/Srijita-31/SMS-Spam-Detection.git
cd SMS-Spam-Detection

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
