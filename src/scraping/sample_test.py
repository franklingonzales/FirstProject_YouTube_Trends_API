import requests
from bs4 import BeautifulSoup


#url = 'https://socialblade.com/youtube/user/caseyneistat'

#response = requests.get(url)

#if response.status_code == 200:
#else:
#    print (f"Error loading url - return_code : {response.status_code}")

with open("../../documents/socialblade_template.html") as f:
    #soup = BeautifulSoup(f,features='lxml')
    soup = BeautifulSoup(f, 'html.parser')

print (soup.title)

total_uploads = soup.find('span', id='youtube-stats-header-uploads').text
total_subscriptions = soup.find('span', id='youtube-stats-header-subs').text
total_views = soup.find('span', id='youtube-stats-header-views').text

print (f"Total of uploads.........: {total_uploads}")
print (f"Total of subscriptions...: {total_subscriptions}")
print (f"Total of Views...........: {total_views}")

#for element in soup.find_all('span', id='youtube-stats-header-uploads'):
#    print (element.text)