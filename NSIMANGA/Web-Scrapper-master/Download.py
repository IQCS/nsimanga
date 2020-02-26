import requests               #On importe le module requests
import urllib.request         #On importe le module request d'urrlib
import os                     #On importe le module os
from PIL import Image         #On importe la méthode Image du module PIL
import shutil                 #On importe le module shutil
if __name__ == '__main__':    #Cette ligne permet que le script soit executé seulement si le fichier "Download.py" est éxécuté et pas s'il est importé dans un autre script
    def dossier():            #On crée la fonction dossier qui ne prend pas d'arguments
        os.chdir("Google Drive//Python//Web-Scrapper")   #On change de dossier pour se diriger dans le fichier Google drive/Python/Web-scrapper

    dossier()                 #On execute la fonction dossier
import MangaFoxScrapper as MF   #On importe le script "MangaFoxScrapper.py" qu'on pourra appeler avec la commande MF
import MangaLeno as ML          #On importe le script "MangaenoL.py" qu'on pourra appeler avec la commande ML
import MangaReaderScrapper as MR  #On importe le script "MangaReaderScrapper.py" qu'on pourra appeler avec la commande MR
import MangaZuki as MZ          #On importe le script "MangaZuki.py" qu'on pourra appeler avec la commande MZ



path = r"C:\Users\Utilisateur\Desktop\Manga Scrapper" #On crée la variable "path" (=chemin) qui mène au ficher "Manga Scrapper" (ici "r" sert à utiliser des caractères tels que des antislash (\) )

def Download(download_url,name):             #On crée la fonction Download qui prend en arguments download_url et name
    if download_url != "Fin du Manga":       #On crée un Booléen : Si l'url n'est pas égal à "Fin du Manga"
        if download_url != "https://s3.mangareader.net/images/erogesopt.jpg":  #Et qu'il n'est pas une publicité
            #On fait une requête et on cache le fait que l'on est un robot
            req = urllib.request.Request(download_url, headers={'User-Agent': 'Mozilla/5.0'})

            #on prend le content de la page en bytes
            web_byte = urllib.request.urlopen(req).read()

            #on écrit le content dans un fichier test et on lui file le bon format
            open(name + '.jpg','wb').write(web_byte)


def Compression():            #On crée la fonction Compression qui ne prend aucun argument
    os.mkdir("Compr")         #On crée le sous-dossier "Compr"
    ListeNon = []             #On crée une liste vide pour tous les téléchargements qui ont échoués
    for elt in os.listdir():  #Pour tous les éléments présent dans le dossier actif
        try:                  #On essaye d'executer les commandes suivantes s'il n'y a pas d'exeption
            print(elt)        #On affiche le nom de l'élément
            im = Image.open(elt)  #On attribue à la variable im l'image ouverte de chaque élément
            im.save("Compr/" + elt,quality = 50, optimize = True)   #On enregistre chaque image sous une certaine qualité dans le sous-dossier Compr avec son nom.
        except:   #Si il y'a un problème
            try:     #On rééssaye
                shutil.copy(elt,"Compr/" + elt)  #Avec une autre méthode moins détaillé (on ne choisit pas la qualité et on "n'optimise" pas)
            except:                              #Si cela ne marche toujours pas
                print("Erreur pour elt")         #On affiche qu'il y a une erreur
                ListeNon.append(elt)             #Et on ajoute l'élément dans la liste des éléments qui n'ont pas pu êtres téléchargés
    return ListeNon                              #On renvoie la liste des erreurs


def ParcourSoup(urldebut):                       #On crée la fonction ParcourSoup qui prend urldebut comme argument
    url = urldebut                               #On attribue la valeur de l'argument à la variable url
    u = 0                                        #On crée la variable u de type int  = 0
    while url != "Fin du Manga":                 #Tant qu'on est pas arrivé à la fin du manga
        [soup,ListeLiens] = Navigate(url)        #
        i = 0                                    #On crée la variable i = 0
        for urldown in ListeLiens:               #Pour tous les urldown dans ListeLiens
            Download(urldown,str(u) + str(i))    #On télécharge l'urldown et on lui donne le nom string de i + string de u (donc au début "00")
            i += 1                               #On ajoute 1 à i
        url = Next(soup,url)                     #On attribue à url la méthode Next avec pour arguments soup et url
        u+=1000                                  #On ajoute 1000 à u


