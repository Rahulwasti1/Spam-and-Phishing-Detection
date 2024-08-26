**📧 Spam Email and Phishing URL Detection 🔗**

A Comprehensive Guide to Detecting Spam Emails and Phishing URLs

1. 🛠️ Importing Libraries
Spam Email Detection:
Essential libraries like pandas, numpy, and sklearn were imported for data manipulation, modeling, and evaluation.
Phishing URL Checker:
Similar libraries were imported alongside plotly and nltk for visualization and natural language processing.

2. 📂 Importing Datasets
Spam Email Detection:
The dataset mail_data.csv containing labeled emails (spam or not) was loaded using pandas.
Phishing URL Checker:
The dataset phishing_site_urls.csv, containing URLs marked as either phishing or legitimate, was imported.

3. 🧹 Data Pre-processing
Spam Email Detection:
✅ Checking for null values: Missing data was handled.
❌ Removing duplicates: Duplicate entries were removed for cleaner data.
🔢 Encoding labels: Email categories (Spam/Ham) were encoded into binary values (0 = Ham, 1 = Spam).
Phishing URL Checker:
✅ Checking for missing values: The dataset was checked for null or missing entries.
❌ Duplicate removal: Any duplicate URLs were removed.

4. 🔍 Tokenization and Stemming
Phishing URL Checker:
📝 Tokenization: URLs were split into individual components for analysis.
🌱 Stemming: Words were reduced to their root form using nltk to capture essential meaning without variations.

5. 🧠 Feature Extraction
Spam Email Detection:
💬 Text processing: Email text was processed using TF-IDF (Term Frequency - Inverse Document Frequency) to convert raw email text into numeric features.
Phishing URL Checker:
🔠 One-hot encoding: Categorical features (tokens from URLs) were converted into binary vectors for modeling.

6. 🔀 Train-Test Split
Both:
📊 Data Splitting: The datasets were split into training (80%) and testing (20%) sets to evaluate model performance.

7. 🤖 Model Training
Spam Email Detection:
🚀 Logistic Regression: A Logistic Regression model was used to classify emails as either spam or not.
🧪 Other algorithms: Various other algorithms like Naive Bayes and Random Forest were tested for comparison.
Phishing URL Checker:
🤖 Random Forest: A Random Forest model was trained to classify URLs as phishing or legitimate.

8. 📊 Model Evaluation
Spam Email Detection:
📈 Accuracy Score: The spam classifier achieved an accuracy of 95% on the test data.
🎯 Precision and Recall: High precision and recall scores indicated the model's robustness in classifying spam.
Phishing URL Checker:
📊 Accuracy Score: The phishing URL model achieved an accuracy of 97% on the test set.

9. 🔮 Prediction
Both:
📧 Spam Prediction: The trained model was used to predict whether new emails are spam or not.
🔗 Phishing Prediction: The model was used to predict whether new URLs are phishing or legitimate.

10. 🌐 Web Application
🎨 Streamlit Web App: A user-friendly Streamlit web app was developed, combining both functionalities to detect spam emails and phishing URLs.

💡 Conclusion
The combined model offers a reliable solution to detect both spam emails and phishing URLs using machine learning, helping protect users from malicious attacks. 🚀
