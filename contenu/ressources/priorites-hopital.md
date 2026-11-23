<!--
Source : mapping-menaces-risques.md § Niveau 3 (geste prioritaire)
À écrire : Priorités (Hôpital public) : par quoi commencer, quel type d'interlocuteur solliciter.
Écrire en Markdown sous ce commentaire. Tant que le fichier est vide, le site affiche « À remplir ».
-->


À l'hôpital, trois risques sont critiques : le rançongiciel, l'accès illégitime aux dossiers et l'attaque sur les équipements connectés. Les premières mesures rejoignent les prérequis du programme CaRE, qui conditionne une partie des financements.

| # | Par quoi commencer | Contre quoi | Responsable |
|---|---|---|---|
| 1 | Double authentification pour les accès distants, les comptes d'administration et Practilio : c'est le point d'entrée de la plupart des attaques | [Vol de compte](risques.html#menace-hopital-hameconnage) | Practilio la propose, la DSI la déploie |
| 2 | Réduire l'exposition sur Internet et fermer les interconnexions oubliées (VPN, accès des mainteneurs) | [Équipements connectés](risques.html#menace-hopital-ot), [rebond via un prestataire](risques.html#menace-hopital-prestataire) | DSI, service biomédical et services techniques |
| 3 | Sauvegardes déconnectées et exercice de crise cyber pour préparer le fonctionnement en mode dégradé | [Rançongiciel](risques.html#menace-hopital-rancongiciel) | DSI et direction |
| 4 | Droits au plus juste et contrôle des traces de consultation des dossiers | [Accès illégitime](risques.html#menace-hopital-acces-illegitime) | DSI, DPO et encadrement des services |
| 5 | Inventorier et cloisonner le biomédical et la GTB | [Équipements connectés](risques.html#menace-hopital-ot) | DSI et service biomédical |

#### Qui solliciter

- En interne : le DPO, la DSI de l'établissement support du GHT, le service biomédical.
- Accompagnement public : l'ARS et le GRADeS de votre région (programme CaRE), le CERT Santé de l'ANS (voir [Acteurs publics](#acteurs)).
- Prestataires : un prestataire qualifié par l'ANSSI, ou une offre passée par une centrale d'achat du secteur (voir [Prestataires](#prestataires)).
- En cas d'attaque : voir [Incident : qui contacter](incident.html#interlocuteurs).