class Site:                                      #On crée la classe Site
    def __init__(self,url,Titre):                #On crée la fonction constructrice prenant comme arguments self, url et Titre.
        self.url = url                           #On attribut l'argument url à l'attribut de la classe self.url
        self.soup = ""                           #On crée l'attribut soup ( un string vide )
        self.ListeLiens = []                     #On crée l'attribue ListeLiens ( Une liste vide)
        self.Titre = Titre                       #On crée l'attribut Titre qui a pour valeur l'argument Titre
        self.chapter = ""                        #On crée l'attribut chapter (string vide)
        self.compteur = 0                        #On crée l'attribut compteur, un entier égal à 0


    def Initialisation(self):                    #On crée la méthode Initialisation qui prend comme argument self
        os.chdir(path)                           #On se dirige dans le dossier voulu (défini plus tôt par path
        if self.Titre not in os.listdir():       #S'il n'existe pas déjà un dossier du meme nom que le titre,
            os.mkdir(self.Titre)                 #On en crée un
        os.chdir(self.Titre)                     #On rentre dans ce dossier
        with open('Titre.txt','w+') as file:     #On Crée/Ouvre Le ficher Titre.txt avec la methode w+
            file.write(self.Titre)               #Et on y écrit le Titre


    def Navigate(self):                                           #On crée la méthode Navigate
        if 'mangafox' in self.url:                                #Si "mangafox" est présent dans l'url
            [self.soup,self.ListeLiens] = MF.Navigate(self.url)   #On utilise la fonction navigate de MangaFoxScrapper.py
        if 'manganelo' in self.url or 'mangakakalot' in self.url: #Si "mangaleno" est présent dans l'url
            [self.soup,self.ListeLiens] = ML.Navigate(self.url)   #On utilise la fonction navigate de MangaLeno.py
        if 'mangareader' in self.url:                             #Si "mangareader" est présent dans l'url
            [self.soup,self.ListeLiens] = MR.Navigate(self.url)   #On utilise la fonction navigate de MangaReaderScrapper.py
        if 'mangazuki' in self.url:                               #Si "mangazuki" est présent dans l'url
            [self.soup,self.ListeLiens] = MZ.Navigate(self.url)   #On utilise la fonction navigate de MangaZuki.py


    def Next(self):                                               #On crée la méthode Next qui prend comme argument self
        if self.url != "Fin du Manga":  #A tester                  Si l'url n'est pas égal à Fin du Manga
            with open("LastUrl.txt","w+") as file:                #On ouvre ou crée/ouvre le fichier texte LastUrl.txt en tant que "file" avec la methode w+
                file.write(self.url)                              #On y écrit le dernier url traité(correspondant à self.url)
        if 'mangafox' in self.url:                                #S'il y a mangafox dans l'url
            self.url = MF.Next(self.soup)                         #On utilise la fonction Next de MangaFoxScrapper.py
        if 'manganelo' in self.url or 'mangakakalot' in self.url: #S'il y a mangaleno ou mangakakalot dans l'url
            self.url = ML.Next(self.soup)                         #On utilise la fonction Next de MangaLeno.py
        if 'mangareader' in self.url:                             #S'il y a mangareader dans l'url
            self.url = MR.Next(self.soup)                         #On utilise la fonction Next de MangaReaderScrapper.py
        if 'mangazuki' in self.url:                               #S'il y a mangazuki dans l'url
            self.url = MZ.Next(self.soup)                         #On utilise la fonction Next de MangaZuki.py


    def Chapter(self):                                            #On crée la méthode Chapter qui prend comme argument self
        if 'mangafox' in self.url:                                #S'il y a mangafox dans l'url
            n = self.url.find('/chapter')                         #
            m = self.url[n+1:].find('-')                          #
            self.chapter = self.url[n+1:n+m+3]                    #
        if 'manganelo' in self.url or 'mangakakalot' in self.url: #S'il y a mangaleno dans l'url
            n = self.url.find("/chapter")                         #
            m = self.url[n+1:].find('/c')                         #
            self.chapter = url[n+m+2:]                            #
        if 'mangareader' in self.url:                             #S'il y a mangareader dans l'url
            n= self.url.find('reader')                            #
            m=url[n:].find('/')                                   #
            l = url[n+m+1:].find('/')                             #
            k = url[n+m+1+l+1:].find('/')                         #
            nom = self.url[n+m+1:m+n+k+l+2]                       #
            nom.replace('/','_')                                  #
            self.url = nom                                        #
        if 'mangazuki' in self.url:                               #S'il y a mangazuki dans l'url
            n = self.url.find("chapter")                          #
            self.chapter = self.url[n:-1]                         #

    def DownloadListe(self):                                      #On crée la méthode DownloadListe qui prend comme argument self
        for lien in self.ListeLiens:                              #Pour tous les liens dans la liste de Liens correspondant
            self.compteur +=1                                     #On ajoute au compteur 1
            Download(lien,f"{self.compteur:05d}")                 #On untilise la fonction Download avec le lien et comme nom

    def InitSoup(self):                                           #On crée la méthode InitSoup
        while self.url != "Fin du Manga":                         #Tant que l'url n'est pas "Fin du Manga"
            self.Navigate()                                       #On execute la méthode Navigate
            self.Initialisation()                                 #Puis la methode Initialisation
            self.DownloadListe()                                  #Puis la methode DownloadListe
            self.Next()                                           #Puis la methode next
    def ReprendreSoup(self):                                      #On crée la méthode ReprendreSoup qui ne prend comme argument self
        os.chdir(self.Titre)                                      #On se redirige dans le dossier portant le nom du titre
        self.Navigate()                                           #On execute la méthode Navigate
        self.Next()                                               #On execute la méthode Next
        while self.url != "Fin du Manga":                         #Tant que l'url n'est pas "Fin du Manga"
            self.Navigate()                                       #On execute la methode Navigate
            self.DownloadListe()                                  #Puis la methode DownloadListe
            self.Next()                                           #Puis la methode Next
        os.chdir("..")                                            #On remonte dans le dossier précédent



