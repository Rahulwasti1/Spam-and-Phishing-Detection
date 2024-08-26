**📧 Spam Email & Phishing URL Detection 🔗
A comprehensive machine learning solution to detect spam emails and phishing URLs.**

1. 🛠️ Import Libraries  
Spam Detection: Imported pandas, numpy, sklearn.  
Phishing Checker: Added plotly, nltk for visualization and tokenization.

2. 📂 Import Datasets  
Spam Detection: Loaded mail_data.csv with email content and labels.  
Phishing Checker: Imported phishing_site_urls.csv with labeled URLs.

3. 🧹 Data Pre-processing  
Spam Detection: Handled missing values, removed duplicates, and encoded labels (Spam = 1, Ham = 0).  
Phishing Checker: Cleaned missing/duplicate data.

4. 🔍 Tokenization & Stemming  
Phishing Checker: Tokenized URLs and applied stemming using nltk to normalize URL words.  

5. 🧠 Feature Extraction  
Applied TF-IDF and OHE to conveert text to numeric feature for both.  

6. 🔀 Train-Test Split  
Both datasets were split into 80% training and 20% testing.  

7. 🤖 Model Training  
Spam Detection: Trained with Logistic Regression, Support Vector Machine and Decision Tree Classifier.  
Phishing Checker: Used Random Forest and Logistic Regression to classify URLs.

8. 📊 Model Evaluation  
Spam: Achieved 97% highest accuracy.  
Phishing: Achieved 95% highest accuracy.

9. 🔮 Prediction  
Spam: Predicted whether new emails are spam or not.  
Phishing: Predicted if URLs are phishing or legitimate.

10. 🌐 Streamlit App  
Integrated both models into a user-friendly Streamlit web app for real-time email and URL detection.  

💡 Conclusion  
This project offers a dual protection mechanism against spam and phishing, making the internet safer! 🚀

Demonstration:  

<img width="468" alt="image" src="https://github.com/user-attachments/assets/873474ab-f9a6-4792-8d44-b644bbfbf5fd">
