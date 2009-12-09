import urllib2, cookielib

cj = cookielib.LWPCookieJar('/home/mononofu/Programmieren/browser-game-bot/cookies.txt')
#cj.load()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

url = "http://localhost/ogame/new/"