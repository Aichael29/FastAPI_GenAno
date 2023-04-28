# FastAPI_GenAno
### Le code fourni est un serveur FastAPI permettant de générer des nombres aléatoires , de les stocker dans un fichier CSV et chiffrer ou déchiffrer les données d'un fichier CSV . Les routes disponibles sont:

*  ### /: `renvoie un message de salutation`
*  ### POST /generate:`génère un nombre spécifié de nombres aléatoires entre une valeur minimale et maximale spécifiée, renvoyant les données générées au format JSON`
*  ### GET /generate: `génère par défaut 10 nombres aléatoires entre 0 et 100, renvoyant les données générées au format JSON`
*  ### POST /generate_and_store: `génère un nombre spécifié de nombres aléatoires entre une valeur minimale et maximale spécifiée, stockant les données générées dans un fichier CSV. Le chemin du fichier CSV est codé en dur dans le code source.`
*  ### POST /generate_and_store_path_arg: `génère un nombre spécifié de nombres aléatoires entre une valeur minimale et maximale spécifiée, stockant les données générées dans un fichier CSV dont le chemin est spécifié en tant qu'argument de requête.`
*  ### POST /generate_and_store_path_class: `génère un nombre spécifié de nombres aléatoires entre une valeur minimale et maximale spécifiée, stockant les données générées dans un fichier CSV dont le chemin est spécifié en tant qu'attribut de classe.`
*  ### PUT /update_csv/{line_number}/{new_value}: `modifie une valeur de la colonne "data" d'une ligne spécifiée dans un fichier CSV. Le chemin du fichier CSV est codé en dur dans le code source.`
*  ### DELETE /delete_csv/{line_number}: `supprime une ligne spécifiée d'un fichier CSV. Le chemin du fichier CSV est codé en dur dans le code source.`
*  ### POST /encrypt_file: `chiffrer ou déchiffrer les données d'un fichier CSV en utilisant l'algorithme AES-256-CBC ou de hasher les données en utilisant l'algorithme SHA256. L'API prend en entrée le chemin du fichier source, le chemin du fichier de sortie, l'opération à effectuer (chiffrement, déchiffrement ou hashage), la clé de chiffrement, le mode de chiffrement, le vecteur d'initialisation, les colonnes à chiffrer/déchiffrer (optionnel), le séparateur de champ (optionnel) et retourne le fichier de sortie modifié.`
### Le code importe également les modules random et csv, ainsi que le module fct (contient les fct de chiffrement,dechiffrement et hachage), et définit les modèles de données RandomData et RandomData1 à l'aide de la bibliothèque Pydantic.