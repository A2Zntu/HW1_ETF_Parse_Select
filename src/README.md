# ETF_PARSE_SELECT

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
def get_home_page(url, sym):
    '''Parse the Home page from ETFdb.com'''
    time.sleep(0.5)
    resp = requests.get(url = url)
    dom = resp.text
    soup = BeautifulSoup(dom, 'html.parser')
    if soup.find_all('a', string = "Home page"):
        link = str(soup.find('a', string = "Home page").attrs['href'])
        return str(link)
    else:
        print("Can't find the home url!")
    
```

### classify the link, and redirect them to their own website page with unique scraping fashion

``` python 
def classify_web_page(link, sym, groupName):
    if groupName == 'FlexShares':
        download_from_flexshares(link, sym)
        return True
    elif groupName == 'iShares':
        download_from_ishares(link, sym)
        return True
        
    else:
        print("Can't download raw csv!")
        return False
    
```

### Take flexshare as example
```python
def download_from_flexshares(link, sym):
    time.sleep(0.5)
    resp = requests.get(url = link)
    dom = resp.text
    soup = BeautifulSoup(dom, 'html.parser')
    csv_name = sym + ".csv"
    if soup.find('a', href = re.compile(".*?\.csv")):
        link_tail = soup.find('a', href = re.compile(".*?\.csv")).attrs['href']
        url = 'https://www.flexshares.com' + str(link_tail)
        write_raw_csv(url, csv_name)
    else:
        print("Can't download raw csv!")
 ```
 
 ### Download raw csv
 ```python
 def write_raw_csv(url, csv_name, results_path = os.path.join(work_dir, 'data', 'Raw_csv')):
    '''Write csv from url'''
    if not os.path.isdir(results_path):
        os.mkdir(results_path)
    response = requests.get(url)
    with open(os.path.join(results_path, csv_name),  'wb') as f:
        f.write(response.content)
        f.close()
    print("Sucessfully writing {}".format(csv_name))
 
 ```



## License

This project is licensed under the MIT License
