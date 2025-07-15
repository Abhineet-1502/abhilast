import pandas as pd
data={
      'Customers':[1,2,3,4,5,6,7,8,9],
      'Gender':['Male','Male','Female','Female','Female','Female','Female','Female','Male'],
      'Age':[19,21,20,23,31,22,35,23,64],
      'Annual Income (k$)':[15,15,16,16,17,17,18,18,19],
      'Spending Score(1-100)':[39,81,6,77,40,76,6,94,3]
}
df=pd.DataFrame(data)
print(df)
csv_filename='Data13.csv'
df.to_csv(csv_filename, index='False')