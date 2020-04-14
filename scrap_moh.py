import requests
from bs4 import BeautifulSoup as soup
import pandas as pd

def get_state_data():
	url='https://www.mohfw.gov.in/'
	data=requests.get(url)
	page_data = soup(data.text,'html.parser')

	soup_table=page_data.find_all('div',{'class':'data-table table-responsive'})[0]
	soup_row=soup_table.find_all('tr')
	r=len(soup_row);
	for i in range(0,r):
	    soup_row[i]=soup_row[i].text.split('\n')
	arr=[]
	for i in range(1,r-2):
	    temp=[]
	    #temp.append(soup_row[i][1])S.no is inbuilt in DataFrame
	    temp.append(soup_row[i][2])
	    temp.append(int(soup_row[i][3]))
	    temp.append(int(soup_row[i][4]))
	    temp.append(int(soup_row[i][5]))
	    arr.append(temp)

	df=pd.DataFrame(arr)
	df.columns=['State','Total Confirmed Cases','Cured/Discharged/Migrated','Death']

	df_lat_lon = pd.read_excel('data/state_latlng.xlsx')
	df = pd.merge(df,df_lat_lon,on='State')
	return df