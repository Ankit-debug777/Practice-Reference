import pandas as pd
from pandas import Series, DataFrame

data = pd.ExcelFile('dummy.xlsx')
dframe = data.parse('Sheet1')
dframe.to_csv('output1.csv',sep=',');

dframe = data.parse('Sheet2')
dframe.to_csv('output2.csv',sep=',');

dframe = data.parse('Sheet3')
dframe.to_csv('output3.csv',sep=',');

dframe = data.parse('Sheet4')
dframe.to_csv('output4.csv',sep=',');

dframe = data.parse('Sheet5')
dframe.to_csv('output5.csv',sep=',');

dframe = data.parse('Sheet6')
dframe.to_csv('output6.csv',sep=',');

dframe = data.parse('Sheet7')
dframe.to_csv('output7.csv',sep=',');

dframe = data.parse('Sheet8')
dframe.to_csv('output8.csv',sep=',');

dframe = data.parse('Sheet9')
dframe.to_csv('output9.csv',sep=',');

dframe = data.parse('Sheet10')
dframe.to_csv('output10.csv',sep=',');

