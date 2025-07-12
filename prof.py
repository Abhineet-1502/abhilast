import pandas as pd
data={
    'Name':['Abhineet','Ashish','Surya','Nitin','Mudit'],
    'Age':[18,19,20,18,19],
    'City':['New Delhi','Ranchi','Udaypur','Rewadi'],
    'Employed':['Yes','No','Yes','No','Yes']
}
df=pd.DataFrame(data)
print(df)