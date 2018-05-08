from datetime import timedelta, date
from bs4 import BeautifulSoup
import requests

def daterange(start_date, end_date):
	print((end_date-start_date).days)
	for n in range(int((end_date-start_date).days)):
		yield start_date + timedelta(n)

start_date = date(2017, 1, 1)
end_date = date(2018, 4, 16)

for Date in daterange(start_date, end_date):
	print(Date)
	page = requests.get('http://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station=C0R150&stname=%25E4%25B8%2589%25E5%259C%25B0%25E9%2596%2580&datepicker={}'.format(Date))
	print(page.status_code) # page.content
	soup = BeautifulSoup(page.content, 'html.parser')
	# print(soup.prettify())

	with open("%s.html" %Date, "w") as f:
		f.write(str(soup.prettify()))
		f.close()