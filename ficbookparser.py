import requests as req
from bs4 import BeautifulSoup
import re, os

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
}

def __save_txt(chapter_name,content,fiction_name):
    with open(f'{fiction_name}/{chapter_name}.txt', 'wt', encoding='utf-8') as output:
        output.write(str(content))

def parse(url):
    r = req.get(url, headers= headers)
    return BeautifulSoup(r.content, 'lxml')

def get_title(fanfiction):
    title = fanfiction.find('h1', {'class': 'mb-10'}).text
    title = re.sub('[/|"|<|>|:|?|*]','',title)
    title = re.search('[^ ].+[^ ]', title).group()
    return title

# Get list of all chapters
def get_chapters(fanfiction, print_results = False):
    chapters = fanfiction.find_all('li', {'class': 'part'})
    names = []
    links = []

    for chapter in chapters:
        name = re.findall('(?<=<h3>)(.*)(?=</h3>)', str(chapter))[0]
        link = re.findall('(?<=(<a class="part-link visit-link" href="))(.*)(?=">)', str(chapter))[0][1]
        names.append(name)
        links.append(link)
    
    if print_results == True:
        for i, name in enumerate(names):
            print(f'{i+1} | {name}')
        return

    return names, links

# Export all chapters to txt's
def export(fanfiction, chapter_num = -1):

    def save_chapter(name, link):
        content = req.get('https://ficbook.net'+link, headers= headers)
        soup = BeautifulSoup(content.content, 'lxml')
        text = soup.find('div', {'id': 'content'}).text
        name = re.sub('[/|"|<|>|:|?|*]','',name)
        __save_txt(name,text,fiction_name)
    
    fiction_name = get_title(fanfiction)

    if not fiction_name in os.listdir():
        os.mkdir(fiction_name)

    names, links = get_chapters(fanfiction)
    if chapter_num != -1:
        save_chapter(names[chapter_num-1], links[chapter_num - 1])
        return

    for num, link in enumerate(links):
        save_chapter(names[num], link)
