# ETF web crawler

## Something need to update
Our working on ETF's homepage, codes are in other branches</br>
flow chart</br>
Problems</br>
</br></br>
## Set up environment
First, you need Python 3.6+ and pip 18+ in your device＜/br＞
Install all packages with this command:
```
./install.sh
```
</br>

## How to use
csv datas</br>
https://drive.google.com/open?id=17cRLsfyaU_RAoIh6CMzMwxDacQa1CY0w
unzip this under ETF folder</br>

Get all data in csv form, data will save in "dirtyData"
```
Python getData.py
```

Convert them into pandas dataframe and print
```
Python convertData.py
```
</br>

## Result

<img src="https://github.com/A2Zntu/HW1_ETF_Parse_Select/blob/ETF_price/ETF/result.png" width="500">

</br>

## How does we implement

<img src="https://github.com/A2Zntu/HW1_ETF_Parse_Select/blob/ETF_price/ETF/chart.png" width="500">
</br>

## Common Problems
1. Don't know where to run our command.</br>
Ans : Use windows powershell.</br>
</br>
2. Selenium cost too much time to get ETF data.</br>
Ans : It's because the browser is slow, we can't help you about this.</br>
3. If you failed when running "getData.py", check if you has "group17_region.csv".</br>
4. If you can open the browser but cannot get data, it may because yahoo change its html format.</br>
5. Our program can tell you many information, try to check text shown in the cmd window</br>

