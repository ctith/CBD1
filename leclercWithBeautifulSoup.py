import requests
from bs4 import BeautifulSoup
import csv

# page web bifidus actif de leclerc
url = "http://www.e-leclerc.com/catalogue/marques-distributeurs/marque-repere/alimentaire/frais/cremerie-LS/ultra-frais/lait-fermente-au-bifidus-nature-acti-fidus---4-x-125-g,77045"

"""
<div class="prod-data">
    <div class="prod-data-header">
        <div class="prod-marque"></div>
        <h1 class="prod-title" itemprop="name model">Lait fermente au bifidus nature acti-fidus - 4 x 125 g</h1>
        <div class="prod-price">
            <strong>0,80</strong>
            <span>1,60 / Kilo</span>
<!--        <p class="ecoPart" th:if="${produit.ecoTaxe != null}" th:text="#{produit.libelle.ecotaxe(${produit.ecoTaxe})}"></p> -->
        </div>
    </div>
"""

# Recupere reponse HTTP GET du site
r = requests.get(url)

# verification du code renvoye par le server
def statusServer(status):
    switcher = {
        200 : "succes de la requete",
        301 : "redirection permanente",
        302 : "redirection temporaire",
        401 : "utilisateur non authentifie",
        403 : "acces refuse",
        404 : "page non trouvee",
        500 : "erreur serveur",
        503 : "erreur serveur",
        504 : "le serveur n'a pas repondu"
    }
    print "Le serveur nous renvoie le code {} = ".format(r.status_code, url) + switcher.get(status, "erreur inconnue")

statusServer(r.status_code)

# transformer html en dom
dom = BeautifulSoup(r.text, "html.parser")

# recuperer ligne html qui nous interesse
listeProduit = dom.find_all("div", "prod-data")

# recuperer info dans le bloc html qui nous interesse
for produit in listeProduit:
    nomProduit = produit.find("h1","prod-title").text.strip().encode("utf-8")
    prixProduit = produit.find("div","prod-price").text.strip().encode("utf-8")
    print "{} vaut {}".format(nomProduit, prixProduit)
