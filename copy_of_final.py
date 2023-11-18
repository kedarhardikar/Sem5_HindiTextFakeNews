# -*- coding: utf-8 -*-
"""Copy of final.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pgpZFzX2cIRWSpDkzPX7we8ClY8Vi_5W
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

from google.colab import drive
drive.mount('/content/drive')

!pip3 install pandas_ods_reader -q
from pandas_ods_reader import read_ods

import nltk
import re
nltk.download('punkt')

import pandas as pd
!pip3 install pandas_ods_reader -q
from pandas_ods_reader import read_ods

# data_sentiment = read_ods('/content/hi_3500.ods',1,headers = False)
# data_sentiment.columns = ['text','sentiment']
# data_sentiment.head()

data_sentiment = read_ods('/content/drive/MyDrive/NLP Project/Sentiment data/hi_3500.ods',1,headers = False)
data_sentiment.columns = ['text','sentiment']

data_sentiment.head()

data_sentiment.dropna()
# data_sentiment_test.dropna()

# Define a function to remove English words, numeric characters, and specific special characters
def clean_hindi_text(text):
    words = nltk.word_tokenize(text)
    cleaned_words = []
    for word in words:
        if not re.match("^[A-Za-z]*$", word) and not bool(re.search(r'[0-9०-९]', word)):
            # Specify special characters to remove (e.g., @, ., ,, #, &)
            word = re.sub(r'[.,@#&:)(]', '', word)
            cleaned_words.append(word)
    return ' '.join(cleaned_words)

data_sentiment['text'] = data_sentiment['text'].apply(clean_hindi_text)
# data_sentiment_test['text'] = data_sentiment_test['text'].apply(clean_hindi_text)
data_sentiment

X = data_sentiment['text']
y = data_sentiment['sentiment']

X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.33, random_state=42)

# # Split the dataset into training and testing sets
# X_train = data_sentiment_train['text']  # Your Hindi text data
# X_test = data_sentiment_test['text']
# y_train = data_sentiment_train['sentiment']  # Sentiment labels (e.g., positive, negative)
# y_test = data_sentiment_test['sentiment']

# Create TF-IDF vectors from the text data
tfidf_vectorizer = TfidfVectorizer(ngram_range=(1, 2))
X_train_tfidf = tfidf_vectorizer.fit_transform(X_train)
X_test_tfidf = tfidf_vectorizer.transform(X_test)

from sklearn.svm import SVC

# Initialize and train a Support Vector Machine classifier for multiclass classification
svm_classifier = SVC(kernel='linear', decision_function_shape='ovr', random_state=42)
svm_classifier.fit(X_train_tfidf, y_train)

# Predict sentiment on the test data
y_pred_svm = svm_classifier.predict(X_test_tfidf)

# Evaluate the SVM model
accuracy_svm = accuracy_score(y_test, y_pred_svm)
classification_rep_svm = classification_report(y_test, y_pred_svm)

# Print evaluation metrics for SVM
print("Support Vector Machine (SVM) Classifier:")
print(f"Accuracy: {accuracy_svm:.2f}")
print(classification_rep_svm)

# # Initialize and train a Random Forest classifier
# rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
# rf_classifier.fit(X_train_tfidf, y_train)
# # Predict sentiment on the test data
# y_pred = rf_classifier.predict(X_test_tfidf)

# # Evaluate the model
# accuracy = accuracy_score(y_test, y_pred)
# classification_rep = classification_report(y_test, y_pred)

# # Print evaluation metrics
# print(f"Accuracy: {accuracy:.2f}")
# print(classification_rep)

# from sklearn.ensemble import GradientBoostingClassifier

# # Initialize and train a Gradient Boosting classifier
# gb_classifier = GradientBoostingClassifier(n_estimators=100, random_state=42)
# gb_classifier.fit(X_train_tfidf, y_train)

# # Predict sentiment on the test data
# y_pred_gb = gb_classifier.predict(X_test_tfidf)

# # Evaluate the Gradient Boosting model
# accuracy_gb = accuracy_score(y_test, y_pred_gb)
# classification_rep_gb = classification_report(y_test, y_pred_gb)

# # Print evaluation metrics for Gradient Boosting
# print("Gradient Boosting Classifier:")
# print(f"Accuracy: {accuracy_gb:.2f}")
# print(classification_rep_gb)

# from sklearn.naive_bayes import MultinomialNB

# # Initialize and train a Multinomial Naive Bayes classifier
# nb_classifier = MultinomialNB()
# nb_classifier.fit(X_train_tfidf, y_train)

# # Predict sentiment on the test data
# y_pred_nb = nb_classifier.predict(X_test_tfidf)

# # Evaluate the Naive Bayes model
# accuracy_nb = accuracy_score(y_test, y_pred_nb)
# classification_rep_nb = classification_report(y_test, y_pred_nb)

# # Print evaluation metrics for Naive Bayes
# print("Multinomial Naive Bayes Classifier:")
# print(f"Accuracy: {accuracy_nb:.2f}")
# print(classification_rep_nb)



"""*italicized text*# SVC on Fake news data for sentiment"""

