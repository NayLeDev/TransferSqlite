# Script de transfert de données de SQLite vers MySQL

Ce script Python permet de transférer des données d'une base de données SQLite vers une base de données MySQL.

## Utilisation

1. Assurez-vous d'avoir Python installé sur votre système.
2. Téléchargez le script `transfer_sqlite_to_mysql.py`.
3. Exécutez le script à l'aide de Python.
4. Suivez les instructions pour entrer le nom du fichier de la base de données SQLite.
5. Entrez les informations de connexion pour la base de données MySQL lorsque vous y êtes invité.

## Fonctionnalités

- Le script prend en charge la conversion de toutes les tables et données de la base de données SQLite.
- Il utilise les modules `sqlite3` et `pymysql` pour la gestion des connexions aux bases de données.
- L'interface utilisateur utilise une fonction de saisie progressive pour améliorer l'expérience utilisateur.

## Prérequis

- Python 3.x
- Accès à une base de données MySQL
- Accès à un fichier de base de données SQLite à transférer

## Installation des dépendances

Vous pouvez installer les dépendances requises à l'aide de pip :

```
pip install pymysql
```

## Exemple d'utilisation

Voici un exemple d'utilisation du script :

```bash
python transfer_sqlite_to_mysql.py
```

## Remarques

- Assurez-vous d'avoir les permissions nécessaires pour accéder aux bases de données SQLite et MySQL.
- Les informations de connexion à la base de données MySQL doivent être fournies lors de l'exécution du script.
- Ce script est fourni tel quel, sans aucune garantie.
- Pour toute question ou suggestion, veuillez ouvrir une issue sur ce dépôt.

## Auteurs

- [Nay](https://github.com/NayLeDev/)

## Licence

Ce projet est sous licence [MIT](LICENSE).
