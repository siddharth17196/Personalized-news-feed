from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup as soup

nt = 'https://www.nytimes.com/section/'
sec = ['world', 'science', 'technology']

final_head = []
final_link = []

s = requests.Session()
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'} #bot protection

# g_tech = s.get(gn, headers=headers)
# print(g_tech.status_code)
# so = soup(g_tech.content, 'html.parser')
# g_news_list = so.find_all('article')[:15]
# print(len(g_news_list))
# newl=[]
# for gnl in g_news_list:
# 	if gnl.find('h3')!=None:
# 		newl.append(gnl.find('h3'))
# g_news_list	= newl
# print(len(g_news_list))
# g_news_list = [gnl.find('a', class_='DY5T1d') for gnl in g_news_list]
# gt_head = [gnl.get_text() for gnl in g_news_list]
# gt_link = [(gnhome + gnl['href'][1:]) for gnl in g_news_list]
# final_head.append(gt_head)
# final_link.append(gt_link)

for tab in sec:
	nt_link = nt+tab
	nt_all = s.get(nt_link, headers=headers)
	so = soup(nt_all.content, 'html.parser')
	nt_news = [ntn.find('h2') for ntn in so.find_all('article')]
	newl=[]
	for ntl in nt_news:
		if ntl.find('a')!=None:
			newl.append(ntl.find('a'))
	nt_news	= newl
	news_head = [ntl.get_text() for ntl in nt_news]
	news_link = [ntl['href'] for ntl in nt_news]
	final_head.append(news_head)
	final_link.append(news_link)

print(*final_head[2], sep="\n")