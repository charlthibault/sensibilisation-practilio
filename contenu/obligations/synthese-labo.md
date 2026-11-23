<!--
Source : obligations-reglementaires-par-acteur.md ; anciens blocs archivés dans archive/obligations-v2/
À écrire : Restitution des textes applicables (Laboratoire de biologie) : droit commun / propre à la santé, ce que ça implique, première action. Points en évolution datés.
Écrire en Markdown sous ce commentaire. Tant que le fichier est vide, le site affiche « À remplir ».
-->

Un laboratoire multi-sites traite des données de santé à grande échelle et pilote des automates : il cumule le RGPD, probablement NIS 2, et deux obligations propres à la biologie.

#### Droit commun

| Texte | Ce que ça implique | Première action |
|---|---|---|
| [RGPD](https://eur-lex.europa.eu/eli/reg/2016/679/oj) | Le laboratoire est responsable du traitement sur tous ses sites (SIL, serveur de résultats, prise de rendez-vous), Practilio est sous-traitant. Traitement à grande échelle : DPO obligatoire et analyse d'impact. Une fuite se [notifie à la CNIL](https://www.cnil.fr/fr/notifier-une-violation-de-donnees-personnelles) sous 72 h. | Désigner le DPO et lancer l'analyse d'impact, en commençant par les résultats en ligne. |
| [NIS 2](https://eur-lex.europa.eu/eli/dir/2022/2555/oj) | À partir de 50 salariés ou 10 M€ de chiffre d'affaires (chiffres du groupe si vous en faites partie), le laboratoire deviendrait probablement entité importante ou essentielle : gestion des risques, signalement des incidents, responsabilité de la direction. En dessous, en principe hors champ. | Vérifier vos chiffres et suivre la transposition (ci-dessous). |

#### Propre à la santé

| Texte | Ce que ça implique | Première action |
|---|---|---|
| Hébergement de données de santé (CSP, art. L1111-8) | Toute donnée de santé stockée hors du laboratoire doit l'être chez un hébergeur certifié HDS ([ce que ça couvre](responsabilites.html#hds)). | Demander leur certificat HDS à vos prestataires. |
| [Identification électronique](https://esante.gouv.fr/faq/exigences-ie-cadre-reglementaire-de-l-identification-electronique) (PGSSI-S) | Connexion par [Pro Santé Connect](https://esante.gouv.fr/produits-services/pro-sante-connect) ou par une authentification forte. | Pro Santé Connect ou double authentification pour tout le personnel, sur tous les sites. |
| Signalement des incidents graves (CSP, art. L1111-8-2 ; décret n° 2016-1214) | Obligatoire, sur le [portail des signalements](https://signalement.social-sante.gouv.fr/). Le [CERT Santé](https://esante.gouv.fr/securite/cert-sante) apporte ensuite son appui. | Désigner qui signale, sur chaque site. |
| [Accréditation COFRAC](https://www.has-sante.fr/jcms/c_2811553/fr/accreditation-en-biologie-medicale) (ISO 15189) | La norme impose de maîtriser le système d'information : SIL, middleware, automates, sauvegarde. Une attaque du SIL devient aussi un problème de qualité. | Ajouter le scénario « SIL indisponible » au système qualité. |
| [Réactovigilance](https://ansm.sante.fr/documents/reference/cybersecurite-des-dm-et-dmdiv) (ANSM) | Automates et réactifs sont des dispositifs de diagnostic in vitro : un incident qui fausse des résultats, attaque informatique comprise, se signale à l'ANSM et au fabricant. Il n'y a pas de canal ANSM dédié au cyber. | Prévoir qui déclare, et inventorier les télémaintenances des fabricants. |

> ⚠️ À surveiller, sources consultées le 23/11/2026 :
>
> - NIS 2 : la loi « Résilience », qui la transpose en France, a été adoptée au Sénat le 12/03/2025 et à l'Assemblée nationale en première lecture le 17/11/2026 ; une commission mixte paritaire doit encore se réunir. Le rattachement des laboratoires au secteur « santé » reste à confirmer. Sources : [IT for Business](https://www.itforbusiness.fr/loi-resilience-nis-2-assemblee-adopte-110073), [MDP Data](https://mdp-data.com/transposition-nis2-france-loi-resilience/), [Pilote NIS2](https://www.pilote-nis2.fr/guides/loi-resilience-nis2-france).
> - Identification électronique : version 2.0 du référentiel en cours de publication, échéance envisagée au 31/12/2026 pour les moyens autres que Pro Santé Connect (ANS).

Textes du Code de la santé publique (CSP) : [Légifrance](https://www.legifrance.gouv.fr/).
