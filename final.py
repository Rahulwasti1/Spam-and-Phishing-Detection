import streamlit as st
import re
import pickle

# Loading the vectorizers and classifiers
with open("feature_extraction_spam.pkl", 'rb') as file: 
    spam_tfidf_vectorizer = pickle.load(file)

with open("svm_spam.pkl", 'rb') as file:
    spam_classifier = pickle.load(file)

with open("tfidf_vectorize_phishing.pkl", 'rb') as file: 
    phishing_tfidf_vectorizer = pickle.load(file)

with open("lr_classifier_phishing.pkl", 'rb') as file:
    phishing_classifier = pickle.load(file)

# Suspicious TLDs often associated with phishing domains
SUSPICIOUS_TLDS = ['.xyz', '.club', '.top', '.work', '.info', '.servebbs.org', '.biz', '.tk', '.ml', '.ga', '.cf']

# Suspicious keywords often found in phishing URLs
SUSPICIOUS_KEYWORDS = [
    "login", "verify", "secure", "account", "update", "password", "bank", "paypal", 
    "signin", "billing", "support", "service", "confirm", "identity", "credit"
]

# Function to extract URLs
def extract_url(text):
    url_pattern = re.compile(r'http[s]?://\S+|www\.\S+')
    return re.findall(url_pattern, text)

# Function to check if a URL uses a suspicious TLD
def is_suspicious_tld(url):
    for tld in SUSPICIOUS_TLDS:
        if url.endswith(tld):
            return True
    return False

# Function to check if a URL contains suspicious keywords
def contains_suspicious_keywords(url):
    return any(keyword in url.lower() for keyword in SUSPICIOUS_KEYWORDS)

# Function to check for multiple subdomains (common in phishing URLs)
def has_multiple_subdomains(url):
    domain = url.split('/')[2]  # Extract domain from URL
    return domain.count('.') > 2  # More than two dots in domain

# Function to check for IP-based URLs (commonly used in phishing)
def is_ip_url(urls):
    ip_pattern = re.compile(r'http[s]?://(?:\d{1,3}\.){3}\d{1,3}(?:\:\d+)?(?:/\S*)?')
    return any(re.match(ip_pattern, url) for url in urls)

# Function to detect phishing URLs based on multiple heuristics
def detect_phishing_url(url):
    return is_suspicious_tld(url) or contains_suspicious_keywords(url) or has_multiple_subdomains(url)

# To detect phishing words in text
def contains_suspicious_words(text):
    phishing_words = [
        "click here", "credit", "prize", "urgent", "account", "verify", "free", 
        "limited time", "login", "password", "update", "security", "confirm", 
        "offer", "congratulations", "lottery", "bank", "important", "immediately", 
        "risk", "billing", "invoice", "pay now", "action required", "claim", 
        "unsubscribe", "dear customer", "suspended", "verify your identity", 
        "security alert", "failure", "access", "login now", "win", "problem with your", 
        "unauthorized", "help desk", "support", "reset", "unlock", "deactivation", 
        "problem", "solution required", "limited offer", "act fast", "contest", 
        "redeem", "alert", "notify", "your information", "expired", "friend request",
        "earn", "refund", "cancel", "download", "funds", "identity", "threat"
    ]
    return any(word in text.lower() for word in phishing_words)

# Title and subtitle
st.title("Email Spam and Phishing Classification App")
st.subheader("Built with Streamlit & Python")

# Text input field
user_input = st.text_area("Enter the email text")

# Prediction logic
if st.button("Predict"):
    if user_input.strip() == "":
        st.info("Please enter text to predict.")
    else:
        # Transform the user input for Spam Detection
        spam_features = spam_tfidf_vectorizer.transform([user_input])
        spam_prediction = spam_classifier.predict(spam_features)
        
        # Transform the user input for Phishing Detection
        phishing_features = phishing_tfidf_vectorizer.transform([user_input])
        phishing_prediction = phishing_classifier.predict(phishing_features)
        
        # Check for URLs in the input text
        urls = extract_url(user_input)
        ip_url_detected = is_ip_url(urls)
        suspicious_urls = [url for url in urls if detect_phishing_url(url)]
        
        # Flag for phishing and spam
        contains_phishing = False
        contains_spam = False
        
        # Determine if the text contains phishing content
        if phishing_prediction[0] == 0 or contains_suspicious_words(user_input) or ip_url_detected or suspicious_urls:
            contains_phishing = True

        # Determine if the text is spam
        if spam_prediction[0] == 0:
            contains_spam = True

        # Handle different scenarios
        if contains_spam and contains_phishing:
            st.error("This email contains both spam text and phishing content (including suspicious URLs).")
        elif contains_spam:
            st.error("This email is classified as spam.")
        elif contains_phishing:
            if urls:
                st.warning(f"Found URLs: {urls}")
            if ip_url_detected:
                st.error("Warning: The email contains a URL with an IP address, which is commonly associated with phishing.")
            if suspicious_urls:
                st.error("Suspicious phishing URLs detected:")
                for url in suspicious_urls:
                    st.markdown(f"- [Phishing Link]({url})")
            st.error("This email contains phishing content.")
        else:
            st.success("This email does not contain spam or phishing content.")
