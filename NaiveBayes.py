import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    ConfusionMatrixDisplay,
    f1_score,
    classification_report,
)


#Data Loading
df = pd.read_csv('s3://msds434finalprojectcogswell/datalab_export_2025-05-26 14_10_54.csv')
df.head()

pre_df = pd.get_dummies(df,columns=['purpose'],drop_first=True)
pre_df.head()


#Data Processing 
X = pre_df.drop('not.fully.paid', axis=1)
y = pre_df['not.fully.paid']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=125
)


#Heading 3
model = GaussianNB()

model.fit(X_train, y_train);


#Heading 4
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_pred, y_test)
f1 = f1_score(y_pred, y_test, average="weighted")

print("Accuracy:", accuracy)
print("F1 Score:", f1)
