#coding: utf-8

import csv 
import json 
import requests 

deuxiemefichier = "liste2.csv"

fraise = open(deuxiemefichier, "w")

#Ceci est l'URL qui contient mon TOKEN et mon ID List de CrowdTangle
url= "https://api.crowdtangle.com/posts?token=PNaHsdzuYKReh2w5VHph6DMr7HWvOF7Fif0RQ6pd&listIds=1382545&count=100"

entetes = {
    "User-Agent":"Hi, my name is Sandrine and I'm using this for a school project",
    "from":"sandrinevieira2017@gmail.com"
}

req = requests.get(url,headers=entetes)

#assnat= req.json()
#print(assnat)

req = requests.get(url, headers=entetes)

if req.status_code !=200 : 
    print("Ça ne marche pas")
else: 
    assnat= req.json()
    for variable in assnat["result"]["posts"]:

        resultat = []
        nom = variable["account"]["name"]
        deputeid = variable["id"]
        ladate = variable["date"]
        try:
            publication = variable["message"]
        except:
            publication = "No Message"
        lienpubli = variable["link"]
        nblikes = variable["statistics"]["actual"]["likeCount"]

        #apend les valeurs dans la liste résultat
        resultat.append(nom)
        resultat.append(deputeid)
        resultat.append(ladate)
        resultat.append(publication)
        resultat.append(lienpubli)
        resultat.append(nblikes)
        #print(resultat)

        #Écriture du premier fichier csv
        framboise = csv.writer(fraise)
        framboise.writerow(resultat)

#Ceci est mon code pour append les nouveaux résultats de la liste 2 (résultats plus récents) dans mon csv d'origine.
with open('liste1.csv', 'r') as f1:
    original = f1.read()

with open('liste2.csv', 'a') as f2:
    f2.write('\n')
    f2.write(original)
