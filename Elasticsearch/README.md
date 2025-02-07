# Elasticsearch & Kibana avec Docker

## Description
Ce projet configure un environnement Docker pour Elasticsearch et Kibana en utilisant Docker Compose.

## Prérequis
- [Docker](https://www.docker.com/get-started) installé
- [Docker Compose](https://docs.docker.com/compose/install/) installé

## Installation
```sh
# Clonez ce dépôt
git clone <URL_DU_REPO>
cd <NOM_DU_REPO>

# Démarrez les conteneurs
docker-compose up -d
```

## Services
### Elasticsearch
- **Image** : `docker.elastic.co/elasticsearch/elasticsearch:7.6.2`
- **Accès** : `http://localhost:9200`
- **Données stockées** : `./elas1:/usr/share/elasticsearch/data`
- **Ports** :
  - `9200` (API Elasticsearch)
  - `9300` (Communication entre nœuds Elasticsearch)

### Kibana
- **Image** : `docker.elastic.co/kibana/kibana:7.6.2`
- **Accès** : `http://localhost:5601`
- **Dépendance** : Elasticsearch doit être en cours d'exécution
- **Port** : `5601`

## Configuration réseau
Les services communiquent via le réseau Docker nommé `esnet` utilisant le driver `bridge`.

## Gestion des conteneurs
```sh
# Démarrer les services
docker-compose up -d

# Arrêter les services
docker-compose down

# Vérifier les logs
docker-compose logs -f
```

## Sécurité
L'authentification et la sécurité X-Pack sont désactivées pour simplifier l'accès en développement.

## Licence
Ce projet est sous licence MIT. Voir `LICENSE` pour plus de détails.

