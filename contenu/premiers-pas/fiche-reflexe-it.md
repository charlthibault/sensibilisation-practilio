<!--
Source : notes-sujet.md ; anciens blocs essentiel-* archivés dans archive/premiers-pas-v1/
À écrire : Fiche réflexe imprimable pour le profil Équipe IT, avec la raison de chaque geste en une ligne.
Écrire en Markdown sous ce commentaire. Tant que le fichier est vide, le site affiche « À remplir ».
-->

Référent interne, prestataire ou DSI : votre rôle est de réduire les portes d'entrée et de rendre un incident récupérable. Les points sont classés par effet sur les menaces de [la matrice](risques.html#vue-ensemble). À revoir à chaque intervention.

#### Hygiène

- ☐ L'inventaire des comptes (personnel, prestataires, comptes techniques) est à jour ; les comptes sans titulaire sont fermés.
- ☐ Aucun utilisateur n'est administrateur de son poste, et les comptes d'administration sont séparés des comptes de messagerie.
- ☐ Le personnel informatique n'a pas d'accès aux données de santé : il n'en a pas besoin pour travailler.
- ☐ La double authentification protège la messagerie, les accès distants, les consoles d'administration et les comptes Practilio. C'est la mesure qui bloque le plus de vols d'identifiants.
- ☐ Les mises à jour sont appliquées, en priorité sur ce qui est exposé à Internet (pare-feu, VPN, messagerie).
- ☐ Une sauvegarde est hors ligne ou non modifiable, et la dernière restauration testée date de moins d'un an. Un rançongiciel chiffre aussi les sauvegardes qu'il peut atteindre.
- ☐ Chaque VPN, outil de télémaintenance et interconnexion a un propriétaire, une raison d'exister et une date de revue. Ce qui ne sert plus est coupé.
- ☐ Les postes administratifs, les postes médicaux et les équipements biomédicaux sont sur des réseaux séparés, et aucun bureau à distance (RDP) n'est exposé directement sur Internet.
- ☐ Les journaux de connexion et d'administration sont conservés : sans eux, impossible de savoir ce qui a été touché.

#### En cas d'incident

- ☐ J'isole les postes touchés sans les éteindre.
- ☐ Je coupe les accès distants non indispensables.
- ☐ Je vérifie que les sauvegardes sont intactes avant de restaurer.
- ☐ Je préviens le responsable, et Practilio si ses comptes sont concernés ([comment](incident.html#practilio)).

Les outils pour chaque point : [catégories d'outils](ressources.html#outils).
