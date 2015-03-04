__author__ = 'Omkareshwar'


from bs4 import BeautifulSoup, SoupStrainer
import urllib2, ftplib, urllib

def func(toplink):
    links = SoupStrainer('a')
    try:
        page = urllib2.urlopen(toplink)
        soup = BeautifulSoup(page.read(), parse_only=links)
        for link in soup('a'):
            s = str(link.get('href'))
            if(s.__contains__('zip') and not s.__contains__('128')):
                print(s)
                """filename = 'temp.zip'
                urllib.urlretrieve(s, filename)
                writeftp('temp.zip')"""


    except Exception as e:
        pass

def func2(alphabet):
    url = alphabet
    links = SoupStrainer('a')
    try:
        page = urllib2.urlopen(url)
        soup = BeautifulSoup(page.read(), parse_only=links)
        for link in soup('a'):
            s = str(link.get('href'))
            func('http://www.songspk.name/' + link.get('href'))
    except Exception as e:
        pass

def writeftp(file):
    ftp = ftplib.FTP()
    ftp.connect("ftp.irtiamized.com", 21)
    ftp.login("nikitph@irtiamized.com", "#@$hkey123")
    print("logged in")
    ftp.storbinary("STOR " + file, open(file, "rb"), 1024)
    print("file stored")
    ftp.close()





url = 'http://www.songspk.name/bollywood-songs-mp3.html'
links = SoupStrainer('a')
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read(), parse_only=links)
for link in soup('a'):
    s = str(link.get('href'))
    if(s.__contains__('list')):
        print(s)
        func2('http://www.songspk.name/' + link.get('href'))


