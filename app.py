import requests
from bs4 import BeautifulSoup
import pickle

def url_to_transcript(url):
    
    page = requests.get(url).text
    soup = BeautifulSoup(page, "lxml")
    text = [p.text.strip() for p in soup.find_all(class_="base-search-card__title")]
    cname = [p.text.strip() for p in soup.find_all(class_="base-search-card__subtitle")]
    print(url)
    
    return text,cname

url1 = 'https://www.linkedin.com/jobs/search?keywords={}&location={}&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=1'
url1=url1.format('JavaScript','Chennai')

x,y = url_to_transcript(url1)
print(x)
print(y)
