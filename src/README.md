# Web_data_parser

For the usage of ETF NAV monthly returns 

### Installing

```
pip install bs4
```

```
pip install urllib
```
## NAV finished ETF
ETF Company | NAV finished
----------- | ------------
First       |  
FlexShares  |       Y
Global      | 
Goldman     | 
Invesco     |
iShares     |       Y
Renaissance |
SPDR        |
VanEck      |
Vanguard    |
WisdomTree  |
Xtrackers   |

## Break down the procedure

Read the ETF list, and try to find the home page of each ETF.  

### Instantiates the home page from ETFdb.com

``` python 
get_home_page(url, sym)   
```
 * url: The specific path on ETFdb.com 
 * sym: Symbol of this ETF


### classify the link, and redirect them to their own website page with unique scraping fashion

``` python 
classify_web_page(link, sym, groupName)  
```
 * link: The home page link
 * sym: Symbol of this ETF
 * groupName: Group name of this ETF


### Take flexshare as example
```python
download_from_flexshares(link, sym)
 ```
 
 ### Download raw csv
 ```python
write_raw_csv(url, csv_name, results_path = os.path.join(work_dir, 'data', 'Raw_csv')
 ```
 * url: The download path
 * csv_name: The name of your csv file
 * results_path: The path you'd like to store the file



## License

This project is licensed under the MIT License

