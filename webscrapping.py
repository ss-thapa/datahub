from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'http://www.scrapethissite.com/pages/forms/'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')



title = soup.find_all('th')


title_names = [data.get_text(strip=True) for data in title]

df = pd.DataFrame(columns=title_names)

row_data = soup.find_all('td')

individeual_row_data = [data.get_text(strip=True) for data in row_data]

rows=[]
chunk_size = len(title_names)
for i in range(0, len(individeual_row_data), chunk_size):
    row_data = individeual_row_data[i:i + chunk_size]
    rows.append(row_data)

df = pd.DataFrame(rows, columns = title_names)

print(df)




