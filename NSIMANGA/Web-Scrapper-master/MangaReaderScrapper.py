import requests                    #On importe le module requests
import urllib.request              #On importe le module urllib.request
import time                        #On importe le module time
from bs4 import BeautifulSoup      #On importe le module BeautifulSoup de bs4
import os                          #On importe le module os
if __name__ == '__main__':   #Cette ligne permet que le script soit executé seulement si le fichier "Download.py" est éxécuté et pas s'il est importé dans un autre script
    def dossier():           #On crée la fonction dossier qui ne prend pas d'arguments
        os.chdir("Google Drive//Python//Web-Scrapper")  #On change de dossier pour se diriger dans le fichier Google drive/Python/Web-scrapper
    dossier() #On execute la fonction dossier


#Ne marche que sur MangaReader


"""

Initialisation

"""

path = r"C:\Users\Utilisateur\Desktop\Manga Scrapper"
CompteurParcours = 0
Titre = "Manga"



"""

Navigation dans la page Web

"""

trunk = "https://www.mangareader.net"


url = trunk + "/tate-no-yuusha-no-nariagari/1/2"




"""

Recherche de l'image dans la page web

"""

def Navigate(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    if soup.text.find("is not released") <0:
        Im = soup.findAll('img')[0]
        link = Im['src']
        download_url = [link]
    else:
        print("Fin du manga")
        download_url = "Fin du Manga"
    return [soup, download_url]



def Next(soup):
    NextUrl = ""
    Div = soup.findAll("div")
    for item in Div:
        if 'id' in item.attrs and item['id'] == 'imgholder':
            NextUrl = trunk + item.a['href']
    if NextUrl == "":
        NextUrl = "Fin du Manga"
    print(NextUrl)
    return NextUrl







