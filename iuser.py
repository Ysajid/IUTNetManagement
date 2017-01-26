import mechanize
import re
from bs4 import BeautifulSoup
import urllib2 
import cookielib

def connect() : {

}

def getRemainingTime(userid, password) : 
    cj = cookielib.CookieJar()
    br = mechanize.Browser()
    br.set_cookiejar(cj)
    br.open("http://10.220.20.12/index.php/home/login")

    br.select_form(nr=0)
    br.form['username'] = userid
    br.form['password'] = password
    br.submit()

    response  = br.response().read().replace('\n',' ')
    usage = re.findall(r'<td>([0-9]+) Minute+', response)

    return usage


getRemainingTime("yeminsajid", "______")
