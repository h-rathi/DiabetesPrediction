# final script
import numpy as np
import joblib
import pickle
# from sklearn.preprocessing import StandardScaler

#load the model as classifer 
with open("model.pkl", "rb") as f:
    classifier = pickle.load(f)

user_input=input("enter values separated by comma(,) ")
array=user_input.split(',')
for i in range(len(array)):
  array[i]=float(array[i])
print(array)
# convert the array to numpy array
array=np.asarray(array)
#convert to 2d array
array=array.reshape(1,-1)
print(array)

#load the scaler 
scaler = joblib.load("scaler.pkl")

array=scaler.transform(array)
result=classifier.predict(array)
print(result)
if result==0:
  print("The person is Diabetic")
else:
  print("The person is not Diabetic")