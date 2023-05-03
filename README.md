## FastAPI_GenAno
Le code fourni est un serveur FastAPI permettant de générer des nombres aléatoires , de les stocker dans un fichier CSV et chiffrer ou déchiffrer les données d'un fichier CSV . 

Utilisez un terminal pour vous rendre dans le répertoire du projet et exécuter la commande suivante:
* uvicorn main:app --reload
maintenant Vous pouvez tester tous les routes disponibles en utilisant Postman
### Les routes disponibles sont:
*  ### /: `renvoie un message de salutation`
* Vous pouvez le tester en utilisant Postman:
1.	Ouvrez Postman et créez une nouvelle requête GET.
2.	Dans l'URL de la requête, entrez l'URL de l'API que vous avez créée. Par exemple, si votre API est hébergée localement sur le port 8000, l'URL sera http://localhost:8000/.
3.	Cliquez sur le bouton "Send" pour envoyer la requête GET à l'API.
Vous devriez maintenant voir une réponse de l'API dans Postman. La réponse devrait être un objet JSON contenant une propriété "greeting" avec la valeur "Hello world".


*  ### POST /generate:`génère un nombre spécifié de nombres aléatoires entre une valeur minimale et maximale spécifiée, renvoyant les données générées au format JSON`
* Vous pouvez le tester en utilisant Postman:
1.	Ouvrez Postman et créez une nouvelle requête POST.
2.	Dans l'URL de la requête, entrez l'URL de l'API que vous avez créée, suivi de "/generate". Par exemple, si votre API est hébergée localement sur le port 8000, l'URL sera http://localhost:8000/generate.
3.	Cliquez sur l'onglet "Body" dans Postman, puis sélectionnez "raw" et "JSON" dans le menu déroulant.
4.	Dans le corps de la requête, entrez un objet JSON qui contient les propriétés "count", "min_value" et "max_value". Par exemple :
{
"count": 10,
"min_value": 0,
"max_value": 100
}
Cela indique à l'API de générer 10 nombres aléatoires entre 0 et 100 inclus.
5.	Cliquez sur le bouton "Send" pour envoyer la requête POST à l'API.
Vous devriez maintenant voir une réponse de l'API dans Postman. La réponse devrait être un objet JSON contenant une propriété "data" avec une liste de nombres aléatoires générés

*  ### GET /generate: `génère par défaut 10 nombres aléatoires entre 0 et 100, renvoyant les données générées au format JSON`
*  Vous pouvez le tester en utilisant Postman:
1.	Ouvrez Postman et créez une nouvelle requête GET.
2.	Dans l'URL de la requête, entrez l'URL de l'API que vous avez créée, suivi de "/generate". Par exemple, si votre API est hébergée localement sur le port 8000, l'URL sera http://localhost:8000/generate.
3.	Cliquez sur le bouton "Send" pour envoyer la requête GET à l'API.
Vous devriez maintenant voir une réponse de l'API dans Postman. La réponse devrait être un objet JSON contenant une propriété "data" avec une liste de 10 nombres aléatoires générés.

*  ### POST /generate_and_store: `génère un nombre spécifié de nombres aléatoires entre une valeur minimale et maximale spécifiée, stockant les données générées dans un fichier CSV. Le chemin du fichier CSV est codé en dur dans le code source.`
*  Vous pouvez  le tester en utilisant Postman:
1.	Ouvrez Postman et créez une nouvelle requête POST.
2.	Entrez l'URL de la requête: "http://localhost:8000/generate_and_store".
3.	Dans l'onglet "Body", sélectionnez "raw" et choisissez "JSON" dans le menu déroulant.
4.	Entrez les données de la requête JSON :
{ "min_value": 0, 
"max_value": 100, 
"count": 5 }
5.	Cliquez sur "Send" pour envoyer la requête.
Vous devriez recevoir une réponse JSON avec un message indiquant que les données ont été générées et stockées avec succès.


*  ### POST /generate_and_store_path_arg: `génère un nombre spécifié de nombres aléatoires entre une valeur minimale et maximale spécifiée, stockant les données générées dans un fichier CSV dont le chemin est spécifié en tant qu'argument de requête.`
*  Vous pouvez le tester en utilisant Postman:
1.	Ouvrez Postman et créez une nouvelle requête POST.
2.	Dans l'URL de la requête, entrez l'URL de l'API que vous avez créée, suivi de "/generate_and_store_path_arg". Par exemple, si votre API est hébergée localement sur le port 8000, l'URL sera http://localhost:8000/generate_and_store?file_path=C%3A%5CUsers%5Cpc%5CDesktop%5Cstage_inwi%5Crandom_data1.csv
3.	Cliquez sur l'onglet "Body" dans Postman, puis sélectionnez "raw" et "JSON" dans le menu déroulant.
4.	Dans le corps de la requête, entrez un objet JSON qui contient les propriétés "count", "min_value", "max_value" et "file_path". Par exemple :
{
"count": 10,
"min_value": 0,
"max_value": 100,
"file_path": " C:/Users/pc/Desktop/stage_inwi/random_data1.csv"
}
5.	Cela indique à l'API de générer 10 nombres aléatoires entre 0 et 100 inclus et de stocker ces données dans un fichier CSV situé à l'emplacement "data/generated_data.csv".
6.	Cliquez sur le bouton "Send" pour envoyer la requête POST à l'API.
Vous devriez maintenant voir une réponse de l'API dans Postman. La réponse devrait être un objet JSON contenant une propriété "message" avec un message indiquant que les données ont été générées et stockées avec succès.

