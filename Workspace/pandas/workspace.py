import pandas as pd

s1 = pd.Series([1, 2, 3, 4])
s2 = pd.Series([7,8])

print((s1+s2).count())
