import requests
from bs4 import BeautifulSoup
import concurrent.futures

# create a session object
session = requests.Session()

# specify the website URL
# the range specifies the no. of pages to look
urls = ['https://www.discudemy.com/language/english/' + str(i) for i in range(1, 4)]

def get_links(url):
    # send a GET request to the website
    response = session.get(url)
    # parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    # find the post
    top_posts = soup.find_all('div', class_='content')
    # iterate over the posts
    for post in top_posts:
        # find all the links in the post
        links = post.find_all('a')
        # print the links
        for link in links:
            l = link.get('href')
            l = l.replace("English", "go")
            response = session.get(l)
            soup = BeautifulSoup(response.content, 'html.parser')
            tp = soup.find_all('div', class_ = 'ui segment')
            for p in tp:
                a_link = p.find_all('a')
                i = 0
                for b_link in a_link:
                    if(i%2==0):
                        print(b_link.get('href') + "\n")
                        
                    i+=1

# use multi-threading to send requests simultaneously
with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = []
    for url in urls:
        futures.append(executor.submit(get_links, url))

print("done")