# train = pd.read_csv('/content/train (5).csv',encoding='utf-8-sig')
# test = pd.read_csv('/content/test (2).csv',encoding='utf-8-sig')

train = pd.read_csv('/content/drive/MyDrive/NLP Project/Data/train.csv',encoding='utf-8-sig')
test = pd.read_csv('/content/drive/MyDrive/NLP Project/Data/test.csv',encoding='utf-8-sig')

train.drop(['Unnamed: 0','author','id'], inplace = True, axis = 1)
test.drop(['Unnamed: 0','author','id'], inplace = True, axis = 1)

train = train.dropna()
test = test.dropna()

hindi_stopwords = [
    'अपना', 'अपनी', 'अपने', 'अभी', 'आदि', 'इस', 'इसके', 'इसको', 'इसमें', 'इससे',
    'उनका', 'उनकी', 'उनके', 'उनको', 'उनका', 'उनकी', 'उनके', 'उनको', 'उन्हें', 'उसका',
    'उसकी', 'उसके', 'उसको', 'उसमें', 'उसने', 'उसी', 'उसे', 'उसका', 'करता', 'करते',
    'करना', 'करने', 'करें', 'कहते', 'कहा', 'का', 'कारण', 'किसी', 'की', 'कुछ', 'के',
    'को', 'कोई', 'कौन', 'कौनसा', 'गया', 'घर', 'जब', 'जहाँ', 'जा', 'जितना', 'जिन',
    'जिन्होंने', 'जिन्हों', 'जिस', 'जिसे', 'जी', 'जिसके', 'जिसको', 'जिसमें', 'जिसे', 'तक',
    'तब', 'तरह', 'तिन', 'तिन्हें', 'तिन्हों', 'तिस', 'तिसे', 'था', 'थे', 'दिया', 'दूसरे',
    'दो', 'द्वारा', 'ने', 'पर', 'पहले', 'पूरा', 'पूरी', 'फिर', 'बनी', 'बहुत', 'बाद',
    'बाला', 'भी', 'मगर', 'मानो', 'मैं', 'मैंने', 'में', 'यदि', 'यह', 'यहाँ', 'यही',
    'या', 'यिह', 'ये', 'रखें', 'रहा', 'रहे', 'लिए', 'लिया', 'लेकिन', 'व', 'वगेरह', 'वर्ग',
    'वह', 'वहाँ', 'वही', 'वाले', 'वाली', 'वाला', 'वाले', 'वाली', 'वाला', 'वाले', 'वाली',
    'वाला', 'सबसे', 'सबसे', 'सकता', 'सकते', 'सकती', 'सकती', 'सब', 'सबसे', 'से', 'ही',
    'है', 'हैं', 'हुआ', 'हुई', 'हुए', 'हो', 'होता', 'होते', 'होती', 'होती', 'होते', 'होते',
    'होती', 'होती', 'होती', 'होना', 'होने', 'अंदर', 'अदि', 'अन्य', 'अप', 'अफ', 'अल', 'अलब',
    'अव', 'अवश्य', 'अस', 'आदि', 'आप', 'आपका', 'आपकी', 'आपके', 'आपने', 'आपने', 'आदि', 'आना',
    'इंहोंने', 'इंहें', 'इंहों', 'इतना', 'इतनी', 'इतने', 'इन', 'इनका', 'इनकी', 'इनके', 'इन्ही',
    'इन्होंने', 'इन्हें', 'इन्हों', 'इस', 'इसका', 'इसकी', 'इसके', 'इसी', 'उंहोंने', 'उंहें',
    'उंहों', 'उपर', 'उसके', 'उससे', 'उसी', 'उसे', 'उसी', 'उसे', 'कर', 'करत', 'करता', 'करती',
    'करते', 'करन', 'करना', 'करने', 'किया', 'किये', 'किये', 'किया', 'कुछ', 'कुल', 'के', 'को', 'को'
]

