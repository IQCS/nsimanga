import requests                    #On importe le module requests
import urllib.request              #On importe le module urllib.request
import time                        #On importe le module time
from bs4 import BeautifulSoup      #On importe le module BeautifulSoup de bs4
import os                          #On importe le module os
if __name__ == '__main__':   #Cette ligne permet que le script soit executé seulement si le fichier "Download.py" est éxécuté et pas s'il est importé dans un autre script
    def dossier():           #On crée la fonction dossier qui ne prend pas d'arguments
        os.chdir("Google Drive//Python//Web-Scrapper")  #On change de dossier pour se diriger dans le fichier Google drive/Python/Web-scrapper

    dossier() #On execute la fonction dossier

"""

Initialisation

"""


path = r"C:\Users\Sylgi\Desktop\Manga Scrapper"
CompteurParcours = 0



def Navigate(url):
    if url != "Fin du Manga":
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        ListeLiens = RecupListeLiens(soup)
    return [soup, ListeLiens]

def RecupListeLiens(soup):
    Div = soup.findAll('div')
    L = []
    for item in Div:
        if ClasseDownload(item):
            L.append(item)
    ListeTag = []
    for item in L:
        ListeTag.append(item.find('img'))
    ListeLiens = []
    for item in ListeTag:
        t = item['src']
        n = t.find('https')
        ListeLiens.append(item['src'][n:])
    return ListeLiens



def Next(soup):
    NextUrl = ""
    A = soup.findAll('a')
    L = []
    for a in A:
        if 'class' in a.attrs and a['class'] == ['btn','next_page']:
            NextUrl = a['href']
    if NextUrl == "":
        NextUrl = "Fin du Manga"
    print(NextUrl)
    return NextUrl


def ClasseDownload(item):
    bool = False
    bool = 'class' in item.attrs and (item['class'] == ['page-break'])
    return bool

def ClasseNextDiv(item):
    bool = False
    bool = 'class' in item.attrs and (item['class'] == ['navi-change-chapter-btn'] or item['class'] == ['btn-navigation-chap'])
    return bool

def ClasseNextListe(tag):
    bool = False
    bool = 'class' in tag.attrs  and (tag['class'] ==['navi-change-chapter-btn-next','a-h'] or tag['class'] == ['next'])
    return bool
