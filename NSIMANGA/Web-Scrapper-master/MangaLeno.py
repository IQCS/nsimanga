import requests                    #On importe le module requests
import urllib.request              #On importe le module urllib.request
import time                        #On importe le module time
from bs4 import BeautifulSoup      #On importe le module BeautifulSoup de bs4
import os                          #On importe le module os
if __name__ == '__main__':    #Cette ligne permet que le script soit executé seulement si le fichier "Download.py" est éxécuté et pas s'il est importé dans un autre script
    def dossier():            #On crée la fonction dossier qui ne prend pas d'arguments
        os.chdir("Google Drive//Python//Web-Scrapper")  #on précise  le dossier

    dossier() #On execute la fonction dossier

"""

Initialisation

"""


path = r"C:\Users\Utilisateur\Desktop\Manga Scrapper"
CompteurParcours = 0

Titre = "GOHS"
url = "http://manganelo.fun/tales-of-demons-and-gods-chapter-1"

def Initialisation(Titre):
    os.chdir(path)
    if Titre not in os.listdir():
        os.mkdir(Titre)
    os.chdir(Titre)


AA = soup.findAll('a')
for item in AA:
    if 'id' in item.attrs.keys():
        print(item.attrs)


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
    M = L[0]
    ListeTag = M.findAll('img')
    ListeLiens = []
    for item in ListeTag:
        ListeLiens.append(item['src'])
    return ListeLiens



def Next(soup):
    NextUrl = ""
    A = soup.findAll('a')
    L = []
    for a in A:
        if a.text == "NEXT CHAPTER":
            NextUrl = a['href']
    if NextUrl == "":
        NextUrl = "Fin du Manga"
    print(NextUrl)
    return NextUrl


def ClasseDownload(item):
    bool = False
    bool = 'class' in item.attrs and (item['class'] == ['container-chapter-reader'] or item['class'] == ['vung-doc'] or item['class'] == ['comic_wraCon', 'text-center'])
    return bool

def ClasseNextDiv(item):
    bool = False
    bool = 'class' in item.attrs and (item['class'] == ['navi-change-chapter-btn'] or item['class'] == ['btn-navigation-chap'])
    return bool

def ClasseNextListe(tag):
    bool = False
    bool = 'class' in tag.attrs  and (tag['class'] ==['navi-change-chapter-btn-next','a-h'] or tag['class'] == ['next'])
    return bool