from nltk.corpus import stopwords
import nltk
nltk.download("indian")

nltk.download("stopwords")
def remove_hindi_stopwords(text):
    words = nltk.word_tokenize(text)
    cleaned_words = []
    for word in words:
        # Remove specific words
        if word.lower() not in hindi_stopwords:
            # Remove English words and special characters
            if not re.match("^[A-Za-z]*$", word) and not bool(re.search(r'[0-9०-९]', word)):
                # Specify special characters to remove (e.g., @, ., ,, #, &)
                word = re.sub(r'[.,@#&]', '', word)
                cleaned_words.append(word)
    return ' '.join(cleaned_words)

train['text'] = train['text'].apply(remove_hindi_stopwords)
test['text'] = test['text'].apply(remove_hindi_stopwords)

# Create TF-IDF vectors from the text data
#tfidf_vectorizer = TfidfVectorizer(max_features=10000, ngram_range=(1, 2))
train_tfidf = tfidf_vectorizer.transform(train['text'])
test_tfidf = tfidf_vectorizer.transform(test['text'])

sentim_train = svm_classifier.predict(train_tfidf)
sentim_test = svm_classifier.predict(test_tfidf)

train['sentiment'] = sentim_train
test['sentiment'] = sentim_test

train['sentiment'].value_counts()

sentiment_mapping = {"negative": -1, "neutral": 0, "positive": 1}
train['sentiment'] = train['sentiment'].map(sentiment_mapping)
test['sentiment'] = test['sentiment'].map(sentiment_mapping)

row_with_sentiment_zero = train.loc[train['sentiment'] == 0].iloc[2]
row_with_sentiment_zero.text

"""Fake news detection"""

#train.head()

from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.preprocessing import StandardScaler

class ItemSelector(BaseEstimator, TransformerMixin):
    def __init__(self, key):
        self.key = key

    def fit(self, x, y=None):
        return self

    def transform(self, data_dict):
        return data_dict[self.key]

