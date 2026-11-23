<!--
Source : recherche-attaques-sante.md § 1, 2 et 4
À écrire : Fiches d'attaques réelles (Hôpital public) : ce qui s'est passé, ce que ça veut dire pour vous, statut Confirmé / Revendiqué, menace de la matrice, sources.
Écrire en Markdown sous ce commentaire. Tant que le fichier est vide, le site affiche « À remplir ».
-->

> Dans un hôpital, la menace la plus lourde est l'arrêt des soins : par une attaque directe sur votre système d'information, ou par celle d'un prestataire dont vous dépendez. Avec de nombreux services, comptes et intervenants extérieurs, les points d'entrée sont nombreux.


#### Corbeil-Essonnes : rançongiciel puis publication des données

> **Confirmé** · Août 2022 · Corbeil-Essonnes
>
> **Patients transférés, opérations reportées, données publiées**

Voir dans la matrice : [Rançongiciel](#menace-hopital-rancongiciel)

Menace : le groupe cybercriminel LockBit · Vecteur : non précisé dans les sources

Ce qui s'est passé : le groupe LockBit a chiffré les systèmes du Centre hospitalier Sud Francilien. L'hôpital a refusé de payer, a transféré des patients et a reporté des opérations. Un mois plus tard, des données de patients, de personnels et de partenaires ont été publiées.

Dans votre hôpital : c'est un hôpital public français, comparable au vôtre. Pour les équipes, c'est le retour au fonctionnement sans informatique : patients transférés, opérations reportées. Puis la fuite des données expose patients et agents au chantage et à l'hameçonnage ciblé. Le mode dégradé se prépare avant l'attaque, pas pendant.

<details>
<summary>Sources et détails</summary>

- Rançongiciel LockBit 3.0, attaque le 21 août 2022, environ 11 Go publiés le 23 septembre 2022.
- Sources : [Le Monde Informatique](https://www.lemondeinformatique.fr/actualites/lire-piratage-du-ch-sud-francilien-de-corbeil-essonnes-des-donnees-sensibles-divulguees-88114.html), [Le Quotidien du Médecin](https://www.lequotidiendumedecin.fr/hopital/cyberattaque-de-corbeil-essonnes-les-pirates-divulguent-des-donnees-de-sante-volees-pour-exercer-un)

</details>

#### Synnovis : un prestataire attaqué, des hôpitaux à l'arrêt

> **Confirmé** · Juin 2024 · Londres
>
> **Plus de 800 opérations annulées en une semaine**

Voir dans la matrice : [Attaque par rebond via un prestataire](#menace-hopital-prestataire)

Menace : le groupe cybercriminel Qilin, chez un prestataire · Vecteur : non communiqué

Ce qui s'est passé : un rançongiciel a bloqué Synnovis, le prestataire d'analyses de biologie de plusieurs hôpitaux. Faute de résultats, plus de 800 opérations ont été annulées la semaine suivante. Des données de patients ont ensuite été publiées.

Dans votre hôpital : vous confiez la maintenance de vos automates et de votre imagerie à des prestataires, et vous dépendez d'autres partenaires pour vos soins. S'ils s'arrêtent, vos soins s'arrêtent aussi, sans que votre système ait été attaqué. Il faut savoir lesquels sont vitaux et comment travailler sans eux.

<details>
<summary>Sources et détails</summary>

- Rançongiciel attribué au groupe Qilin, environ 400 Go de données publiés.
- Plus de 900 000 personnes concernées (estimation). Retour à la normale fin 2024.
- Sources : [Security Affairs](https://securityaffairs.com/164541/cyber-crime/londol-hospitals-canceled-800-operations-ransomware.html), [Computer Weekly](https://www.computerweekly.com/news/366589583/Qilin-ransomware-gang-publishes-stolen-NHS-data-online)

</details>
