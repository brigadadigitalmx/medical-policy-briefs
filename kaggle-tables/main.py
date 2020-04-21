import re
from pathlib import Path
from selenium import webdriver
import pandas as pd

driver = webdriver.Firefox()
driver.get("https://www.kaggle.com/covid-19-contributions")

elems = driver.find_elements_by_class_name('c19-finding')

first = elems[0]

headers = first.find_elements_by_class_name('heading6')
tables = first.find_elements_by_class_name('c19-table')

assert len(headers) == len(tables)

Path('output').mkdir(exist_ok=True)
pattern = re.compile('[\W_]+')

for header, table in zip(headers, tables):
    name = pattern.sub('_', header.text )
    print(name)
    table_html = table.get_attribute('innerHTML')
    df = pd.read_html('<table>{}</table>'.format(table_html))[0]
    df.to_csv(str(Path('output', name+'.csv')), index=False)
