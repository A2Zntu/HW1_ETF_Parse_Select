import csv
import requests as re
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

delay = 30 # seconds
inputFileName = "group17_region.csv"
baseUrl = "https://finance.yahoo.com/quote/"
urlDdata = "/history?period1=1451491200&period2={}&interval=1d&filter=history&frequency=1d".format(int(time.time()))
symbols = []
chromedriver = "./driver/chromedriver"
monthPair = {"Jan":1,"Feb":2,"Mar":3,"Apr":4,"May":5,"Jun":6,"Jul":7,"Aug":8,"Sep":9,"Oct":10,"Nov":11,"Dec":12}


def dateConvert(inpu):
	# convert the date to correct format
	inputList = inpu.replace(",","").split(" ")
	month = monthPair[inputList[0]]
	day = inputList[1]
	year = inputList[2]
	output = "{}-{}-{}".format(year,month,day)
	return output


def waiting(browser):
	# wait the browser to load JS and track whether the browser is time out (ex : server crash will cause browser time out)
	try:
		myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr')))
		return 1
	except TimeoutException:
		print("Loading took too much time!")	
		return 0



def oneDayParse(rowElement):
	# parse one row data
	dataList = rowElement.find_elements_by_xpath(".//td")
	if len(dataList) < 3:
		output = {"date" : dateConvert(dataList[0].text),
			"open" : None,
			"high" : None,
			"low"  : None,
			"close": None,
			"AdjClose": None,
			"volume":None
		}

	else:
		output = {"date" : dateConvert(dataList[0].text),
				"open" : dataList[1].text,
				"high" : dataList[2].text,
				"low"  : dataList[3].text,
				"close": dataList[4].text,
				"AdjClose": dataList[5].text,
				"volume":dataList[6].text.replace(",","")
		}

	return output


if __name__ == '__main__':

	# read all ETF we need in our csv file
	with open(inputFileName, newline='') as csvfile:
		rows = csv.DictReader(csvfile)
		for row in rows:
			symbols.append(row["Symbol"])

	# open selenium browser
	browser = webdriver.Chrome(chromedriver)

	# one loop for one ETF
	for s in symbols:

		# init our record list
		symbolData = []

		# go to the correspond url
		browser.get(baseUrl + s + urlDdata)
		print("we are at "+ s)

		# check function "waiting"
		if waiting(browser):
			print("success open page of ETF {}".format(s))

			# init data list
			allRow = []

			# scroll the browser to get more data, stop when we get 3000 days or there are no more data
			while (len(allRow) < 3000) and (len(allRow) % 100 == 0):
				ActionChains(browser).key_down(Keys.PAGE_DOWN).perform()
				allRow = browser.find_elements_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr')		

			# record all data in a list
			for rowIndex in range(len(allRow)):
				symbolData.append(oneDayParse(allRow[rowIndex]))
				if rowIndex%300 == 0:
					print("{} days done".format(rowIndex))			
			print("success load all data of ETF {}".format(s))


			# record our data in a csv
			with open('dirtyData/{}.csv'.format(s), 'w', newline='') as csvfile:
				fieldnames = ["date","open","high","low","close","AdjClose","volume"]
				writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
				writer.writeheader()
				writer.writerows(symbolData)

			print("{} record done".format(s))		

		else:
			print("QQ for {}".format(s))


	browser.close()