# Stack ELK avec Docker

Ce dépôt permet de configurer une stack ELK (Elasticsearch, Logstash et Kibana) en utilisant Docker. Il est conçu pour collecter, traiter et visualiser les journaux générés par un serveur web.

## Prérequis

Avant de commencer, assurez-vous d'avoir installé :

- **Docker**
- **Docker Compose**

## Démarrage rapide

Suivez les étapes ci-dessous pour mettre en place et exécuter la stack ELK localement avec Docker.

### 1. Cloner le dépôt

```bash
git clone <url-du-depot>
cd <repertoire-du-depot>
```

### 2. Construire et lancer les conteneurs

Pour démarrer la stack, utilisez la commande suivante :

```bash
docker-compose up
```

Cela démarrera les trois services suivants :

- **Elasticsearch** : Le moteur de recherche et d’analyse des données.
- **Logstash** : Outil de collecte, d'analyse et d'envoi des journaux vers Elasticsearch.
- **Kibana** : Interface graphique pour visualiser les données stockées dans Elasticsearch.

### 3. Accéder aux services

- **Kibana** : Ouvrez votre navigateur et accédez à [http://localhost:5601](http://localhost:5601) pour l'interface web de Kibana.
- **Elasticsearch** : Accédez directement à [http://localhost:9200](http://localhost:9200) pour interagir ou faire des requêtes via l'API.
- **Logstash** : L'interface web de Logstash est disponible à [http://localhost:9600](http://localhost:9600).

### 4. Données des journaux

Cette configuration est prête à traiter les journaux d'un serveur web Apache, situés dans le fichier `./data/apache_logs.txt`. Logstash lira ce fichier, le traitera et enverra les données vers Elasticsearch pour indexation.

#### Configuration de Logstash

Le fichier de configuration `logstash.conf` est configuré pour :

- Analyser les journaux Apache au format combiné avec le filtre **grok**.
- Enrichir les journaux avec des informations géographiques grâce au filtre **geoip**.
- Indexer les journaux dans Elasticsearch sous l'index `web_server_logs`.

#### Configuration d'Elasticsearch

Le fichier `elasticsearch.yml` configure Elasticsearch pour qu'il fonctionne comme un cluster à nœud unique nommé `docker-cluster`, et expose le réseau sur toutes les interfaces (`0.0.0.0`).

#### Configuration du pipeline Logstash

Logstash lit le fichier `apache_logs.txt`, applique les filtres définis dans `logstash.conf`, et envoie les journaux traités à Elasticsearch pour les indexer.

### 5. Personnalisation de la configuration

- **Modifier les journaux Apache** : Changez le fichier `./data/apache_logs.txt` pour pointer vers vos propres fichiers de journaux Apache.
- **Personnaliser Logstash** : Modifiez le fichier `logstash.conf` pour ajuster le traitement des journaux ou adapter le format de sortie selon vos besoins.
- **Configurer Elasticsearch et Logstash** : Si nécessaire, ajustez les paramètres de performance ou de réseau dans les fichiers `elasticsearch.yml` et `logstash.yml`.

### 6. Arrêter les conteneurs

Pour arrêter les services en cours d'exécution, utilisez la commande suivante :

```bash
docker-compose down
```

### 7. Volumes et réseau

La configuration utilise un réseau Docker personnalisé nommé `dockerelk` et des montages de volumes pour les fichiers de configuration de Logstash et les journaux Apache.

- **Volumes** :
    - `./elasticsearch/elasticsearch.yml` : Configuration d'Elasticsearch.
    - `./logstash/logstash.yml` : Configuration de Logstash.
    - `./logstash/logstash.conf` : Configuration du pipeline d'entrée/sortie de Logstash.
    - `./web_server_logs/logstash-apache.conf` : Configuration supplémentaire de Logstash.
    - `./data/apache_logs.txt` : Fichier contenant vos journaux Apache.

### 8. Documentation complémentaire

Pour en savoir plus sur la configuration et la gestion de la stack ELK, consultez la documentation officielle :

- [Documentation Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/index.html)
- [Documentation Logstash](https://www.elastic.co/guide/en/logstash/index.html)
- [Documentation Kibana](https://www.elastic.co/guide/en/kibana/index.html)
```