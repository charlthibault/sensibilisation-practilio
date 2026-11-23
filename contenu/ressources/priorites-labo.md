<!--
Source : mapping-menaces-risques.md § Niveau 3 (geste prioritaire)
À écrire : Priorités (Laboratoire de biologie) : par quoi commencer, quel type d'interlocuteur solliciter.
Écrire en Markdown sous ce commentaire. Tant que le fichier est vide, le site affiche « À remplir ».
-->


Dans un laboratoire multi-sites, deux risques sont critiques : le vol de compte et le rançongiciel. Commencez par eux, puis traitez les accès des prestataires et du personnel.

| # | Par quoi commencer | Contre quoi | Responsable |
|---|---|---|---|
| 1 | Double authentification pour tout le personnel, sur tous les sites, et en priorité sur la plateforme de résultats | [Vol de compte](risques.html#menace-labo-hameconnage) | Practilio la propose, l'équipe IT la déploie |
| 2 | Sauvegardes déconnectées du réseau et plan de continuité si le centre d'analyse s'arrête | [Rançongiciel](risques.html#menace-labo-rancongiciel) | Équipe IT et direction du laboratoire |
| 3 | Cadrer la télémaintenance des automates : ouverte à la demande, nominative, tracée | [Rebond via un prestataire](risques.html#menace-labo-prestataire), [équipements connectés](risques.html#menace-labo-ot) | Équipe IT avec les fabricants |
| 4 | Retirer les accès le jour du départ, sur tous les sites et toutes les applications | [Accès illégitime](risques.html#menace-labo-acces-illegitime) | Ressources humaines et équipe IT |
| 5 | Contrôler les envois de résultats (destinataire, canal MSSanté) | [Fuite par erreur](risques.html#menace-labo-fuite) | Biologistes et secrétariat |

#### Qui solliciter

- En interne : le DPO du laboratoire, obligatoire pour une structure multi-sites, et le responsable qualité (l'accréditation COFRAC couvre aussi le système d'information).
- Pour se faire accompagner : un prestataire qualifié par l'ANSSI pour le service recherché, ou une offre du catalogue de l'ANS (voir [Prestataires](#prestataires)).
- Pour les automates : le fabricant, et l'ANSM en cas d'incident qui fausse des résultats.
- En cas d'attaque : voir [Incident : qui contacter](incident.html#interlocuteurs).
