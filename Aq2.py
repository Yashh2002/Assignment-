import pandas as pd
info={'Gender':['Male','Female','Male','Female','Female'], 
      'Position':['Head','Asst.prof','Associate Prof.','Head','Asst.Prof.']
     }
df=pd.DataFrame(info)
print(df)
from sklearn.preprocessing import LableEncoder 

le=LableEncoder()

gender_encoded=le.fit_tramsform(df['Gender'])
encoded_position=le.fit_transform(df['Position'])

df['Encoded_Gender']=gender_encoded
df['Encoded_Position']=encoded_position
print(df)