*  ### POST /generate_and_store_path_class: `génère un nombre spécifié de nombres aléatoires entre une valeur minimale et maximale spécifiée, stockant les données générées dans un fichier CSV dont le chemin est spécifié en tant qu'attribut de classe.`
*  Vous pouvez le tester en utilisant Postman:
1.	Ouvrez Postman et créez une nouvelle requête POST.
2.	Dans l'URL de la requête, entrez l'URL de l'API que vous avez créée, qui est "/generate_and_store_path_class".
3.	Cliquez sur l'onglet "Body" dans Postman, puis sélectionnez "raw" et "JSON" dans le menu déroulant.
4.	Dans le corps de la requête, entrez un objet JSON qui contient les propriétés "count", "min_value" et "max_value". Par exemple :
{
  "count": 10,
  "min_value": 0,
  "max_value": 100,
  "file_path": " C:/Users/pc/Desktop/stage_inwi/random_data1.csv"
}
5.	Cliquez sur le bouton "Send" pour envoyer la requête POST à l'API.
Vous devriez maintenant voir une réponse de l'API dans Postman. La réponse devrait être un objet JSON contenant une propriété "message" avec un message indiquant que les données ont été générées et stockées avec succès.

*   ### PUT /update_csv/{line_number}/{new_value}: `modifie une valeur de la colonne "data" d'une ligne spécifiée dans un fichier CSV. Le chemin du fichier CSV est codé en dur dans le code source.`
* Vous pouvez le tester en utilisant Postman:
1.	Ouvrir Postman et créer une nouvelle requête PUT.
2.	Ajouter l'URL de l'API dans la barre d'adresse, par exemple http://localhost:8000/update_csv/3/25, où 3 est le numéro de la ligne à modifier et 25 est la nouvelle valeur à insérer dans la première colonne de cette ligne.
3.	Envoyer la requête et vérifier que la réponse contient le message "Ligne 3 modifiée avec succès!".
Vérifier que le fichier CSV a bien été mis à jour avec la nouvelle valeur en utilisant un éditeur de texte ou en répétant la lecture du fichier avec un script Python.

*  ### DELETE /delete_csv/{line_number}: `supprime une ligne spécifiée d'un fichier CSV. Le chemin du fichier CSV est codé en dur dans le code source.`
* Vous pouvez  le tester en utilisant Postman:
1.	Ouvrir Postman et créer une nouvelle requête DELETE.
2.	Ajouter l'URL de l'API dans la barre d'adresse, par exemple http://localhost:8000/delete_csv/3, où 3 est le numéro de la ligne à supprimer.
3.	Envoyer la requête et vérifier que la réponse contient le message "Ligne 3 supprimée avec succès!".
Vérifier que le fichier CSV a bien été mis à jour en utilisant un éditeur de texte ou en répétant la lecture du fichier avec un script Python.

* ### POST /encrypt_file: `chiffrer ou déchiffrer les données d'un fichier CSV en utilisant l'algorithme AES-256-CBC ou de hasher les données en utilisant l'algorithme SHA256. L'API prend en entrée le chemin du fichier source, le chemin du fichier de sortie, l'opération à effectuer (chiffrement, déchiffrement ou hashage), la clé de chiffrement, le mode de chiffrement, le vecteur d'initialisation, les colonnes à chiffrer/déchiffrer (optionnel), le séparateur de champ (optionnel) et retourne le fichier de sortie modifié.`
* Vous pouvez le tester en utilisant Postman:
1.	Ouvrir Postman et créer une nouvelle requête POST.
2.	Ajouter l'URL de l'API dans la barre d'adresse, par exemple http://localhost:8000/encrypt_file.
3.	Ajouter un corps de requête de type JSON contenant les paramètres d'entrée pour la fonction, par exemple :
{
    "fichier_entree": "C:/Users/pc/Desktop/stage_inwi/data.csv",
    "fichier_sortie": "C:/Users/pc/Desktop/stage_inwi/dataDA1.csv",
    "operation": "chiffrement",
    "cle_chiffrement": "ma_cle_secrete12",
    "mode_chiffrement": "CBC",
    "vecteur": "monvecteursecret",
    "colonnes": "id",
    "separateur": ";"

}
4.	Envoyer la requête et vérifier que la réponse contient le message "Fichier encrypté avec succès!".
Vérifier que le fichier de sortie a été créé avec les données modifiées en utilisant un éditeur de texte ou en répétant la lecture du fichier avec un script Python.
* ### POST /generate_data_int_str_date: ` Cette fonction generate_data_int_str_date utilise la bibliothèque random de Python pour générer des données aléatoires de trois types différents: int, str et date. Elle prend en entrée une instance de la classe RandomData qui spécifie les paramètres de génération des données, tels que la valeur minimale et maximale pour les entiers, le nombre de données à générer`
Vous pouvez le tester en utilisant Postman:
1. Assurez-vous que votre serveur est en cours d'exécution et que vous avez accès à l'URL de l'API.
2. Ouvrez Postman et créez une nouvelle requête POST en collant l'URL de l'API.
3. Dans le corps de la requête, sélectionnez le format JSON et entrez les valeurs souhaitées pour les paramètres de génération des données min_value, max_value et count. Par exemple:
{
 "min_value": 1,
 "max_value": 10,
 "count": 5
 } 
4. Cliquez sur le bouton "Envoyer" pour envoyer la requête. 
5. Si la requête est traitée avec succès, le serveur renverra une réponse JSON contenant un message de confirmation que les données ont été générées et écrites dans le fichier. Le fichier CSV contenant les données générées sera également créé dans le répertoire de travail actuel du serveur.
Vérifiez que le fichier CSV a été créé avec les données générées en naviguant vers le répertoire de travail du serveur.
* ### Le code importe également les modules random et csv, ainsi que le module fct (contient les fct de chiffrement,dechiffrement et hachage), et définit les modèles de données RandomData et RandomData1 à l'aide de la bibliothèque Pydantic.