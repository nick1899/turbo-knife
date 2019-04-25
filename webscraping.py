from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://coreyms.com/').text


soup = BeautifulSoup(source, 'lxml')

# Create CSV file for output
csv_file = open('cms_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])


for article in soup.find_all('article'):

    # header
    headline = article.h2.a.text
    print(headline)

    # summary
    summary = article.find('div', class_='entry-content').p.text
    print(summary)

    
    
    try:
        # link
        vid_src = article.find('iframe', class_='youtube-player')['src']

        # parse for Youtube
        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]

        # create youtube link
        yt_link = f'https://youtube.com/watch?v={vid_id}'

    except expression as identifier:
        yt_link = None

    print(yt_link)
    
    print()

    csv_writer.writerow([headline, summary, yt_link])

csv_file.close()