from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.ensemble import RandomForestClassifier
pipeline_rfc = Pipeline([
    # ('selector', ItemSelector(key='text')),
    ('cv', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('classifier', RandomForestClassifier())
])

from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.svm import SVC

pipeline_svc = Pipeline([
    # ('selector', ItemSelector(key='text')),
    ('cv', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('classifier', SVC())
])

# Split the dataset into training and testing sets
X = train['text']
y_sentiment = train['sentiment']
y_authenticity = train['label']

X_train, X_test, y_sentiment_train, y_sentiment_test, y_authenticity_train, y_authenticity_test = train_test_split(
    X, y_sentiment, y_authenticity, test_size=0.2, random_state=42
)

y_sentiment_test

svc_sentiment_test

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

pipeline_rfc_sent.fit(X_train, y_sentiment_train)
rfc_sentiment_train = pipeline_rfc_sent.predict(X_train)

rfc_sentiment_test = pipeline_rfc_sent.predict(X_test)

print(f"Accuracy for sentiments with RFC training:{accuracy_score(y_sentiment_train, rfc_sentiment_train)}")
print(f"Accuracy for sentiments with RFC test:{accuracy_score(y_sentiment_test, rfc_sentiment_test)}\n")

print(f"Classification rep for sentiments with RFC training\n:{classification_report(y_sentiment_train, rfc_sentiment_train)}")
print(f"Classification rep for sentiments with RFC test\n:{classification_report(y_sentiment_test, rfc_sentiment_test)}")

# print()

# pipeline_rfc_sent.fit(X_train,y_authenticity_train)
# rfc_authenticity_train = pipeline_rfc_sent.predict(X_train)

# rfc_authenticity_test = pipeline_rfc_sent.predict(X_test)

# print(f"Accuracy for news with RFC training:{accuracy_score(y_authenticity_train, rfc_authenticity_train)}")
# print(f"Accuracy for news with RFC test:{accuracy_score(y_authenticity_test, rfc_authenticity_test)}\n")

# print(f"Classification rep for news with RFC training\n:{classification_report(y_authenticity_train, rfc_authenticity_train)}")
# print(f"Classification rep for news with RFC test\n:{classification_report(y_authenticity_test, rfc_authenticity_test)}")

pipeline_svc.fit(X_train, y_sentiment_train)
svc_sentiment_train = pipeline_svc.predict(X_train)

svc_sentiment_test = pipeline_svc.predict(X_test)

print(f"Accuracy for sentiments with RFC training:{accuracy_score(y_sentiment_train, svc_sentiment_train)}")
print(f"Accuracy for sentiments with RFC test:{accuracy_score(y_sentiment_test, svc_sentiment_test)}\n")

print(f"Classification rep for sentiments with RFC training\n:{classification_report(y_sentiment_train, svc_sentiment_train)}")
print(f"Classification rep for sentiments with RFC test\n:{classification_report(y_sentiment_test, svc_sentiment_test)}")
pipeline_svc.fit(X_train,y_authenticity_train)
svc_authenticity_train = pipeline_svc.predict(X_train)

svc_authenticity_test = pipeline_svc.predict(X_test)

print(f"Accuracy for news with SVC training:{accuracy_score(y_authenticity_train, svc_authenticity_train)}")
print(f"Accuracy for news with SVC test:{accuracy_score(y_authenticity_test, svc_authenticity_test)}\n")

print(f"Classification rep for news with SVC training\n:{classification_report(y_authenticity_train, svc_authenticity_train)}")
print(f"Classification rep for news with SVC test\n:{classification_report(y_authenticity_test, svc_authenticity_test)}")

pipeline_svc.predict(["हाउस डिम एड: हमने जेसन चैफेट के ट्वीट करने तक कॉमी का पत्र भी नहीं देखा,हाउस डिम एड : हमने अक्टूबर  डारेल ल्यूकस इसे कॉमी पत्र नहीं देखा  अमेरिकन फोर्क  यूटा स्टैम्प जेसन शैफेट्ज सदस्यता लें ( छवि सौजन्य माइकल लॉली  एक क्रिएटिव कॉमन्स-बाय लाइसेंस तहत उपलब्ध ) कीथ ओल्बरमैन माफी साथ  संदेह नहीं कि विश्व खराब व्यक्ति सप्ताह है-एफबीआई निदेशक जेम्स कॉमी। एक हाउस डेमोक्रेटिक सहयोगी अनुसार  ऐसा लगता कि हम जानते कि दूसरा खराब व्यक्ति है। पता चला कि कॉमी अब-कुख्यात पत्र घोषणा कि एफबीआई उन ईमेलों देख जो हिलेरी क्लिंटन ईमेल सर्वर संबंधित  तो संबंधित समितियों रैंकिंग डेमोक्रेट कॉमी बारे सुना नहीं है। रिपब्लिकन कमेटी एक अध्यक्ष एक ट्वीट माध्यम पता चला। जैसा कि अब हम जानते  कॉमी रिपब्लिकन अध्यक्षों और हाउस इंटेलिजेंस  ज्यूडिशियरी  और ओवरसाइट समितियों डेमोक्रेटिक रैंकिंग सदस्यों सूचित कि एजेंसी उन ईमेलों समीक्षा रही थी जिन्हें हाल पता चला कि क्या वे वर्गीकृत जानकारी रखते हैं। पत्र बाहर जाने लंबे समय  ओवरसाइट कमेटी अध्यक्ष जेसन चैफेट्ज़ ट्वीट साथ राजनीतिक दुनिया आग लगा दी। एफबीआई डर मुझे सूचित  `` एफबीआई उन ईमेलों अस्तित्व बारे सीखा जो जांच अनुसार प्रतीत हैं। '' मामला खुल - जेसन शैफेट्ज़ (  ) अक्टूबर  बेशक  अब हम जानते कि मामला नहीं था। कॉमी वास्तव कह कि `` एक असंबंधित मामला '' प्रकाश ईमेल समीक्षा  जो अब हम एक किशोर साथ एंथोनी वेनर सेक्सटिंग जानते हैं। स्पष्ट रूप छोटी चीजें तथ्य रूप महत्वपूर्ण नहीं थीं। यूटा रिपब्लिकन जांच शुरू कसम खाई थी कि अगर हिलेरी कम कम साल जीतती  और संभवत : पूरे कार्यकाल लायक हैं। जाहिर तौर शैफेट्ज लगा कि एफबीआई काम रही - परिणामस्वरूप एक ट्वीट देश हल्का  कि कूलर प्रमुखों एहसास कि एक कठिन घटना है। एक वरिष्ठ हाउस डेमोक्रेटिक सहयोगी अनुसार  उस पत्र गलत तरीके फैलाना शायद चैफेट पापों कम कम हो। उस सहयोगी शेयरब्लू बताया कि बॉस और डेमोक्रेट उस समय कॉमी पत्र बारे नहीं पता - और केवल तभी पता चला उन्होंने ट्विटर जाँच की। `` संबंधित समितियों डेमोक्रेटिक रैंकिंग सदस्यों रिपब्लिकन अध्यक्षों कॉमी पत्र नहीं मिला। वास्तव डेमोक्रेटिक रैंकिंग सदस्यों इसे प्राप्त नहीं कि ओवरसाइट और सरकारी सुधार समिति अध्यक्ष  जेसन चैफेट्ज़ इसे ट्वीट नहीं और इसे सार्वजनिक दिया। ” तो चलो देखते कि क्या हमें अधिकार मिला है। एफबीआई निदेशक शैफेट और जीओपी समिति अध्यक्षों संभावित रूप राजनीतिक रूप विस्फोटक जांच एक प्रमुख विकास बारे बताता  और न शैफेट और सहयोगियों डेमोक्रेटिक समकक्षों बारे बताने शिष्टाचार था। बजाय  सहयोगी अनुसार  ट्विटर बारे पता लगाया। डेली कोस बात चुकी कि कॉमी खुद शैफेट और रिपब्लिकन पत्र अग्रिम नोटिस  जिससे स्पिन मशीन चालू समय मिल गया। कि अच्छे थिएटर बना  ऐसा नहीं जो बताता कि मामला है। आखिरकार  ऐसा नहीं जो बताता कि कॉमी घोर अक्षम और टोन-बहरा अलावा नहीं था। हालांकि  सुझाव देता कि चैफेट्ज़ एक अभिनय  जो डैन बर्टन और डेरेल इस्सा ज़िम्मेदारी और द्विदलीयता मॉडल दिखता है। पास विस्फोटक बारे रैंकिंग सदस्य एलिजा कमिंग्स सूचित शालीनता नहीं थी। निष्पक्षता बुनियादी मानकों नहीं रौंदता  तो मुझे नहीं पता कि क्या है। दी गई  संभावना नहीं कि शैफेट जवाब देना होगा। प्रोवो और ओरेम लंगर डाले एक हास्यास्पद रिपब्लिकन जिले बैठता ; + कुक पार्टिसन वोटिंग इंडेक्स  और मिट रोमनी प्रतिशत वोट दंड था। अलावा  रिपब्लिकन हाउस नेतृत्व शैफेट योजनाबद्ध मछली पकड़ने अभियान पूर्ण समर्थन है। मतलब नहीं कि हम उस गर्म रोशनी नहीं डाल सकते। आखिरकार  एक पाठ्यपुस्तक उदाहरण जो सदन रिपब्लिकन नियंत्रण है। और दुनिया दूसरा बुरा व्यक्ति है। डेरेल लुकस बारे डारेल उत्तरी कैरोलिना विश्वविद्यालय स्नातक जो खुद पुराने स्कूल पत्रकार मानता है। कॉलेज धार्मिक अधिकार एक सदस्य रूप बदलने प्रयास केवल धार्मिक अधिकार बुरे सपने बदलने सफल - एक करिश्माई ईसाई जो एक अप्रकाशित उदारवादी है। उन लोगों खड़े इच्छा जो केवल चुप्पी डर गए  एक अपमानजनक तीन साल शादी बच गए। ईपू  डेली कोस ईसाई मांग रूप जान हैं। ट्विटर  अनुसरण फेसबुक साथ जुड़ें। खरीदने यहां क्लिक करें। जुडिये"])

!pip install joblib
import joblib
joblib.dump(pipeline_svc, '/content/drive/MyDrive/NLP Project/news_classifier.pkl')
# joblib.dump(pipeline_rfc_sent,'/content/drive/MyDrive/NLP Project/sentiment_classifier.pkl')

zero_sentiment_rows = train[train['sentiment'] == 0]
zero_sentiment_rows.text

