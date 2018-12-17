import sys
# route sets up endpoints allowing requests to site. requires @ sign. not case sensitive
# run runs a server
# template looks inside of directories to pull files. can update without restarting server
# request provides query paramaters
from bottle import route, run, template, static_file, request, error
import json
import feedparser

path = sys.path[0]

d = feedparser.parse("https://www.jpost.com/Rss/RssFeedsHeadlines.aspx")
headline = []

for i in d.entries:
    headline.append({"title": i.title, "link": i.link})

print(headline)

@route('/rss_display', method='GET')
def rss_display():
    return json.dumps(headline)

@route('/')
def html():
    return template(path+"/index.html")
    
# USING RUN INSTEAD OF MAIN SINCE DONT HAVE A MAIN FUNCTION
if __name__ == '__main__':
    run(host='localhost', port=8080)