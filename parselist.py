import ficbookparser as fbp
from bs4 import BeautifulSoup
import requests as req

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
}

# links = ['https://ficbook.net/readfic/9417126',
#         'https://ficbook.net/readfic/6336968',
#         ]

# for url in links:
#     fic = fbp.parse(url)
#     fbp.get_chapters(fic, True)

link = 'https://ficbook.net/readfic/3293424/8642047#part_content'

# def __save_txt(chapter_name,content,fiction_name):
#     with open(f'{fiction_name}/{chapter_name}.txt', 'wt', encoding='utf-8') as output:
#         output.write(str(content))

# content = req.get(link, headers= headers)
# soup = BeautifulSoup(content.content, 'lxml')
# text = soup.find('div', {'id': 'content'}).text
# __save_txt()


fic = fbp.parse('https://ficbook.net/readfic/3293424')


fbp.export(fic, 2)