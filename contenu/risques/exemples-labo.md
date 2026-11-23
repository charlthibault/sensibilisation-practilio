<!--
Source : recherche-attaques-sante.md § 1, 2 et 4
À écrire : Fiches d'attaques réelles (Laboratoire de biologie) : ce qui s'est passé, ce que ça veut dire pour vous, statut Confirmé / Revendiqué, menace de la matrice, sources.
Écrire en Markdown sous ce commentaire. Tant que le fichier est vide, le site affiche « À remplir ».
-->

> Dans un laboratoire multi-sites, deux risques dominent : un compte volé sur un seul site de prélèvement peut ouvrir les résultats de tous les sites, et un arrêt du centre d'analyse prive de résultats tous les soignants qui en dépendent.


#### Synnovis : un laboratoire paralysé, des hôpitaux à l'arrêt

> **Confirmé** · Juin 2024 · Londres
>
> **Plus de 800 opérations annulées en une semaine**

Voir dans la matrice : [Rançongiciel](#menace-labo-rancongiciel)

Menace : le groupe cybercriminel Qilin · Vecteur : non communiqué

Ce qui s'est passé : un rançongiciel a bloqué Synnovis, prestataire d'analyses de biologie de plusieurs hôpitaux. Faute de résultats, plus de 800 opérations ont été annulées la semaine suivante. Des données de patients ont ensuite été publiées.

Dans votre laboratoire : c'est le scénario le plus proche du vôtre. Si votre centre d'analyse s'arrête, tous les sites de prélèvement s'arrêtent avec lui, et les médecins, cliniques et hôpitaux qui attendent vos résultats retardent leurs soins. L'attaque d'un seul laboratoire a suffi à paralyser plusieurs hôpitaux.

<details>
<summary>Sources et détails</summary>

- Rançongiciel attribué au groupe Qilin, environ 400 Go de données publiés.
- Plus de 900 000 personnes concernées (estimation). Retour à la normale fin 2024.
- Sources : [Security Affairs](https://securityaffairs.com/164541/cyber-crime/londol-hospitals-canceled-800-operations-ransomware.html), [Computer Weekly](https://www.computerweekly.com/news/366589583/Qilin-ransomware-gang-publishes-stolen-NHS-data-online)

</details>

#### Cegedim : des comptes de médecins utilisés pour aspirer des dossiers patients

> **Confirmé** · Fin 2025 · France
>
> **1 500 comptes de médecins utilisés, 11 à 15 millions de dossiers estimés**

Voir dans la matrice : [Hameçonnage et compromission de comptes](#menace-labo-hameconnage)

Menace : attaquant non identifié · Vecteur : des comptes de médecins, avec des identifiants probablement volés

Ce qui s'est passé : des requêtes anormales sont parties des comptes de 1 500 médecins utilisateurs d'un logiciel médical, MonLogicielMedical. Des dossiers patients ont été extraits, y compris les notes libres des médecins.

Dans votre laboratoire : votre personnel se connecte depuis plusieurs sites à la plateforme de résultats, reliée à Practilio. Un seul compte volé, sur n'importe quel site de prélèvement, peut suffire à extraire les résultats de patients de tous les sites, sans intrusion technique visible.

<details>
<summary>Sources et détails</summary>

- Hypothèse dominante, non confirmée : identifiants volés (logiciel espion, hameçonnage, absence de double authentification).
- Ampleur estimée par France 2 : 11 à 15 millions de patients.
- Sources : [Caducée](https://www.caducee.net/actualite-medicale/16821/incident-mlm-chez-cegedim-anatomie-d-une-fuite-de-donnees-estimee-a-11-15-millions-de-dossiers-patients.html), [Le Monde Informatique](https://www.lemondeinformatique.fr/actualites/lire-le-piratage-du-logiciel-medical-de-cegedim-refait-surface-99493.html)

</details>
