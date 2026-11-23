<!--
Source : notes-sujet.md (cas pratiques) ; mapping § Lien avec les cas pratiques
À écrire : Quiz corrigé avec explications pour le profil Employé, chaque question rattachée à une case de la matrice. Format libre pour l'instant (question, choix, bonne réponse, explication) : il sera rendu interactif ensuite.
Écrire en Markdown sous ce commentaire. Tant que le fichier est vide, le site affiche « À remplir ».
-->

#### Un email aux couleurs de Practilio vous demande de changer votre mot de passe, qui « expire aujourd'hui ». Que faites-vous ? {menace=hameconnage}
- [ ] Je clique sur le lien et je change mon mot de passe tout de suite
- [ ] Je réponds à l'email pour demander s'il est authentique
- [x] Je tape moi-même l'adresse habituelle de Practilio, et je signale le message

Un message pressant qui pousse à cliquer est le signe classique de l'hameçonnage. La page ouverte par le lien peut imiter Practilio avec une adresse presque identique. Répondre à l'email ne prouve rien : c'est l'attaquant qui répondra. Voyez [la situation détaillée](premiers-pas.html#fiche-reflexe).

#### Un patient vous tend une clé USB pour imprimer son ordonnance. Que faites-vous ? {menace=rancongiciel}
- [ ] Je la branche, l'antivirus vérifiera
- [x] Je ne la branche pas et je propose une autre solution (messagerie de Practilio, document sur son téléphone)
- [ ] Je la branche sur le poste du médecin, moins exposé que l'accueil

Une clé peut contenir un programme malveillant, même à l'insu de son propriétaire. Aucun poste qui accède aux dossiers de patients ne doit recevoir un support inconnu.

#### Votre écran affiche une demande de rançon et vos fichiers ont changé de nom. Quel est le premier geste ? {menace=rancongiciel}
- [ ] J'éteins l'ordinateur
- [x] Je débranche le câble réseau et je coupe le Wi-Fi, sans éteindre, puis je préviens
- [ ] Je paie pour récupérer les fichiers au plus vite

Débrancher le réseau empêche la propagation aux autres postes. Éteindre ferait perdre des traces utiles à l'enquête. Payer ne garantit rien et finance les attaquants. La suite : [que faire selon la situation](incident.html#situation).

#### Une collègue partage avec toute l'équipe, par un simple lien, un tableur en ligne créé sur son compte personnel, avec les rendez-vous et leur motif. Où est le problème ? {menace=acces-illegitime}
- [ ] Il n'y en a pas, si le lien n'est donné qu'aux collègues
- [ ] Le seul problème est que le tableur n'est pas protégé par un mot de passe
- [x] Des données de santé sortent des outils prévus : le cabinet ne les maîtrise plus et n'importe qui ayant reçu le lien y accède

Le motif de consultation est une donnée de santé. Stocké hors des outils prévus, il échappe au cabinet : impossible de le protéger ou de couper l'accès au départ de la collègue. Le bon réflexe est d'exprimer le besoin au responsable. Voyez [le scénario complet](premiers-pas.html#scenario).

#### Pour gagner du temps, vous voulez reformuler un courrier médical avec un assistant d'intelligence artificielle en ligne. Que pouvez-vous y mettre ? {menace=fuite}
- [ ] Le courrier, si je retire le nom du patient
- [x] Rien qui concerne un patient, sauf outil validé par l'établissement
- [ ] Le courrier complet, ces outils suppriment les données après usage

Ce que vous tapez part sur les serveurs de l'éditeur, parfois hors de l'Union européenne, et peut être conservé. Retirer le nom ne suffit pas : une date et une pathologie permettent souvent de reconnaître quelqu'un. Voyez [l'IA et les données de patients](premiers-pas.html#ia).
