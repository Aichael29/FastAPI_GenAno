from fastapi import FastAPI
from pydantic import BaseModel
import random
import csv
from datetime import datetime, timedelta
from fct import *
app = FastAPI()


class RandomData(BaseModel):
    min_value: int
    max_value: int
    count: int

@app.get("/")
async def root():
 return {"greeting":"Hello world"}
@app.post("/generate")
async def generate_random_data(data: RandomData):
    generated_data = []
    for _ in range(data.count):
        generated_data.append(random.randint(data.min_value, data.max_value))
    return {"data": generated_data}

@app.get("/generate")
async def generate_default_random_data():
    generated_data = []
    for _ in range(10):
        generated_data.append(random.randint(0, 100))
    return {"data": generated_data}

@app.post("/generate_and_store")
async def generate_and_store_random_data(data: RandomData):
    generated_data = []
    for _ in range(data.count):
        generated_data.append(random.randint(data.min_value, data.max_value))

    # Écrire les données dans un fichier CSV
    with open('C:/Users/pc/Desktop/stage_inwi/random_data1.csv', mode='w', newline='') as csv_file:
        fieldnames = ['data']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for data_point in generated_data:
            writer.writerow({'data': data_point})

    return {"message": "Données générées et stockées avec succès!"}

""""
exemple d'execution 
http://127.0.0.1:8000/generate_and_store
{
    "min_value": 0,
    "max_value": 100,
    "count": 5
}"""

@app.post("/generate_and_store_path_arg")
async def generate_and_store_random_data(data: RandomData, file_path: str):
    generated_data = []
    for _ in range(data.count):
        generated_data.append(random.randint(data.min_value, data.max_value))

    # Écrire les données dans un fichier CSV
    with open(file_path, mode='w', newline='') as csv_file:
        fieldnames = ['data']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for data_point in generated_data:
            writer.writerow({'data': data_point})

    return {"message": f"Données générées et stockées avec succès dans le fichier {file_path}!"}


"""
exemple d'execution 
http://localhost:8000/generate_and_store?file_path=C%3A%5CUsers%5Cpc%5CDesktop%5Cstage_inwi%5Crandom_data1.csv
    {
        "min_value": 1,
        "max_value": 100,
        "count": 10

}
"""
class RandomData1(BaseModel):
    min_value: int
    max_value: int
    count: int
    file_path: str

@app.post("/generate_and_store_path_class")
async def generate_and_store_random_data(data: RandomData1):
    generated_data = []
    for _ in range(data.count):
        generated_data.append(random.randint(data.min_value, data.max_value))

    # Écrire les données dans un fichier CSV
    with open(data.file_path, mode='w', newline='') as csv_file:
        fieldnames = ['data']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for data_point in generated_data:
            writer.writerow({'data': data_point})

    return {"message": f"Données générées et stockées avec succès dans le fichier {data.file_path}!"}


""" 
exemple d'execution
{
        "min_value": 1,
        "max_value": 100,
        "count": 10,
        "file_path":"C:/Users/pc/Desktop/stage_inwi/random_data1.csv"

}
"""
class RandomData2(BaseModel):
    file_path: str
@app.put("/update_csv/{line_number}/{new_value}")
async def update_csv(path: RandomData2,line_number: int, new_value: int):
    # Ouvrir le fichier CSV et lire les données
    with open(path.file_path, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        data = list(csv_reader)

    # Modifier la ligne spécifiée
    data[line_number][0] = new_value

    # Écrire les données modifiées dans le fichier CSV
    with open(path.file_path, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(data)

    return {"message": f"Ligne {line_number} modifiée avec succès!"}

"""
exemple d'execution :http://localhost:8000/update_csv/1/42
{
    "file_path":"C:/Users/pc/Desktop/stage_inwi/random_data1.csv"
}
"""
@app.delete("/delete_csv/{line_number}")
async def delete_csv(path: RandomData2,line_number: int):
    # Ouvrir le fichier CSV et lire les données
    with open(path.file_path, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        data = list(csv_reader)

    # Supprimer la ligne spécifiée
    del data[line_number]

    # Écrire les données modifiées dans le fichier CSV
    with open(path.file_path, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(data)

    return {"message": f"Ligne {line_number} supprimée avec succès!"}
"""exemple d'execution :http://localhost:8000/delete_csv/2
  {
    "file_path":"C:/Users/pc/Desktop/stage_inwi/random_data1.csv"

}
"""
class EncryptFileInput(BaseModel):
    fichier_entree: str
    fichier_sortie: str
    operation: str
    cle_chiffrement: str
    mode_chiffrement: str
    vecteur: str
    colonnes: str = None
    separateur: str = None
@app.post("/encrypt_file")
async def encrypt_file_endpoint(input_data: EncryptFileInput):
    df = pd.read_csv(input_data.fichier_entree, sep=input_data.separateur)
    # Appliquer la fonction de decryptage à chaque colonne spécifiée
    if input_data.colonnes:
        colonnes = input_data.colonnes.split(',')
    else:
        colonnes = df.columns.tolist()

    for col in colonnes:
        if input_data.operation == 'chiffrement':
            df[col] = df[col].apply(lambda x: aes_encrypt(str(x), input_data.cle_chiffrement, input_data.mode_chiffrement, iv=input_data.vecteur if input_data.mode_chiffrement == 'CBC' else None))
        elif input_data.operation == 'dechiffrement':
            df[col] = df[col].apply(lambda x: aes_decrypt(str(x), input_data.cle_chiffrement, input_data.mode_chiffrement, iv=input_data.vecteur if input_data.mode_chiffrement == 'CBC' else None))
        elif input_data.operation == 'hashage':
            df[col] = df[col].apply(lambda x: sha256_hash(str(x)))
    # écrire le dataframe modifié dans un nouveau fichier excel
    df.to_csv(input_data.fichier_sortie, index=False, sep=input_data.separateur)


""" exemple d'execution :  http://localhost:8000/encrypt_file
{
    "fichier_entree": "C:/Users/pc/Desktop/stage_inwi/data.csv",
    "fichier_sortie": "C:/Users/pc/Desktop/stage_inwi/dataDA1.csv",
    "operation": "chiffrement",
    "cle_chiffrement": "ma_cle_secrete12",
    "mode_chiffrement": "CBC",
    "vecteur": "monvecteursecret",
    "colonnes": "id",
    "separateur": ";"

}"""

@app.post("/generate_data_int_str_date")
async def generate_data(random_data: RandomData):
    data = []
    for i in range(random_data.count):
        # Générer une valeur aléatoire de type int
        int_val = random.randint(random_data.min_value, random_data.max_value)

        # Générer une valeur aléatoire de type str
        str_val = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=random.randint(1, 10)))

        # Générer une valeur aléatoire de type date
        date_val = datetime.today() - timedelta(days=random.randint(0, 365))

        # Ajouter les valeurs dans la liste de données
        data.append((int_val, str_val, date_val.strftime("%Y-%m-%d")))

    # Écrire les données dans un fichier CSV
    with open('random_data.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['int', 'str', 'date'])
        writer.writerows(data)

    return {"message": f"Les données ont été générées et écrites dans le fichier 'random_data.csv'."}



