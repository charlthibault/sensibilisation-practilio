<!--
Source : notes-sujet.md (cas pratiques) ; mapping § Lien avec les cas pratiques
À écrire : Quiz corrigé avec explications pour le profil Équipe IT, chaque question rattachée à une case de la matrice. Format libre pour l'instant (question, choix, bonne réponse, explication) : il sera rendu interactif ensuite.
Écrire en Markdown sous ce commentaire. Tant que le fichier est vide, le site affiche « À remplir ».
-->

#### Vous découvrez un VPN de télémaintenance ouvert il y a trois ans pour un équipement d'imagerie, avec un mot de passe partagé. Que faites-vous en premier ? {menace=ot}
- [ ] Je le coupe immédiatement
- [x] Je contacte le fabricant et le biomédical pour savoir s'il sert encore, avant de le sécuriser ou de le fermer
- [ ] Je change le mot de passe et je n'en parle à personne

Couper sans prévenir peut interrompre une maintenance en cours sur un équipement médical. S'il sert : compte nominatif, double authentification, ouverture à la demande, journalisation. Sinon : fermeture et vérification des journaux. Dans tous les cas, l'accès entre dans l'inventaire avec un propriétaire et une date de revue.

#### Le compte de votre prestataire est administrateur de tout le réseau et accède aux comptes des médecins, « c'était plus simple ». Quelle est la bonne correction ? {menace=prestataire}
- [ ] Rien, le prestataire est de confiance
- [ ] Changer le mot de passe du compte tous les mois
- [x] Limiter ses droits au strict nécessaire, un compte nominatif par intervenant avec double authentification, et séparer administration et accès aux données de santé

Si le prestataire est compromis, l'attaquant hérite de tous ses droits. Le moindre privilège limite les dégâts. Le contrat doit prévoir la revue de ces accès et l'information en cas d'incident.

#### Quelle sauvegarde protège réellement contre un rançongiciel ? {menace=rancongiciel}
- [ ] Une copie sur un disque réseau partagé, faite chaque nuit
- [x] Au moins une copie déconnectée ou non modifiable, dont la restauration est testée régulièrement
- [ ] La synchronisation des fichiers dans un dossier en ligne

Un rançongiciel chiffre aussi les sauvegardes qu'il peut atteindre, et une synchronisation recopie les fichiers chiffrés. Seul un test de restauration prouve qu'elle fonctionne.

#### Sur quels accès la double authentification est-elle prioritaire ? {menace=hameconnage}
- [ ] Seulement sur les postes des médecins
- [x] Messagerie, accès distants, consoles d'administration et comptes Practilio
- [ ] Elle est inutile si les mots de passe sont longs

C'est la mesure qui bloque le plus d'attaques par vol d'identifiants : un mot de passe volé par hameçonnage ne suffit plus pour entrer.

#### Un portable de l'équipe est volé dans une voiture. Quelle mesure, prise avant, limite le plus les conséquences ? {menace=perte-materiel}
- [x] Le chiffrement du disque et le verrouillage automatique de la session
- [ ] Un antivirus à jour
- [ ] Un mot de passe sur le fond d'écran

Sans chiffrement, il suffit de retirer le disque pour lire les données, mot de passe de session ou non. Pensez aussi à couper les accès de l'appareil (messagerie, Practilio, VPN) dès la déclaration du vol.
