import pandas as pd

l1 = ['kav','muthu', 'raja', 's']
l2 = [1, 2, 3]

ds1 = pd.Series(l1, index=['a', 'b', 'c', 'd'])
print(ds1)
ds2 = pd.Series(l2)

ds1[1:3]='dd'
print(ds1)
