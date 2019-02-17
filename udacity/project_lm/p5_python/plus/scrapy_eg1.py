# 原文章1 https://mp.weixin.qq.com/s/dFna4N-ZgQ1KAiA5LqirnA
# 原文章2（sci） https://towardsdatascience.com/data-science-skills-web-scraping-using-python-d1a85ef607ed

# import libraries
import urllib.request
from bs4 import BeautifulSoup
import csv
from pprint import pprint

# specify the url
print('\n---url---\n')
urlpage =  'http://www.fasttrack.co.uk/league-tables/tech-track-100/league-table/' 
print(urlpage)
# query the website and return the html to the variable 'page'
page = urllib.request.urlopen(urlpage)
# parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(page, 'html.parser')
# find results within table
table = soup.find('table', attrs={'class': 'tableSorter'})
results = table.find_all('tr')
print('Number of results', len(results))
print(results[:1])

# create and write headers to a list 
print('\n---rows---\n')
rows = []
rows.append(['Rank', 'Company Name', 'Webpage', 'Description', 'Location', 'Year end', 'Annual sales rise over 3 years', 'Sales £000s', 'Staff', 'Comments'])
print(rows)

print('\n---loop1---\n')
# loop over results
for result in results:
    # find all columns per result
    data = result.find_all('td')
    # check that columns have data
    # 如果像表头这种没有信息的就回因为continue结束本次循环
    if len(data) == 0: 
        continue
    
    # write columns to variables
    rank = data[0].getText()
    company = data[1].getText()
    location = data[2].getText()
    yearend = data[3].getText()
    salesrise = data[4].getText()
    sales = data[5].getText()
    staff = data[6].getText()
    comments = data[7].getText()

    # print('Company is', company)下面输出是要清理的内容
    # Company is WonderblyPersonalised children's books
    # print('Sales', sales)
    # Sales *25,860

    # extract description from the name
    companyname = data[1].find('span', attrs={'class':'company-name'}).getText() 
    # 把companyname消除以后存为desciption   
    description = company.replace(companyname, '')
    
    # remove unwanted characters
    sales = sales.strip('*').strip('†').replace(',','')

    # go to link and extract company website
    url = data[1].find('a').get('href')
    print('---checking:',url,'---')
    page = urllib.request.urlopen(url)
    # 这里要吧url给urlopen做修正，变成标准格式后存为page
    # 否则下面soup对page的格式会报错（有些小调整）
    # parse the html using beautiful soup and store in variable 'soup'
    soup = BeautifulSoup(page, 'html.parser')
    try:
        tableRow = soup.find('table').find_all('tr')[-1]
        webpage = tableRow.find('a').get('href')
    except:
        webpage = None
    
    # write each result to rows
    rows.append([rank, companyname, webpage, description, location, yearend, salesrise, sales, staff, comments])

print('\n---verifiying1:companyname---\n')
for row in rows:
    print(row[2])

print('\n---verifiying2:first3data---\n')
pprint(rows[:2])
# 使用pprint会换行
# 也可以用print '\n'.join(lst)强制加个换行
    
## Create csv and write rows to output file
with open('techtrack100.csv','w', newline='') as f_output:
    csv_output = csv.writer(f_output)
    csv_output.writerows(rows)

print('---done---')