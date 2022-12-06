#using pasdas
import pandas as pd
from sklearn.datasets import load_iris

iris_data=load_iris()
df=pd.DataFrame(iris_data.data, columns=iris_data.feature_names)
print(df)
training_data=df.sample(frac=0.8,random_stage=25)
testing_data=df.drop(training_data.index)

print(f"No.of training examples:{training_data.shape[0]}")
print(f"No.of testing examples:{training_data.shape[0]}")

