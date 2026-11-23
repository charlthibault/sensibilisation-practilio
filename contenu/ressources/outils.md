<!--
Source : à rechercher et vérifier
À écrire : Un tableau : au moins 5 catégories (EDR/XDR, IAM/MFA, sauvegarde, scan de vulnérabilités, MDM…), chacune avec au moins 3 éditeurs ou technologies.
Écrire en Markdown sous ce commentaire. Tant que le fichier est vide, le site affiche « À remplir ».
-->

Un cabinet n'a pas besoin de tout : commencez par le gestionnaire de mots de passe, la double authentification et la sauvegarde. Les autres catégories concernent surtout un laboratoire ou un hôpital, avec une équipe informatique pour les exploiter.

| Type d'outil | À quoi ça sert | Exemples d'éditeurs ou de technologies |
|---|---|---|
| Gestionnaire de mots de passe | Un coffre-fort qui retient un mot de passe différent pour chaque logiciel : vous n'en retenez plus qu'un. | LockSelf (LockPass), éditeur français ; KeePass / KeePassXC, logiciel libre ; Bitwarden |
| Double authentification et gestion des comptes (MFA, IAM) | Un mot de passe volé ne suffit plus : il faut aussi la carte, le téléphone ou une clé. | Carte CPS et e-CPS avec Pro Santé Connect (santé, ANS) ; Microsoft Entra ID ; Okta ; Cisco Duo |
| Surveillance de l'exposition sur Internet (EASM) | Repérer ce que votre structure expose sur Internet sans le savoir : accès distants, serveurs oubliés, logiciels pas à jour. | Patrowl, éditeur français ; Microsoft Defender External Attack Surface Management ; Tenable Attack Surface Management ; Censys |
| Sauvegarde | La seule vraie parade au rançongiciel : pouvoir tout remettre en état sans payer. | Veeam ; Atempo, éditeur français ; Acronis |
| Protection des postes et serveurs (EDR, XDR) | Un « super antivirus » qui repère un comportement anormal et isole le poste à distance. | HarfangLab, éditeur français ; Microsoft Defender for Endpoint ; CrowdStrike Falcon ; SentinelOne |
| Filtrage de la messagerie et anti-hameçonnage | Le courriel reste la porte d'entrée la plus fréquente. | Mailinblack, éditeur français ; Proofpoint ; Microsoft Defender for Office 365 |
| Recherche de vulnérabilités | Savoir ce qui n'est pas à jour à l'intérieur du réseau. | Tenable (Nessus) ; Qualys ; Greenbone (OpenVAS), logiciel libre |
| Gestion des appareils mobiles (MDM) | Garder la main sur les téléphones et tablettes qui accèdent aux données. | Microsoft Intune ; Jamf (appareils Apple) ; Ivanti |

> Liste relevée le 23/11/2026, sans ordre de préférence.
