# Projet Elasticsearch, Logstash & Kibana avec Docker

Ce projet permet de configurer un environnement Elasticsearch, Logstash et Kibana (ELK) en utilisant Docker et Docker Compose. Elasticsearch sert de moteur de recherche et d'analyse, Logstash est utilisé pour l'ingestion des données, et Kibana fournit une interface de visualisation des données.

## 📌 Prérequis

Avant de commencer, assurez-vous d'avoir installé :

- **Docker**
- **Docker Compose**

## 🚀 Installation & Démarrage

### 1️⃣ Cloner le dépôt (si applicable)

```bash
git clone <url-du-dépôt>
cd <nom-du-dossier>
```

### 2️⃣ Lancer les conteneurs Docker

Pour démarrer la stack ELK, exécutez la commande suivante :

```bash
docker-compose up -d
```

Cette commande va :

- Télécharger et démarrer Elasticsearch (version 7.6.2)
- Télécharger et démarrer Logstash (version 7.6.2)
- Télécharger et démarrer Kibana (version 7.6.2)
- Créer un réseau Docker `dockerelk`
- Monter les fichiers de configuration de Logstash et Elasticsearch

### 3️⃣ Vérifier que tout fonctionne

Pour vérifier les logs des conteneurs, utilisez :

```bash
docker-compose logs -f
```

Pour afficher les conteneurs actifs, exécutez :

```bash
docker ps
```

### 4️⃣ Accéder à Kibana

Après quelques secondes, ouvrez votre navigateur et accédez à l'interface Kibana en visitant l'URL suivante :  
👉 [http://localhost:5601](http://localhost:5601)

## 📂 Structure du projet

```
.
├── docker-compose.yml   # Configuration Docker Compose
├── elasticsearch/       # Configuration d'Elasticsearch
│   └── elasticsearch.yml
├── logstash/            # Configuration de Logstash
│   ├── logstash.yml
│   ├── logstash.conf
│   └── logstash-json.conf
├── data/                # Fichiers de données pour ingestion
│   ├── data.csv
│   └── data-json.log
```

## 🛑 Arrêter et supprimer les conteneurs

Si vous souhaitez arrêter les services, exécutez :

```bash
docker-compose down
```

Cela arrêtera les conteneurs mais conservera les données.  
Si vous voulez tout supprimer (conteneurs, réseaux, volumes), utilisez :

```bash
docker-compose down -v
```

## 🔧 Configuration

### 🔹 Modifier la configuration de Logstash

Les fichiers de configuration de Logstash se trouvent dans le dossier `logstash/`.

#### Exemple de pipeline CSV (logstash.conf)

```plaintext
input {
  file {
    path => "/usr/share/logstash/external-data/data.csv"
    start_position => "beginning"
    sincedb_path => "/dev/null"
  }
}
filter {
  csv {
    columns => ["orderId", "orderGUID", "orderPaymentAmount", "orderDate", "orderPaymentType", "latitude", "longitude"]
  }
  mutate {
    convert => { "latitude" => "float" "longitude" => "float" }
  }
}
output {
  elasticsearch {
    hosts => "elasticsearch:9200"
    index => "csv-data"
  }
  stdout {}
}
```

#### Exemple de pipeline JSON (logstash-json.conf)

```plaintext
input {
  file {
    path => "/usr/share/logstash/external-data/data-json.log"
    start_position => "beginning"
    sincedb_path => "/dev/null"
  }
}
filter {
  json {
    source => "message"
  }
  mutate {
    remove_field => ["message", "host", "@timestamp", "path", "@version"]
  }
}
output {
  elasticsearch {
    hosts => "elasticsearch:9200"
    index => "json-data"
  }
  stdout {}
}
```

Après avoir modifié les fichiers de configuration, relancez les conteneurs avec :

```bash
docker-compose down && docker-compose up -d
```

## 📝 Notes

- Assurez-vous que les ports 9200 (Elasticsearch), 5601 (Kibana) et 9600 (Logstash) ne sont pas déjà utilisés sur votre machine.
- Si Kibana ne se connecte pas immédiatement, attendez quelques secondes puis rafraîchissez la page.
- Si vous rencontrez des problèmes, consultez les logs de Logstash pour identifier d'éventuelles erreurs de parsing.
```