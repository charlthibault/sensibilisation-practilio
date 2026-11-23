<!--
Source : obligations-reglementaires-par-acteur.md ; anciens blocs archivés dans archive/obligations-v2/
À écrire : Restitution des textes applicables (Hôpital public) : droit commun / propre à la santé, ce que ça implique, première action. Points en évolution datés.
Écrire en Markdown sous ce commentaire. Tant que le fichier est vide, le site affiche « À remplir ».
-->

Un hôpital public cumule les règles d'un organisme public, celles de NIS 2 et celles du secteur de la santé. C'est aussi le seul des trois contextes à pouvoir financer une partie de sa mise à niveau (programme CaRE).

#### Droit commun

| Texte | Ce que ça implique | Première action |
|---|---|---|
| [RGPD](https://eur-lex.europa.eu/eli/reg/2016/679/oj) | Organisme public : DPO obligatoire, analyses d'impact pour les traitements de santé. Une fuite se [notifie à la CNIL](https://www.cnil.fr/fr/notifier-une-violation-de-donnees-personnelles) sous 72 h. Les exigences de sécurité (HDS, clauses de sous-traitance, réversibilité) s'écrivent dans chaque marché passé avec un éditeur comme Practilio. | Associer le DPO dès le choix d'un nouvel outil. |
| [NIS 2](https://eur-lex.europa.eu/eli/dir/2022/2555/oj) | La plupart des centres hospitaliers seront entités essentielles : gestion des risques, alerte sous 24 h et notification sous 72 h des incidents, responsabilité de la direction. Un établissement déjà désigné OSE ou OIV applique déjà des règles de l'ANSSI. | Préparer la chaîne d'alerte entre RSSI, DPO et direction. |
| RGS (ordonnance n° 2005-1516) | Les téléservices ouverts aux usagers doivent être homologués avant leur mise en service. | Prévoir l'homologation de tout service ouvert aux patients. |

#### Propre à la santé

| Texte | Ce que ça implique | Première action |
|---|---|---|
| Hébergement de données de santé (CSP, art. L1111-8) | Toute donnée de santé stockée hors de l'établissement doit l'être chez un hébergeur certifié HDS ([ce que ça couvre](responsabilites.html#hds)). | Exiger le certificat dans chaque marché. |
| [Identification électronique](https://esante.gouv.fr/faq/exigences-ie-cadre-reglementaire-de-l-identification-electronique) (PGSSI-S) | Connexion par [Pro Santé Connect](https://esante.gouv.fr/produits-services/pro-sante-connect) ou par une authentification forte. | Double authentification sur les accès distants, les comptes d'administration et Practilio. |
| Signalement des incidents graves (CSP, art. L1111-8-2 ; décret n° 2016-1214) | Obligatoire, sur le [portail des signalements](https://signalement.social-sante.gouv.fr/), avec l'appui du [CERT Santé](https://esante.gouv.fr/securite/cert-sante). | L'intégrer à la procédure de crise. |
| [Certification HAS](https://www.has-sante.fr/jcms/p_3563407/fr/mettre-en-oeuvre-le-6e-cycle-de-certification) | Le référentiel inclut la maîtrise des risques, y compris numériques. | Rattacher le plan cyber au plan qualité. |
| [Programme CaRE](https://esante.gouv.fr/strategie-nationale/cybersecurite) (2023-2027) | Financement par l'ARS des établissements qui atteignent des prérequis : double authentification, maîtrise de l'exposition sur Internet, sauvegardes déconnectées, exercices de crise. | Faire le point avec l'ARS et le GRADeS de votre région. |
| Biologie et téléconsultation, si l'hôpital en fait | Laboratoire intégré : accréditation COFRAC et [réactovigilance ANSM](https://ansm.sante.fr/documents/reference/cybersecurite-des-dm-et-dmdiv), comme un laboratoire de ville. Téléconsultation : solution hébergée HDS, patient identifié ([référentiel ANS](https://esante.gouv.fr/produits-et-services/telesante/telemedecine/teleconsultation)). | Vérifier ces deux points avec le biomédical et l'éditeur. |

Textes du Code de la santé publique (CSP) : [Légifrance](https://www.legifrance.gouv.fr/).
