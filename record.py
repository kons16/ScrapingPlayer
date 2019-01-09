# 野手のみ
import requests
import codecs
import urllib.parse
from bs4 import BeautifulSoup

def searchulr(name):
	s = name
	sq = urllib.parse.quote(s)
	linkto = "https://search.yahoo.co.jp/search?p={}&fr=spo_npb&ei=utf-8&vs=baseball.yahoo.co.jp".format(sq)

	html = requests.get(linkto).content
	soup = BeautifulSoup(html, "html.parser")
	# 選手データのページ
	dataurl = [a.get("href") for a in soup.find_all("a")][3]

	#print(soup)

	dataurl = requests.get(dataurl).content
	soup = BeautifulSoup(dataurl, "html.parser")
	yjm = soup.find_all("tr", class_="yjM")[0]
	yjmops = soup.find_all("tr", class_="yjM")[1]
	profile = soup.find_all("div", class_="yjS")[0]

	
	# 生年月日
	old = profile.find_all("td")[1].contents[0]
	# 経歴
	career = profile.find_all("td")[7].contents[0]

	# 打率
	hitrate = yjm.find_all("td")[0].contents[0]
	# 試合数
	gamecount = yjm.find_all("td")[1].contents[0]
	# 本塁打数
	homerun = yjm.find_all("td")[7].contents[0]
	# 打点数
	rbi = yjm.find_all("td")[9].contents[0]
	# OPS
	ops = yjmops.find_all("td")[9].contents[0]


	print(old)
	print(career)
	print("{0}試合 打率{1} {2}本 {3}打点 OPS{4}"
		.format(gamecount,hitrate,homerun,rbi,ops))
	print()



name = input()
searchulr(name)
