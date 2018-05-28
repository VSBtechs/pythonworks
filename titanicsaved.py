#kaggle titanic problem
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import OneHotEncoder



# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

import os
print(os.listdir("../input"))

# Any results you write to the current directory are saved as output.

main_file_path = '../input/train.csv' # this is the path to the Iowa data that you will use
train = pd.read_csv(main_file_path)
train_y = train.Survived
#print(train.columns)

test = pd.read_csv('../input/test.csv')
#print(test['Age'].value_counts())
#print(test[ 'Cabin'].value_counts())
#print(test['Embarked'].value_counts())

train=train.fillna({"Age": 23})
train=train.fillna({"Embarked": "S"})
train=train.fillna({"Pclass": 3})
train=train.fillna({"Sex": "male"})
train=train.fillna({"SibSp": 0})
train=train.fillna({"Parch": 0})
train=train.fillna({"Fare": 12})

test=test.fillna({"Age": 23})
test=test.fillna({"Embarked": "S"})
test=test.fillna({"Pclass": 3})
test=test.fillna({"Sex": "male"})
test=test.fillna({"SibSp": 0})
test=test.fillna({"Parch": 0})
test=test.fillna({"Fare": 12})


#encodedtrainX= pd.get_dummies(train)
#encodedtestX=pd.get_dummies(test)
#final_train, final_test =encodedtrainX.align(encodedtestX, join='left', axis=1)


cleanup_nums = {"Sex": {"male": 0, "female": 1},
                "Embarked": {"S": 0, "C": 1, "Q": 2 }}
train.replace(cleanup_nums, inplace=True)
test.replace(cleanup_nums, inplace=True)



#print(train.dtypes)
#print(test.dtypes)
predictor_cols = ['Pclass','Age', 'Sex','SibSp','Fare', 'Embarked']

test_X = test[predictor_cols]

train_X = train[predictor_cols]

#print(train[predictor_cols].isnull().sum())
#print(test[predictor_cols].isnull().sum())


#my_imputer = SimpleImputer(strategy="most_frequent")                                       
#imputed_X_train = my_imputer.fit_transform(train_X)
#imputed_X_test = my_imputer.transform(test_X)

my_model = RandomForestClassifier(n_estimators=400,max_features=None)
my_model.fit(train_X, train_y)



pred = my_model.predict(test_X)

print(pred)
my_submission = pd.DataFrame({'PassengerId': test.PassengerId, 'Survived': pred})
my_submission.to_csv('submission.csv', index=False)
