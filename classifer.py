from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split,cross_val_score
from data import df
train_X,test_X,train_Y,test_Y=train_test_split(df['URL'],df['Label'],test_size=0.1,random_state=12)
vectorization = TfidfVectorizer()
train_XV = vectorization.fit_transform(train_X)
test_XV = vectorization.transform(test_X)
from sklearn.naive_bayes import MultinomialNB
mnb = MultinomialNB()
mnb.fit(train_XV,train_Y)
testing_news = ['www.paypal.ca.0247.secure2h.idhfvidshvgd']
pred_Y = mnb.predict(vectorization.transform(testing_news))
print(pred_Y[0])

# from sklearn import metrics
# print(metrics.accuracy_score(train_Y, pred_Y))