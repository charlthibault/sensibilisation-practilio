<!--
Source : mapping-menaces-risques.md § Niveau 3 ; version longue archivée dans archive/risques-v1/
À écrire : Fiche menaces (Cabinet libéral). Une section par type d'attaque, titre au format « #### <niveau> <titre> {#clé} » (niveaux : 🔴 🟠 🟡 ⚪ — ; clés : hameconnage, rancongiciel, prestataire, acces-illegitime, fuite, perte-materiel, ot). Trois paragraphes courts : qui et comment, pourquoi chez vous, conséquences. Ces fichiers alimentent aussi la matrice.
Écrire en Markdown sous ce commentaire. Tant que le fichier est vide, le site affiche « À remplir ».
-->

#### 🟠 Hameçonnage et compromission de comptes {#hameconnage}

Un cybercriminel opportuniste, qui revend ensuite les accès ou les données, envoie un faux email (par exemple aux couleurs de Practilio) pour faire saisir un identifiant et un mot de passe sur un faux site.

Pourquoi chez vous : la double authentification n'est souvent pas activée, certains comptes sont partagés, et personne n'est chargé de repérer les messages suspects.

Conséquences : les dossiers de toute la patientèle peuvent être consultés ou volés depuis un compte légitime, ce qui oblige le cabinet à [notifier la CNIL](obligations.html) et entame la confiance des patients.

#### 🟠 Attaque par rebond via un prestataire {#prestataire}

Un cybercriminel passe par l'accès à distance de votre prestataire informatique, ou par le prestataire lui-même s'il a été piraté.

Pourquoi chez vous : un seul prestataire détient tous les droits d'administration, et son logiciel de prise en main à distance reste souvent ouvert en permanence.

Conséquences : l'attaquant a les mêmes droits que votre informaticien. Il peut bloquer tout le cabinet et lire ce qui est stocké sur les postes. Le même prestataire gère souvent d'autres cabinets, touchés en même temps.

#### 🟠 Fuite de données par erreur {#fuite}

Personne ne cherche à nuire : une ordonnance part au mauvais destinataire, un compte rendu est envoyé depuis une messagerie personnelle ou collé dans un assistant d'IA grand public.

Pourquoi chez vous : pas de messagerie sécurisée de santé utilisée au quotidien, des demandes de patients par email à traiter vite, et aucune règle écrite sur les outils autorisés.

Conséquences : atteinte au secret médical et violation de données à [signaler à la CNIL](obligations.html).

#### 🟠 Perte ou vol de matériel {#perte-materiel}

Un portable ou un téléphone professionnel est perdu ou volé, au cabinet, en visite à domicile ou dans les transports.

Pourquoi chez vous : les appareils ne sont pas toujours chiffrés, les sessions Practilio restent ouvertes et des mots de passe sont enregistrés dans le navigateur.

Conséquences : la personne qui trouve l'appareil accède aux documents et aux comptes encore connectés. C'est une violation de données à [signaler à la CNIL](obligations.html).

#### 🟡 Rançongiciel {#rancongiciel}

Un groupe cybercriminel chiffre les fichiers des postes et demande une rançon, parfois en menaçant aussi de publier les données.

Pourquoi le niveau est modéré : le cabinet a peu de postes, l'agenda et les dossiers gérés dans Practilio restent accessibles depuis un autre appareil, et les consultations peuvent continuer quelque temps sur papier. Le point faible reste les sauvegardes des postes, rarement testées.

Conséquences : quelques jours de fonctionnement dégradé, des frais de remise en état, et la perte des documents qui n'existaient que sur les postes.

#### ⚪ Accès illégitime aux dossiers {#acces-illegitime}

Un ancien salarié qui peut encore se connecter, ou une personne en poste qui ouvre un dossier par curiosité.

Pourquoi le niveau est faible : l'équipe est petite, chacun connaît les patients qu'il suit, et les départs sont rares. Le point d'attention est un mot de passe partagé qui n'est pas changé après un départ.

Conséquences, si cela arrive : atteinte au secret médical, dont le cabinet reste responsable.

#### — Attaque sur les équipements connectés (OT) {#ot}

Ne vous concerne pas : un cabinet libéral n'a en général aucun équipement médical ou technique relié à son réseau.
