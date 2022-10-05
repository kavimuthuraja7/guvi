import pandas as pd

oneDlist = [0, 1, 2, 3, 4, 5]  # one dimension list
print("Actual List :", oneDlist)

dataSeries = pd.Series(oneDlist)  # pandas data series
print("############ Pandas data series ##############")
print(dataSeries)

print("############ Slicing ##############")
print(dataSeries[0:-1])  # slicing based on index range
print(dataSeries[[0, 1, 4]])  # picking particular values based on index

#  custom index values picking
ZeroToThree = list(range(0, 3))
ThreeAndFour = [3, 4]
combinedValues = ZeroToThree+ThreeAndFour
print("############ Custom index picking ##############")
print(dataSeries[combinedValues])

#  pandas data series with named index
namedIndexes = ['a', 'b', 'c', 'd', 'e', 'f']
namedDataSeries = pd.Series(oneDlist, index=namedIndexes)
print("############ Named data series ##############")
print(namedDataSeries)
print(namedDataSeries.iloc[[0, 2]])  # getting data from named data series using index
print(namedDataSeries[['a', 'c']])  # getting data from named data series using named index


#  access data using conditions
print("############ Access data using conditions ##############")
print(namedDataSeries.loc[(namedDataSeries % 2 == 0) & (namedDataSeries > 0)])

#  data series addition
print("############ Series Addition ##############")
series1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
series2 = pd.Series([4, 5], index=['a', 'b'])
result = series1+series2
result2 = series1.add(series2)
result3 = series1.add(series2, fill_value=0)
result4 = series2.add(series1, fill_value=0)
print(result)
print(result2)
print(result3)
print(result4)


#  pandas data frame
dataList = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
df1 = pd.DataFrame(dataList)
namedDF1 = pd.DataFrame(dataList, columns=['A', 'B', 'C'], index=[1, 2, 3])
print("############ Pandas Data Frame ##############")
print(df1)
print("############ Pandas Named index Data Frame ##############")
print(namedDF1)

# inserting rows
namedDF1.loc[len(namedDF1.index)+1] = ([11, 12, 13])
# inserting columns
namedDF1['D'] = 'Added Column'

print(namedDF1)

