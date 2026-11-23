<!--
Source : obligations-reglementaires-par-acteur.md ; anciens blocs archivés dans archive/obligations-v2/
À écrire : Restitution des textes applicables (Cabinet libéral) : droit commun / propre à la santé, ce que ça implique, première action. Points en évolution datés.
Écrire en Markdown sous ce commentaire. Tant que le fichier est vide, le site affiche « À remplir ».
-->

Un cabinet de 2 à 5 médecins n'est pas concerné par NIS 2. Le RGPD et les règles propres à la santé s'appliquent, elles, dès le premier patient.

#### Droit commun

| Texte | Ce que ça implique | Première action |
|---|---|---|
| [RGPD](https://eur-lex.europa.eu/eli/reg/2016/679/oj) | Le cabinet est responsable du traitement des données de ses patients, Practilio est son sous-traitant ([qui fait quoi](responsabilites.html#practilio)). Il faut une sécurité adaptée au risque, un registre des traitements et un contrat avec chaque prestataire. Une fuite de données se [notifie à la CNIL](https://www.cnil.fr/fr/notifier-une-violation-de-donnees-personnelles) sous 72 h. À cette taille, pas de DPO obligatoire, sauf pour un gros cabinet de groupe ou un centre de santé. | Remplir le registre des traitements et décider qui, au cabinet, notifie la CNIL. |
| [NIS 2](https://eur-lex.europa.eu/eli/dir/2022/2555/oj) | Hors champ : la directive exclut les micro et petites entreprises. | Aucune. |

#### Propre à la santé

| Texte | Ce que ça implique | Première action |
|---|---|---|
| Hébergement de données de santé (CSP, art. L1111-8) | Toute donnée de santé stockée hors du cabinet (logiciel en ligne, sauvegarde externe, Practilio) doit l'être chez un hébergeur certifié HDS ([ce que ça couvre](responsabilites.html#hds)). | Demander leur certificat HDS à vos prestataires. |
| [Identification électronique](https://esante.gouv.fr/faq/exigences-ie-cadre-reglementaire-de-l-identification-electronique) (PGSSI-S) | Les professionnels se connectent par [Pro Santé Connect](https://esante.gouv.fr/produits-services/pro-sante-connect) (carte CPS ou e-CPS) ou par une authentification forte. | e-CPS pour chaque médecin, double authentification pour le secrétariat. |
| Signalement des incidents graves (CSP, art. L1111-8-2) | Pas obligatoire pour un cabinet, mais un signalement sur le [portail](https://signalement.social-sante.gouv.fr/) donne accès à l'appui du [CERT Santé](https://esante.gouv.fr/securite/cert-sante). | Garder le lien du portail dans la fiche incident. |
| [Téléconsultation](https://esante.gouv.fr/produits-et-services/telesante/telemedecine/teleconsultation) (CSP, art. L6316-1), si vous en faites | Solution sécurisée, hébergée HDS, patient identifié avant l'échange. | Demander à votre éditeur où il en est du référentiel de l'ANS. |

> ⚠️ À surveiller, sources ANS consultées le 23/11/2026 :
>
> - Identification électronique : la version 2.0 du référentiel est en cours de publication, avec une échéance envisagée au 31/12/2026 pour les moyens de connexion autres que Pro Santé Connect.
> - Téléconsultation : le référentiel de l'ANS est opposable depuis le 14/02/2024 aux sociétés de téléconsultation ; son extension aux éditeurs utilisés en ville est annoncée, sans date.

Textes du Code de la santé publique (CSP) : [Légifrance](https://www.legifrance.gouv.fr/).
