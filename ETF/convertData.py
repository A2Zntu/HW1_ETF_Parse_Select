import pandas as pd
import csv
import datetime

inputFileName = "group17_region.csv"

def compareDate(dateOb,stringOb):
	s0 = "{}-{}-{}".format(dateOb.year,dateOb.month,str(dateOb.day).zfill(2))
	s1 = stringOb
	return s0 == s1

def convertData(dateOb):
	return "{}-{}-{}".format(dateOb.year,dateOb.month,dateOb.day)

if __name__ == '__main__':
	symbols = []
	with open(inputFileName, newline='') as csvfile:
		rows = csv.DictReader(csvfile)
		for row in rows:
			symbols.append(row["Symbol"])

	dates = []
	finalData = {}
	finalData["time"] = []
	for s in symbols:
		dataList = []
		date = datetime.datetime.now()
		df = pd.read_csv('dirtyData/{}.csv'.format(s))
		for i in range(len(df["date"])):
			while not compareDate(date,df["date"][i]):
				if convertData(date) not in dates:
					dates.append(convertData(date))
				date -= datetime.timedelta(days=1)
				dataList.append(None)

			dataList.pop()
			dataList.append(df["AdjClose"][i])

		# print(dataList)
		finalData[s] = dataList

	finalData["time"].extend(dates)

	select_df = pd.DataFrame(finalData)
	
	print(select_df)
