# TP Hive avec HiveQL :musical_note::musical_score::guitar::postal_horn::violin::trumpet::microphone::saxophone::musical_note:

## Fichier csv "Fête de la musique" : 26 colonnes, 3761 lignes 

### Transfert du fichier local vers ubuntu aws
```
ctith:/$ sudo scp -r -i Clé_AWS.pem /path_local/fete_musique.csv ubuntu@IP_public_AWS:/home/ubuntu
```

### Création d'une database "culturedb" sur Hive
```SQL
CREATE DATABASE IF NOT EXISTS culturedb;
```

### Création d'une table "fete_musique" dans la database "culturedb" sur Hive
```SQL
CREATE TABLE IF NOT EXISTS culturedb.fete_musique ( 
identifiant INT, 
link STRING, 
maj STRING, 
informations STRING, 
image_url STRING, 
thumbnail_url STRING, 
share_url STRING, 
langue STRING,
titre STRING,
description STRING,
description_longue STRING,
coordonnees_geo STRING,
nom_site STRING,
adresse STRING,
region STRING,
departement STRING,
ville STRING,
keywords STRING, 
first_date STRING,
last_date STRING,
horaire_iso STRING,
billetterie STRING,
program_uid STRING,
pays STRING,
code_pays STRING,
city_district STRING); 
```

### Importer le csv selon le délimiteur ";"
```SQL
alter table fete_musique set SERDEPROPERTIES ('field.delim' = '\;');
LOAD DATA LOCAL INPATH '/home/ubuntu/fete_musique.csv' OVERWRITE INTO TABLE fete_musique ;
```

## Requêtes HiveQL

### Voir les requêtes en cours sur YARN
```
ubuntu@:~$ yarn application -list
```
![alt text](https://github.com/ctith/CBD1/blob/master/hive%20status.PNG?raw=true)

### Afficher toutes les fêtes commençant le 22 juin
```SQL
SELECT titre,adresse, ville, first_date FROM fete_musique WHERE first_date='22/06/2017';
```
![alt text](https://github.com/ctith/CBD1/blob/master/f%C3%AAte%20le%2022.PNG?raw=true)

### Afficher toutes les fêtes à entrées gratuites
```SQL
SELECT titre, billetterie, adresse, ville, first_date FROM fete_musique WHERE billetterie RLIKE 'Gratuit';
```
![alt text](https://github.com/ctith/CBD1/blob/master/fete%20gratuite.PNG?raw=true)

### Afficher toutes les fêtes avec du jazz en programmation
```SQL
SELECT titre, adresse, ville, keywords FROM fete_musique WHERE description RLIKE 'jazz';
```
![alt text](https://github.com/ctith/CBD1/blob/master/jazz.PNG?raw=true)
![alt text](https://github.com/ctith/CBD1/blob/master/f%C3%AAte%20jazz%20par%20ville.png?raw=true)


### Nombre de ville fêtant la fête de la musique
```SQL
SELECT ville FROM fete_musique GROUP BY ville;
```
![alt text](https://github.com/ctith/CBD1/blob/master/group%20by%20ville.PNG?raw=true)

### Adresse des fêtes ayant de la musique classique en programmation
```SQL
SELECT titre,adresse, ville, keywords FROM fete_musique WHERE description RLIKE ‘classique’;
```
![alt text](https://github.com/ctith/CBD1/blob/master/classique.PNG?raw=true)

### Fêtes se déroulant au sein d'un arrondissement
```SQL
SELECT titre, adresse, ville, city_district FROM fete_musique WHERE city_district RLIKE 'Arrondissement';
```
![alt text](https://github.com/ctith/CBD1/blob/master/arrondissement.PNG?raw=true)
![alt text](https://github.com/ctith/CBD1/blob/master/arrondissement_graph.PNG?raw=true)

### Liste de fêtes se déroulant à Paris 5ème à partir de 20h
```SQL
SELECT titre, adresse, ville, city_district,horaire_iso FROM fete_musique WHERE horaire_iso RLIKE '20' AND city_district RLIKE 'Paris 5e';
```
![alt text](https://github.com/ctith/CBD1/blob/master/fete%20paris5%2020h.PNG?raw=true)

### Liste de fêtes se déroulant en Corse
```SQL
SELECT titre, adresse, ville, region, horaire_iso FROM fete_musique WHERE region RLIKE 'Corse';
```
![alt text](https://github.com/ctith/CBD1/blob/master/corse.PNG?raw=true)
