# ETF web crawler

## To TA
We tried to get some NAV data, codes about this are in NAV. But after some failed, we decided to use yahoo finance website to finish rest of this homework. 

## Set up environment
First, you need Python 3.6+ and pip 18+ in your device＜/br＞
Install all packages with this command:
```
./install.sh
```
</br>

## How to use
csv datas</br>
https://drive.google.com/open?id=17cRLsfyaU_RAoIh6CMzMwxDacQa1CY0w</br>
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

<img src="https://github.com/A2Zntu/HW1_ETF_Parse_Select/blob/master/ETF/result.png" width="500">

</br>

## How does we implement

<img src="https://github.com/A2Zntu/HW1_ETF_Parse_Select/blob/master/ETF/chart.png" width="500">
</br>

## Common Problems
1. Don't know where to run our command.</br>
Ans : Use windows powershell.</br>
</br>
2. Selenium costs too much time to get ETF data.</br>
Ans : It's because the browser is slow, we can't help you about this.</br>
</br>
3. If you failed when running "getData.py", check if you have "group17_region.csv".</br>
4. If you can open the browser but cannot get data, it may be because yahoo change its html format.</br>
5. Our program can tell you many information, try to check text shown in the cmd window</br>

