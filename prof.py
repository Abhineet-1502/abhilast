import pandas as pd
data={
    'Years of Experience':[1.1,1.2,1.3,1.4,2.1,2.5,2.3,3.7,1.9,2.8,4.1,5,6.6,4.5],
    'Salary':[30000,32000,12000,40230,20000,21000,34000,54000,62000,32320,10000,46660,31200,60000]
}
df=pd.DataFrame(data)
print(df)
csv_filename='Data13.csv'
df.to_csv(csv_filename, index='False')