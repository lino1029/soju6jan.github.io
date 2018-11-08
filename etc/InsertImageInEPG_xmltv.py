# -*- coding: utf-8 -*-
import sys, os
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append(os.path.join( os.getcwd(), 'lib' ))


import xml.etree.ElementTree as ET

import re
import pickle
import urllib, urllib2
import json	

DAUM_TV_SRCH   = "http://movie.daum.net/data/movie/search/v2/tv.json?size=20&start=1&searchText=%s"

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait

def insert_image():
	driver = webdriver.Remote(command_executor='http://127.0.0.1:8910', desired_capabilities=DesiredCapabilities.PHANTOMJS)
	driver.implicitly_wait(10)
	history = GetHistory()
	wrong = {}
	filename = 'xmltv.xml'
	#filename = '/volume1/homes/soju6jan/soju6jan.github.io/klive.xml'
	tree = ET.parse(filename)
	root = tree.getroot()

	list = root.findall('programme')
	total = len(list)
	count = 0
	for item in list: #list[:10]:
		count += 1
		#print('%s / %s' % (count, total))
		#print item.tag
		title = item.find('title')
		icon = item.find('icon')
		if icon is None:
			#print 'ORIGINAL : %s' % title.text
			search_text = title.text
			patten = re.compile(r'\(.*?\)')
			search_text = re.sub(patten, '', search_text).strip()

			patten = re.compile(r'\[.*?\]')
			search_text = re.sub(patten, '', search_text).strip()

			patten = re.compile(u'\s\d+회$')
			search_text = re.sub(patten, '', search_text).strip()

			patten = re.compile(u'\s\d+화$')
			search_text = re.sub(patten, '', search_text).strip()

			patten = re.compile(u'\s\d+부$')
			search_text = re.sub(patten, '', search_text).strip()

			patten = re.compile(u'^재\s')
			search_text = re.sub(patten, '', search_text).strip()

			#print 'SEARCH   : %s' % search_text
			try:
				if search_text in history:
					img = history[search_text]
					#print('EXIST IN HISTROTY ')
				elif search_text in wrong:
					#print('ALREADY FAIL')
					img = None
				else:
					img = get_daum_poster(search_text, driver)
					if img is not None:
						history[search_text] = img
					else:
						wrong[search_text] = None
				if img is not None:
					element = ET.Element('icon')
					element.attrib['src'] = img
					item.append(element)
			except:
				import traceback
				exc_info = sys.exc_info()
				traceback.print_exception(*exc_info)

		else:
			#print('ICON EXIST')
			pass
		#print
	SaveHistory(history)
	tree.write('xmltv_icon.xml', encoding='utf-8', xml_declaration=True)

from bs4 import BeautifulSoup
# soup = BeautifulSoup(html_doc, 'html.parser')

def get_daum_poster(str, driver):
	try:
		
		#print
		#print(str)
		url = 'https://search.daum.net/search?w=tv&q=%s' % (urllib.quote(str.encode('utf8')))
		#print(url)
		
		#request = urllib2.Request(url)
		#response = urllib2.urlopen(request)

		#data = response.read()
		driver.get(url)
		data = driver.page_source

		#print(data)
		re_id = re.compile('irk\=(?P<id>\d+)')
		match = re_id.search(data)  
		id = match.group('id') if match else ''
		#print ('ID : %s' % id)
		if id is not '':
			#//*[@id="tv_program"]/div[1]/div[1]/a
			
			a = WebDriverWait(driver, 3).until(lambda driver: driver.find_element_by_xpath('//*[@id="tv_program"]/div[1]/div[1]/a/img'))
			poster_url = '%s' % a.get_attribute('src')

			#url = 'http://movie.daum.net/tv/main?tvProgramId=%s' % id
			#request = urllib2.Request(url)
			#response = urllib2.urlopen(request)
			#data = response.read()
			#print data
			
			#soup = BeautifulSoup(data, 'html.parser') 
			#poster_url = soup.find('img', {'class' : 'img_summary'})['src']
			print('POSTER URL : %s' % poster_url)
			#sys.exit(1)
			return poster_url
		else:
			#print('SEARCH FAIL!!')
			return None
	except:
		import traceback
		exc_info = sys.exc_info()
		traceback.print_exception(*exc_info)
		
	
	


def GetHistory():
	try:
		HISTORY = os.path.join( os.getcwd(), 'daum_poster_urls.txt')
		file = open(HISTORY, 'rb')
		history = pickle.load(file)
		file.close()
	except Exception, e:
		#LOG('<<<GetHistory>>> GetLoginData: %s' % e)
		history = {}
	return history

def SaveHistory(history):
	HISTORY = os.path.join( os.getcwd(), 'daum_poster_urls.txt')
	file = open(HISTORY, 'wb')
	pickle.dump(history, file)
	file.close()


if __name__ == '__main__':
	insert_image()



"""
		#str = urllib.urlencode( str )
		url = 'http://movie.daum.net/data/movie/search/v2/tv.json?size=20&start=1&searchText=%s' % (urllib.quote(str.encode('utf8')))
		request = urllib2.Request(url)
		response = urllib2.urlopen(request)
		data = json.load(response, encoding='utf8')

		#print data
		if data['count'] != 0:
			id = data['data'][0]['tvProgramId']
			url = 'http://movie.daum.net/tv/main?tvProgramId=%s' % id
			request = urllib2.Request(url)
			response = urllib2.urlopen(request)
			data = response.read()
			#print data
			soup = BeautifulSoup(data, 'html.parser') 
			poster_url = soup.find('img', {'class' : 'img_summary'})['src']
			#print('POSTER URL : %s' % poster_url)
			return poster_url
		else:
			#print('SEARCH FAIL!!')
			return None
"""