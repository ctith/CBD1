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



