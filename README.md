# 🛡️ Cyberbullying Detection using Machine Learning

## 🚀 Project Overview

Cyberbullying is a serious issue on social media platforms. This project aims to automatically detect cyberbullying content in tweets using Machine Learning and Natural Language Processing (NLP) techniques.

The system classifies user input text into different categories such as:

* ✅ Not Cyberbullying
* ⚠️ Offensive Language
* 🚫 Hate Speech

It also provides a real-time web interface built using Streamlit for interactive predictions.

---

## 🎯 Objectives

* Detect harmful and abusive content in text
* Classify tweets into meaningful categories
* Build a real-time prediction system
* Understand NLP and Machine Learning workflows

---

## 🧠 Technologies Used

* Python
* Scikit-learn
* Pandas, NumPy
* Natural Language Processing (NLP)
* TF-IDF Vectorization
* Streamlit (for web app)
* Power BI (for dashboard visualization)

---

## ⚙️ Features

✔ Real-time tweet classification
✔ Clean and interactive UI
✔ Machine Learning model trained on dataset
✔ Data visualization using Power BI
✔ Easy to run locally

---

## 📂 Project Structure

```
Cyberbullying-Detection-ML/
├── app.py                      # Streamlit web app
├── README.md                   # Project documentation
├── requirements.txt            # Dependencies
├── cyberbullying_tweets.csv    # Dataset
├── Cyber_Bullying.pbix         # Power BI dashboard
├── Cyberbullying_MLModel.ipynb
├── Cyberbullying_Detection_Final.ipynb
```


---

## 📊 Model Details

* Algorithm Used: Random Forest Classifier
* Feature Extraction: TF-IDF Vectorizer
* Task: Multi-class text classification
* Dataset: Cyberbullying tweets dataset

---

## 📦 Model File (Important)

⚠️ The trained model file is not uploaded due to GitHub size limitations.

👉 Download the model from Google Drive:
[(🔗 cyberbullying_model.pkl)](https://drive.google.com/file/d/1gbEMlzPz5-xauUq0FG5gt3m5-PqchVBn/view?usp=drive_link)

After downloading, place it in the root folder:

```
CyberBulling Detection/
├── app.py
├── cyberbullying_model.pkl
```

---

## 🖥️ How to Run Locally

### 1️⃣ Clone Repository

```
git clone https://github.com/vansh2711/cyberbullying-detection-ml.git
cd cyberbullying-detection-ml
```

### 2️⃣ Install Dependencies

```
pip install streamlit pandas scikit-learn numpy
```

### 3️⃣ Run Application

```
streamlit run app.py
```

---

## 📸 Output

* **Input:** Tweet text

* **Output Categories:**

  * `not_cyberbullying` → Safe content ✅
  * `religion` → Religion-based bullying ⚠️
  * `age` → Age-related bullying ⚠️
  * `ethnicity` → Ethnicity-based bullying ⚠️
  * `gender` → Gender-based bullying ⚠️
  * `other_cyberbullying` → Other forms of bullying ⚠️


---

## 📈 Future Improvements

* Use Deep Learning models (LSTM, BERT)
* Add multi-language support
* Deploy on cloud platforms
* Build REST API

---

## 👨‍💻 Author

**Vansh Patel**
🎓 Final Year Student | Machine Learning Enthusiast

---

## ⭐ Support

If you like this project, please give it a ⭐ on GitHub!
