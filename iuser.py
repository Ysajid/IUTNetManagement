import mechanize
from bs4 import BeautifulSoup
import urllib2 
import cookielib

cj = cookielib.CookieJar()
br = mechanize.Browser()
br.set_cookiejar(cj)
br.open("http://10.220.20.12/index.php/home/login")

br.select_form(nr=0)
br.form['username'] = 'yeminsajid'
br.form['password'] = '-------'
br.submit()

print br.response().read()
