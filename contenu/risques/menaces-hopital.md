<!--
Source : mapping-menaces-risques.md § Niveau 3 ; version longue archivée dans archive/risques-v1/
À écrire : Fiche menaces (Hôpital public). Une section par type d'attaque, titre au format « #### <niveau> <titre> {#clé} ». Trois paragraphes courts : qui et comment, pourquoi chez vous, conséquences. Ces fichiers alimentent aussi la matrice.
Écrire en Markdown sous ce commentaire. Tant que le fichier est vide, le site affiche « À remplir ».
-->

#### 🔴 Rançongiciel {#rancongiciel}

Un groupe cybercriminel organisé chiffre les systèmes et demande une rançon.

Pourquoi chez vous : un système d'information très étendu, dont dépendent presque tous les services de soins.

Conséquences : passage en mode dégradé, retour au papier, soins et opérations reportés, et des coûts de remise en état très élevés.

#### 🔴 Accès illégitime aux dossiers {#acces-illegitime}

Surtout une personne en poste qui consulte, par curiosité, le dossier d'un proche, d'un collègue ou d'une personnalité, ou quelqu'un qui n'a plus le droit d'y accéder.

Pourquoi chez vous : un grand nombre de personnes ont accès aux dossiers, et intérimaires et internes changent souvent de service.

Conséquences : atteinte au secret médical, et c'est l'établissement qui est sanctionné, pas seulement la personne.

#### 🔴 Attaque sur les équipements connectés (OT) {#ot}

Le plus souvent, un cybercriminel dont l'attaque se propage du réseau informatique vers les équipements biomédicaux (imagerie, automates) ou techniques (fluides médicaux, chauffage et ventilation, contrôle d'accès).

Pourquoi chez vous : de nombreux équipements connectés, souvent anciens, difficiles à mettre à jour et maintenus à distance par des prestataires.

Conséquences : une atteinte directe à la sécurité des patients (examens impossibles, résultats faux) et des services d'imagerie ou de biologie à l'arrêt.

#### 🟠 Hameçonnage et compromission de comptes {#hameconnage}

Un cybercriminel vole des identifiants par un faux email, pour revendre les données ou préparer un rançongiciel.

Pourquoi chez vous : la double authentification et la surveillance sont plus probables qu'en cabinet, mais sur des milliers de comptes, il en suffit d'un.

Conséquences : extraction massive de dossiers depuis le dossier patient ou la messagerie, et [notification à la CNIL](obligations.html).

#### 🟠 Attaque par rebond via un prestataire {#prestataire}

Un cybercriminel passe par l'accès d'un prestataire de maintenance.

Pourquoi chez vous : de nombreux intervenants extérieurs, et des connexions ouvertes pour eux puis oubliées.

Conséquences : applications ou équipements indisponibles, et un accès possible aux données et aux équipements médicaux.

#### 🟠 Fuite de données par erreur {#fuite}

Personne ne cherche à nuire : un compte rendu part au mauvais destinataire, passe par une messagerie personnelle, ou est dicté dans un outil d'IA grand public.

Pourquoi chez vous : un très grand nombre de personnes manipulent des données de santé, avec des pratiques différentes d'un service à l'autre.

Conséquences : atteinte au secret médical et violation de données à [signaler à la CNIL](obligations.html).

#### 🟡 Perte ou vol de matériel {#perte-materiel}

Un portable, une tablette de soins ou un téléphone professionnel est perdu ou volé.

Pourquoi le niveau est modéré : le parc est en général géré par la DSI (chiffrement, blocage à distance), mais beaucoup d'appareils mobiles circulent entre les services.

Conséquences : des données accessibles à la personne qui trouve l'appareil, et une violation de données à [signaler à la CNIL](obligations.html).