def Reprise():                                                    #On crée la fonction Reprise qui ne prend pas d'argument
    os.chdir(path)                                                #On se dirige dans le chemin correspondant à path (défini au début)
    ListeSite = []                                                #On crée la liste ListeSite vide
    for dossier in os.listdir():                                  #Pour chaque dossier présent dans le dossier où l'on se trouve
        if os.path.isdir(dossier):                                #S'il y a un dossier nommé comme lui
            os.chdir(dossier)                                     #On se dirige dans ce dossier
            with open("LastUrl.txt","r") as file:                 #Avec le fichier LastUrl.txt ouvert en tant que file
                url = file.read()                                 #On attribue à url ce qu'on y lit (donc le dernier url téléchargé)
            with open("Titre.txt","r") as file:                   #On fait pareil avec Titre.txt
                Titre = file.read()                               #On écrit le contenu dans la variable Titre
            Sitee = Site(url,Titre)                               #On attribue à la variable Sitee la classe Site avec pour arguments l'url et le titre qu'on vient d'attribuer
            ListeSite.append(Sitee)                               #On ajoute à ListeSite Sitee
            os.chdir("..")                                        #Et on remonte dans le cossier au dessus
    for site in ListeSite:                                        #Pour tous les sites dans ListeSite
        site.ReprendreSoup()                                      #On execute la fonction ReprendreSoup avec ce site
    return ListeSite                                              #On renvoie la ListeSite

def BoucleCompr():                                                #On crée la fonction BoucleCompr qui ne prend pas d'arguments
    os.chdir(path)                                                #On se dirige dans le chemin renseigné au début
    for dossier in os.listdir():                                  #Pour tous les dossiers dans le repertoire
        if os.path.isdir(dossier):                                #On cherche un dossier du meme nom
            os.chdir(dossier)                                     #On s'y dirige
            Compression()                                         #Et on y execute la methode Compression
            os.chdir("..")                                        #On remonte dans le dossier précédent
