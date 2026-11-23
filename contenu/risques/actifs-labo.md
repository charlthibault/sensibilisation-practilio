<!--
Source : analyse-par-contexte.md ; mapping-menaces-risques.md ; portrait et version longue archivés dans archive/risques-v1/
À écrire : Portrait en deux lignes, puis actifs critiques (Laboratoire de biologie), IT et OT séparés.
Écrire en Markdown sous ce commentaire. Tant que le fichier est vide, le site affiche « À remplir ».
-->

Un laboratoire réparti sur plusieurs sites de prélèvement, avec un plateau technique qui centralise les analyses. Une équipe informatique gère le réseau entre les sites ; les fabricants assurent la maintenance des automates, à distance.

Ce sans quoi le laboratoire ne peut plus rendre de résultats :

#### Informatique (IT)

- Les résultats d'analyses, transmis aux prescripteurs et mis à disposition des patients.
- Le logiciel du laboratoire (SIL) et la plateforme de résultats, reliée à Practilio.
- Le réseau entre les sites.
- Les comptes du personnel, nombreux et répartis sur tous les sites.
- L'agenda des prélèvements et les rappels envoyés par Practilio.

#### Équipements (OT)

- Les automates d'analyse et leur middleware. Si le plateau technique s'arrête, tous les sites s'arrêtent avec lui.
- La supervision des enceintes réfrigérées : un échantillon mal conservé est perdu et le prélèvement est à refaire.
- Les accès de télémaintenance des fabricants.
