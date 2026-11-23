<!--
Source : mapping-menaces-risques.md § Niveau 3 ; version longue archivée dans archive/risques-v1/
À écrire : Fiche menaces (Laboratoire de biologie). Une section par type d'attaque, titre au format « #### <niveau> <titre> {#clé} ». Trois paragraphes courts : qui et comment, pourquoi chez vous, conséquences. Ces fichiers alimentent aussi la matrice.
Écrire en Markdown sous ce commentaire. Tant que le fichier est vide, le site affiche « À remplir ».
-->

#### 🔴 Hameçonnage et compromission de comptes {#hameconnage}

Un cybercriminel vole des identifiants par un faux email, pour revendre les données ou préparer un rançongiciel à partir du compte volé.

Pourquoi chez vous : beaucoup de personnes sur plusieurs sites, donc beaucoup de comptes. Un seul compte volé peut ouvrir la plateforme de résultats, reliée à Practilio.

Conséquences : les résultats d'analyses des patients de tous les sites peuvent être consultés ou volés, avec une [notification à la CNIL](obligations.html) et une atteinte à l'image du laboratoire et du groupe.

#### 🔴 Rançongiciel {#rancongiciel}

Un groupe cybercriminel organisé chiffre les systèmes et demande une rançon.

Pourquoi chez vous : les analyses sont centralisées. Si le plateau technique s'arrête, aucun site ne peut plus rendre de résultats, et le réseau qui relie les sites permet à l'attaque de se propager.

Conséquences : tous les sites arrêtés en même temps, des résultats retardés, des examens à refaire et des prises en charge ralenties.

#### 🟠 Attaque par rebond via un prestataire {#prestataire}

Un cybercriminel passe par l'accès d'un prestataire, par exemple celui qui assure la maintenance à distance des automates.

Pourquoi chez vous : plusieurs prestataires interviennent, avec des accès à distance entrants sur le réseau des équipements d'analyse.

Conséquences : automates indisponibles et analyses retardées.

#### 🟠 Accès illégitime aux dossiers {#acces-illegitime}

Un ancien salarié dont l'accès n'a pas été retiré, ou une personne en poste qui consulte par curiosité les résultats d'un proche.

Pourquoi chez vous : le personnel tourne entre les sites, beaucoup de personnes ont accès aux résultats, et un départ n'entraîne pas toujours la suppression des accès sur toutes les applications.

Conséquences : atteinte au secret médical, dont le laboratoire répond.

#### 🟠 Fuite de données par erreur {#fuite}

Personne ne cherche à nuire : un résultat part au mauvais patient ou au mauvais prescripteur, un fichier passe par une messagerie personnelle ou un outil d'IA grand public.

Pourquoi chez vous : un très grand nombre de résultats transmis chaque jour, à des destinataires différents, souvent par envoi automatique.

Conséquences : atteinte au secret médical, violation de données à [signaler à la CNIL](obligations.html), perte de confiance des patients et des prescripteurs.

#### 🟡 Perte ou vol de matériel {#perte-materiel}

Un portable, une tablette ou un téléphone professionnel est perdu ou volé, par exemple entre deux sites.

Pourquoi le niveau est modéré : la plupart des postes restent fixes. Le risque porte sur les appareils mobiles, pas toujours chiffrés ni gérés à distance.

Conséquences : des données accessibles à la personne qui trouve l'appareil, et une violation de données à [signaler à la CNIL](obligations.html).

#### 🟡 Attaque sur les équipements connectés (OT) {#ot}

En général, un cybercriminel dont l'attaque se propage du réseau informatique vers les automates d'analyse ou la supervision de la chaîne du froid, sans les viser en premier.

Pourquoi chez vous : ces équipements sont connectés, difficiles à mettre à jour et maintenus à distance par les fabricants.

Conséquences : des résultats faussés ou des échantillons perdus, donc des prélèvements à refaire, et des analyses interrompues.
