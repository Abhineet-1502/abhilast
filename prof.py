import pandas as pd
data={
    'Years of Experience':[1.1,1.2,1.3,1.4,2.1,2.3,2.5,2.8,2.9,3.7,3.9,4.1,4.5,5,6.6],
    'Salary':[10000,12000,14000,10230,20000,21000,25000,28000,29000,37320,39000,41660,45200,50000,66000]
}
df=pd.DataFrame(data)
print(df)
csv_filename='Data13.csv'
df.to_csv(csv_filename, index='False')