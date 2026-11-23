<!--
Source : notes-sujet.md (cas pratiques) ; mapping § Lien avec les cas pratiques
À écrire : Quiz corrigé avec explications pour le profil Dirigeant, chaque question rattachée à une case de la matrice. Format libre pour l'instant (question, choix, bonne réponse, explication) : il sera rendu interactif ensuite.
Écrire en Markdown sous ce commentaire. Tant que le fichier est vide, le site affiche « À remplir ».
-->

#### Un email signé d'un patient vous demande de lui renvoyer son ordonnance « en réponse à ce message ». L'adresse n'est pas celle de son dossier. Que faites-vous ? {menace=fuite}
- [ ] Je réponds avec l'ordonnance en pièce jointe, c'est plus rapide
- [x] J'envoie l'ordonnance par la messagerie de Practilio sur le compte connu du patient, ou je le rappelle au numéro du dossier
- [ ] Je réponds en demandant sa date de naissance pour vérifier

Rien ne prouve que l'expéditeur est votre patient, et une date de naissance se trouve facilement. Une donnée de santé envoyée à la mauvaise personne est une violation de données.

#### Votre fournisseur de matériel annonce par email un changement de RIB, facture « en retard » à l'appui. Que faites-vous ? {menace=hameconnage}
- [ ] Je mets à jour le RIB pour ne pas pénaliser le fournisseur
- [ ] Je réponds à l'email pour demander confirmation
- [x] Je ne change rien et j'appelle le fournisseur au numéro que je connais déjà (contrat, ancienne facture)

C'est la fraude au faux fournisseur, souvent préparée en piratant une vraie messagerie : répondre à l'email, c'est écrire à l'attaquant. Fixez la règle pour tout le monde : aucun changement de coordonnées bancaires sans double vérification.

#### Des données de patients ont été envoyées à la mauvaise personne et présentent un risque pour eux. De combien de temps disposez-vous pour notifier la CNIL ? {menace=fuite}
- [ ] Une semaine
- [x] 72 heures après en avoir pris connaissance
- [ ] Un mois, le temps de terminer l'enquête

Le délai court dès que vous avez connaissance de la violation. Vous pouvez compléter la notification ensuite. Voyez [vos interlocuteurs](incident.html#interlocuteurs).

#### Vos dossiers de patients sont stockés chez Practilio, hébergeur certifié HDS. Qui est responsable de ces données au sens du RGPD ?
- [ ] Practilio uniquement, puisqu'il les héberge
- [x] Vous, responsable du traitement ; Practilio est votre sous-traitant, avec ses propres obligations
- [ ] Personne en particulier, la certification HDS couvre tout

Vous décidez pourquoi et comment les données sont utilisées : vous êtes responsable du traitement. Practilio sécurise sa plateforme ; vous gérez qui y accède et comment. Voyez [qui est responsable de quoi](responsabilites.html#vous).

#### Une secrétaire quitte le cabinet vendredi. Quand son compte doit-il être fermé ? {menace=acces-illegitime}
- [ ] Lors du prochain point annuel sur les comptes
- [ ] Quand sa remplaçante arrive, pour lui transmettre le compte
- [x] Le jour même de son départ

Un compte resté ouvert est un accès que plus personne ne surveille. Chaque personne a son propre compte : la remplaçante en reçoit un à son nom.
