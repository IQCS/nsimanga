import requests                 #On importe le module requests
import urllib.request           #On importe le module urllib.request
import time                     #On importe le module time
from bs4 import BeautifulSoup   #On importe le module BeautifulSoup de bs4
import os                       #On importe le module os

if __name__ == '__main__':    #Cette ligne permet que le script soit executé seulement si le fichier "Download.py" est éxécuté et pas s'il est importé dans un autre script
    def dossier():            #On crée la fonction dossier qui ne prend pas d'arguments
        os.chdir("Google Drive//Python//Web-Scrapper")  #On change de dossier pour se diriger dans le fichier Google drive/Python/Web-scrapper

    dossier()  #On execute la fonction dossier



#Ne marche que sur MangaReader


"""

Initialisation

"""

path = r"C:\Users\Utilisateur\Desktop\Manga Scrapper"        #On définit le chemin
CompteurParcours = 0                                         #On définit le Compteur parcours qui sera égal à 0
Titre = "Manga2"                                       #On définit le titre "Manga2"
url = "https://ww3.mangafox.online/the-top-clan-leader-in-history/chapter-74-1192366631948209"  #On définit l'url

"""

Navigation dans la page Web

"""


url = "https://ww3.mangafox.online/favorite-part/chapter-1-324246019529673"  #On redéfinit un url




"""

Recherche de l'image dans la page web

"""

def Navigate(url):                                                #On crée la fonction Navigate qui prend comme argument url
    if url != "Fin du Manga":                                 #Tant que l'url n'est pas Fin du Manga
        response = requests.get(url)                          #On fait une requête pour avoir l'url
        soup = BeautifulSoup(response.text, "html.parser")    #On utilise le module BeatifulSoup pour avoir une reponse en texte avec la methode html.parser
        ListeLiens = RecupListeLiens(soup)                    #On attribue à ListeLiens les liens décupérés grace a la fonction RecupListeLiens
    return [soup, ListeLiens]                                 #On renvoie soup et ListeLiens

def RecupListeLiens(soup):                            #On crée la fonctionRecupListeLiens qui prend comme argument soup
    Img = soup.findAll('img')                         # On cherche toutes les images avec soup et on les mets dans image
    ListeLiens = []                                   #On crée la liste ListeLiens
    for item in Img:                                  #Pour tous les items dans Img
        if 'class' in item.attrs and item['class'] == ['load_img']:  # Si ce sont bien des images
            ListeLiens.append(item['src'])             #On ajoute leur source dans ListeLiens
    return ListeLiens                       #On renvoie ListeLiens







"""

Manga Fox : Suivant .find(class="next_prev") puis enfant btn"

Boucle sur les scr de class="list_img"

"""

def Next(soup):                                 #On crée la fonction Next qui prend comme argument soup
    trunk = "https://ww3.mangafox.online"       #On attribue à la variable trunk "https://ww3.mangafox.online"
    NextUrl = ""                                #On crée une variable string vide du nom de NextUrl
    A = soup.findAll('a')                       #On cherche tous les éléments de type 'a'
    L = []                                      #On crée une liste L vide
    for a in A:                                 #Pour tous les a trouvés
        if a.text == "Next":                    #Si le texte est Next
            NextUrl = a['href']                 #On attribue à NextUrl a[href]
    if NextUrl == "":                           #Si NextUrl est vide
        NextUrl = "Fin du Manga"                #NextUrl prend la valeur "Fin du Manga"
    print(NextUrl)                              #On affiche NextUrl
    return NextUrl                              #On renvoie NextUrl



