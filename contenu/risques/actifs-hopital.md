<!--
Source : analyse-par-contexte.md ; mapping-menaces-risques.md ; portrait et version longue archivés dans archive/risques-v1/
À écrire : Portrait en deux lignes, puis actifs critiques (Hôpital public), IT et OT séparés.
Écrire en Markdown sous ce commentaire. Tant que le fichier est vide, le site affiche « À remplir ».
-->

Un hôpital public de taille moyenne, avec une DSI interne, un service biomédical et de nombreux prestataires qui maintiennent des équipements critiques pour les soins.

Ce sans quoi l'hôpital ne peut plus soigner normalement :

#### Informatique (IT)

- Le dossier patient informatisé, qui suit le patient d'un service à l'autre.
- Les résultats de biologie et les images, dont dépendent les décisions médicales.
- L'annuaire des comptes (Active Directory), très nombreux : soignants, administratifs, intérimaires, prestataires. C'est, avec les sauvegardes, la première cible d'un rançongiciel.
- Les sauvegardes, qui permettent de redémarrer après une attaque.
- Les rendez-vous et la téléconsultation, gérés avec Practilio, et les interconnexions avec le GHT.

#### Équipements (OT)

- Les équipements biomédicaux connectés : imagerie (radiologie, scanner), automates de biologie, monitoring.
- La gestion technique du bâtiment : chauffage, ventilation, électricité.
- La centrale de fluides médicaux (oxygène, vide, air médical).
- Les accès de télémaintenance des fabricants, souvent ouverts en permanence.
