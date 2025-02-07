# Elasticsearch - Setup et Analyse de Texte

## Installation et Configuration

### 1. Télécharger et exécuter Elasticsearch

```sh
docker pull docker.elastic.co/elasticsearch/elasticsearch:7.11.1

docker run -p 9200:9200 -p 9300:9300 -d -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.11.1
```

### 2. Installer le plugin `analysis-icu`

```sh
docker exec -it (nom ou id du container) bash
./bin/elasticsearch-plugin install analysis-icu
exit

docker restart (nom ou ID de ton container)
```

### 3. Vérifier l'installation des plugins

```sh
curl -X GET "http://localhost:9200/_cat/plugins?v"
```

### 4. Créer un index avec un analyzer français

```sh
curl -X PUT "http://localhost:9200/french" -H "Content-Type: application/json" -d '{
  "settings": {
    "analysis": {
      "filter": {
        "french_elision": {
          "type": "elision",
          "articles_case": true,
          "articles": ["l", "m", "t", "qu", "n", "s", "j", "d", "c", "jusqu", "quoiqu", "lorsqu", "puisqu"]
        },
        "french_synonym": {
          "type": "synonym",
          "ignore_case": true,
          "expand": true,
          "synonyms": [
            "réviser, étudier, bosser",
            "mayo, mayonnaise",
            "grille, toaste"
          ]
        },
        "french_stemmer": {
          "type": "stemmer",
          "language": "light_french"
        }
      },
      "analyzer": {
        "french_heavy": {
          "tokenizer": "icu_tokenizer",
          "filter": [
            "french_elision",
            "icu_folding",
            "french_synonym",
            "french_stemmer"
          ]
        },
        "french_light": {
          "tokenizer": "icu_tokenizer",
          "filter": [
            "french_elision",
            "icu_folding"
          ]
        }
      }
    }
  }
}'
```

## Exécution des scripts Python

### 1. `analyzer.py`

Ce script indexe un document dans Elasticsearch.

```sh
python3 analyzer.py
```

### 2. `analyzer_2.py`

Ce script analyse un texte avec l'index défini.

```sh
python3 analyzer_2.py
```

## Résumé

- Téléchargement et exécution d'Elasticsearch via Docker
- Installation du plugin `analysis-icu`
- Création d'un index avec un analyzer français
- Test des scripts Python pour l'indexation et l'analyse de texte

🚀 **Elasticsearch est maintenant prêt pour l'analyse de texte en français !**

