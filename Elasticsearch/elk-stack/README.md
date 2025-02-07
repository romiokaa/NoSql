# Déploiement de la Stack ELK avec Docker et Filebeat

Ce projet met en place une pile ELK (Elasticsearch, Logstash, Kibana et Filebeat) via Docker afin de collecter, traiter et visualiser les logs générés par une application Python.

## 📌 Prérequis

- Docker
- Docker Compose

## 🚀 Configuration des Services

### 1️⃣ Elasticsearch
- **Image** : `docker.elastic.co/elasticsearch/elasticsearch:7.11.1`
- **Ports** :
  - `9200` : API REST d'Elasticsearch
  - `9300` : Communication entre nœuds Elasticsearch
- **Configuration** :
  - `discovery.type=single-node` : Mode mononœud
  - `ES_JAVA_OPTS=-Xms1g -Xmx1g` : Allocation de mémoire Java
  - Désactivation de la sécurité (`xpack.security.enabled=false`)

### 2️⃣ Logstash
- **Image** : `docker.elastic.co/logstash/logstash:7.11.1`
- **Ports** :
  - `5044` : Réception des logs de Filebeat
  - `5045` : Port d'écoute de Logstash
  - `9600` : Monitoring de Logstash
- **Volumes** :
  - `./logstash/logstash.conf:/usr/share/logstash/pipeline/logstash.conf`
- **Dépendance** : Connecté à Elasticsearch

### 3️⃣ Kibana
- **Image** : `docker.elastic.co/kibana/kibana:7.11.1`
- **Port** : `5601` (interface web Kibana)
- **Configuration** :
  - Connexion à Elasticsearch (`ELASTICSEARCH_HOSTS=http://elasticsearch:9200`)

### 4️⃣ Filebeat
- **Image** : `docker.elastic.co/beats/filebeat:7.11.2`
- **Volumes** :
  - `./filebeat/filebeat.yml:/usr/share/filebeat/filebeat.yml`
  - `./logs:/logs`
- **Dépendances** : Envoie les logs à Logstash et Elasticsearch

### 🌐 Réseau
Tous les services sont interconnectés via un réseau Docker nommé `elk`.

## 📂 Fichiers de Configuration

### 🛠 `docker-compose.yml`
Décrit les services Elasticsearch, Logstash, Kibana et Filebeat.

### 📝 `send_logs.py`
Script Python simulant la génération de logs (`INFO`, `DEBUG`, `ERROR`).

### 📜 `filebeat.yml`
Configuration de Filebeat pour surveiller les logs locaux (`./logs/*.log`) et les envoyer à Logstash.

### 🔧 `logstash.conf`
Configuration de Logstash pour transformer et indexer les logs dans Elasticsearch.

## ▶️ Démarrage des Services

1. **Cloner le dépôt** :
   ```bash
   git clone <url-du-depot>
   cd <repertoire-du-depot>
   ```
2. **Démarrer les services** :
   ```bash
   docker-compose up -d
   ```
3. **Vérifier le statut des services** :
   - **Kibana** : [http://localhost:5601](http://localhost:5601)
   - **Elasticsearch** : [http://localhost:9200](http://localhost:9200)
   - **Logstash** : [http://localhost:9600](http://localhost:9600)

## 📡 Simulation de Logs

1. Exécutez le script Python pour générer et enregistrer des logs :
   ```bash
   python send_logs.py
   ```
2. Les logs sont collectés par Filebeat, envoyés à Logstash pour transformation, puis indexés dans Elasticsearch.

## 🛑 Arrêt des Services

Pour arrêter et supprimer tous les conteneurs :
```bash
docker-compose down
```

## ⚙️ Personnalisation
- Modifiez `filebeat.yml`, `logstash.conf` et `send_logs.py` selon vos besoins.
- Les logs sont stockés dans Elasticsearch sous l’index `python-logs-YYYY.MM.dd`.

## 📚 Documentation
- [Documentation Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html)
- [Documentation Logstash](https://www.elastic.co/guide/en/logstash/current/index.html)
- [Documentation Kibana](https://www.elastic.co/guide/en/kibana/current/index.html)
- [Documentation Filebeat](https://www.elastic.co/guide/en/beats/filebeat/current/index.html)

