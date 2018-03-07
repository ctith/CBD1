# TP Hive avec HiveQL :notes::notes::notes:

## Fichier csv "Fête de la musique" : 26 colonnes, 3761 lignes 

### Transfert du fichier local vers ubuntu aws
```
ctith:/$ sudo scp -r -i Clé_AWS.pem /path_local/fete_musique.csv ubuntu@IP_public_AWS:/home/ubuntu
```

### Création d'une database "culturedb" sur Hive
```
CREATE DATABASE IF NOT EXISTS culturedb;
```

### Création d'une table "fete_musique" dans la database "culturedb" sur Hive
```
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
```
alter table fete_musique set SERDEPROPERTIES ('field.delim' = '\;');
LOAD DATA LOCAL INPATH '/home/ubuntu/fete_musique.csv' OVERWRITE INTO TABLE fete_musique ;
```

## Requêtes HiveQL

### Voir les requêtes en cours sur YARN
```
ubuntu@:~$ yarn application -list
```

### Afficher toutes les fêtes commençant le 22 juin
```
SELECT titre,adresse, ville, first_date FROM fete_musique WHERE first_date='22/06/2017';
```

### Afficher toutes les fêtes à entrées gratuites
```
SELECT titre, billetterie, adresse, ville, first_date FROM fete_musique WHERE billetterie RLIKE 'Gratuit';
```

### Afficher toutes les fêtes avec du jazz en programmation
```
SELECT titre, adresse, ville, keywords FROM fete_musique WHERE description RLIKE 'jazz';
```

### Nombre de ville fêtant la fête de la musique
```
SELECT ville FROM fete_musique GROUP BY ville;
```

### Adresse des fêtes ayant de la musique classique en programmation
```
SELECT titre,adresse, ville, keywords FROM fete_musique WHERE description RLIKE ‘classique’;
```

### Fêtes se déroulant au sein d'un arrondissement
```
SELECT titre, adresse, ville, city_district FROM fete_musique WHERE city_district RLIKE 'Arrondissement';
```

### Liste de fêtes se déroulant à Paris 5ème à partir de 20h
```
SELECT titre, adresse, ville, city_district,horaire_iso FROM fete_musique WHERE horaire_iso RLIKE '20' AND city_district RLIKE 'Paris 5e';
```

### Liste de fêtes se déroulant en Corse
```
SELECT titre, adresse, ville, region, horaire_iso FROM fete_musique WHERE region RLIKE 'Corse';
```
