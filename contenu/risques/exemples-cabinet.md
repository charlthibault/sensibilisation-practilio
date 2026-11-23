<!--
Source : recherche-attaques-sante.md § 1, 2 et 4
À écrire : Fiches d'attaques réelles (Cabinet libéral) : ce qui s'est passé, ce que ça veut dire pour vous, statut Confirmé / Revendiqué, menace de la matrice, sources.
Écrire en Markdown sous ce commentaire. Tant que le fichier est vide, le site affiche « À remplir ».
-->

> Dans un cabinet, l'attaquant ne vise pas votre cabinet en particulier : il cherche un compte facile à prendre. Sans personne chargée de la sécurité, tout se joue sur le mot de passe de chaque médecin, le poste de l'accueil et l'accès à distance de votre informaticien.


#### Cegedim : des comptes de médecins utilisés pour aspirer des dossiers patients

> **Confirmé** · Fin 2025 · France
>
> **1 500 comptes de médecins utilisés, 11 à 15 millions de dossiers estimés**

Voir dans la matrice : [Hameçonnage et compromission de comptes](#menace-cabinet-hameconnage)

Menace : attaquant non identifié · Vecteur : des comptes de médecins, avec des identifiants probablement volés

Ce qui s'est passé : des requêtes anormales sont parties des comptes de 1 500 médecins utilisateurs d'un logiciel de cabinet, MonLogicielMedical. Des dossiers patients ont été extraits, y compris les notes libres des médecins.

Dans votre cabinet : c'est votre logiciel de tous les jours, et ce sont des médecins comme vous dont les comptes ont servi. Les attaquants se sont simplement connectés avec ces comptes. Un portable de médecin infecté ou un mot de passe réutilisé suffit, et ce sont les dossiers de toute votre patientèle qui partent. C'est ensuite au cabinet de prévenir la CNIL.

<details>
<summary>Sources et détails</summary>

- Hypothèse dominante, non confirmée : identifiants volés (logiciel espion, hameçonnage, absence de double authentification).
- Ampleur estimée par France 2 : 11 à 15 millions de patients.
- Sources : [Caducée](https://www.caducee.net/actualite-medicale/16821/incident-mlm-chez-cegedim-anatomie-d-une-fuite-de-donnees-estimee-a-11-15-millions-de-dossiers-patients.html), [Le Monde Informatique](https://www.lemondeinformatique.fr/actualites/lire-le-piratage-du-logiciel-medical-de-cegedim-refait-surface-99493.html)

</details>

#### 1001RDV : un pirate revendique les données de 9 millions de patients

> **Revendiqué** · Novembre 2026 · France
>
> **9 millions de patients selon l'attaquant, non confirmé**

Voir dans la matrice : [Hameçonnage et compromission de comptes](#menace-cabinet-hameconnage)

Menace : un attaquant qui revendique le vol · Vecteur : non communiqué

Ce qui s'est passé : un attaquant affirme avoir volé les données de 9 millions de patients d'un logiciel de prise de rendez-vous médicaux (identité, coordonnées, numéro de sécurité sociale, rendez-vous). L'éditeur confirme seulement l'attaque de son site vitrine.

Dans votre cabinet : même non confirmée, une telle revendication suffit à alimenter des faux SMS et emails très crédibles (« confirmez votre rendez-vous chez le Dr X »), envoyés à vos patients comme à votre secrétariat. Restez vigilant sur les messages qui citent un vrai rendez-vous.

<details>
<summary>Sources et détails</summary>

- Revendication publiée en novembre 2026 ; l'éditeur (Logicielnet) reconnaît une attaque sur son site WordPress, pas sur les données de patients.
- Source : [Journal du Geek](https://www.journaldugeek.com/2026/11/16/donnees-medicales-9-millions-francais-volees-hacker-1001-rdv/)

</details>

#### Doctolib : des rendez-vous volés via des logiciels connectés

> **Confirmé** · Juillet 2020 · France
>
> **6 128 rendez-vous volés**

Voir dans la matrice : [Attaque par rebond via un prestataire](#menace-cabinet-prestataire)

Menace : attaquant non identifié · Vecteur : des logiciels tiers connectés à la plateforme

Ce qui s'est passé : en passant par des logiciels tiers connectés à la plateforme, des attaquants ont récupéré les données de 6 128 rendez-vous : nom, téléphone, email, date du rendez-vous, nom et spécialité du praticien.

Dans votre cabinet : vous reliez souvent plusieurs outils entre eux : agenda, logiciel médical, Practilio. Chaque connexion est une porte d'entrée que vous ne surveillez pas vous-même. Et même sans dossier médical, la liste de vos rendez-vous révèle des informations de santé (spécialité, fréquence des consultations).

<details>
<summary>Sources et détails</summary>

- Accès illégal par l'interface utilisée par des logiciels tiers connectés à la plateforme.
- Sources : [Next](https://next.ink/brief_article/doctolib-sest-fait-derober-les-informations-administratives-de-6-128-rendez-vous/), [Le Quotidien du Médecin](https://cardiologie.lequotidiendumedecin.fr/liberal/gestion-cabinet/doctolib-victime-dun-vol-de-donnees-portant-sur-plus-de-6-000-rendez-vous)

</details>
