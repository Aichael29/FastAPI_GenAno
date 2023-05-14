from fastapi import FastAPI
from pydantic import BaseModel
from fct import *
import pandas as pd
import random
import csv
from typing import List, Dict, Optional
app = FastAPI()

class RandomData(BaseModel):
    min_value: int
    max_value: int
    count:int

@app.get("/")
async def root():
 return {"greeting":"Hello world"}
@app.post("/generate")
async def generate_random_data(data: RandomData):
    generated_data = []
    for _ in range(data.count):
        generated_data.append(random.randint(data.min_value, data.max_value))
    return {"data": generated_data}
"""cas d'utilisation : {
    "min_value": 0,
    "max_value": 100,
    "count": 5
}"""
class RandomDataGenerator:
    def __init__(self, column_types: Dict[str, str]):
        self.column_types = column_types

    def generate_random_data(self, num_rows: int, file_path: str) -> None:
        for column_type in self.column_types.values():
            if column_type not in ["int", "str", "bool", "float"]:
                return False
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.column_types.keys())
            writer.writeheader()
            for i in range(num_rows):
                row = {}
                for column_name, column_type in self.column_types.items():
                    if column_type == "int":
                        row[column_name] = random.randint(0, 100)
                    elif column_type == "float":
                        row[column_name] = random.uniform(0, 100)
                    elif column_type == "str":
                        row[column_name] = ''.join(
                            random.choices(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'], k=10))
                    elif column_type == "bool":
                        row[column_name] = random.choice([True, False])
                writer.writerow(row)
            return True


class RandomDataRequest(BaseModel):
    num_rows: int
    file_path: Optional[str] = "C:/Users/pc/Desktop/stage_inwi/random_data.csv"
    column_types: Dict[str, str]


@app.post("/generate_and_store")
def generate_random_data(request: RandomDataRequest):
    generator = RandomDataGenerator(request.column_types)
    if generator.generate_random_data(request.num_rows, request.file_path):
        return {"message": "Data generated and saved to {}".format(request.file_path)}
    else:
        return {"error": "type colonne invalide "}
class RandomData2(BaseModel):
    file_path: str
    line_number: int
    new_values: Optional[Dict[str, str]] = None
@app.put("/update")
def update_row(request: RandomData2):
    with open(request.file_path, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = [row for row in reader]

    if request.line_number >= len(rows):
        return{"message":"Invalid row number"}

    rows[request.line_number].update(request.new_values)

    with open(request.file_path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    return {"message": "Row {} updated in {}".format(request.line_number, request.file_path)}

"""
exemple d'execution :http://localhost:8000/update
{
    "file_path": "C:/Users/pc/Desktop/stage_inwi/random_data1.csv",
    "line_number": 2,
    "new_values": {
        "id": 1999,
        "name": "value",
        "age": 20,
        "salary": 12223456789
    }
}
"""

@app.delete("/delete")
def delete(request: RandomData2):
    # Ouvrir le fichier CSV en mode lecture
    with open(request.file_path, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)

    # Vérifier si l'index de ligne spécifié est valide
    if request.line_number < 0 or request.line_number >= len(rows):
        return{"message":"L'index de ligne spécifié n'existe pas dans le fichier CSV."}

    # Supprimer la ligne spécifiée
    del rows[request.line_number]

    # Écrire les lignes mises à jour dans le fichier CSV
    with open(request.file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows)

    return {"message": f"Ligne {request.line_number} supprimée de {request.file_path}"}
"""{
    "file_path": "C:/Users/pc/Desktop/stage_inwi/random_data1.csv",
    "line_number": 2
}"""


class EncryptFileInput(BaseModel):
    fichier_entree: str=None
    fichier_sortie: str=None
    operation: str=None
    cle_chiffrement: str=None
    mode_chiffrement: str=None
    vecteur: str=None
    colonnes: str = None
    separateur: str = None


@app.post("/encrypt_file")
async def encrypt_file_endpoint(input_data: EncryptFileInput):
    if input_data.fichier_entree is None:
        return {"message":" le fichier_entree n'est pas spécifié"}
    if input_data.fichier_sortie is None:
        return {"message":"le fichier_sortie n'est pas spécifié "}
    if input_data.operation is None:
        return {"message":"l'operation à effectué n'est pas spécifié"}
    if input_data.cle_chiffrement is None:
        return {"message":"le cle_chiffrement n'est pas spécifié"}
    if input_data.mode_chiffrement is None:
        return {"message":"le mode_chiffrement n'est pas spécifié"}

    # Lire le fichier d'entrée CSV dans un DataFrame
    try:
        df = pd.read_csv(input_data.fichier_entree, sep=input_data.separateur)
    except FileNotFoundError:
        return {"message": "Le fichier d'entrée spécifié n'existe pas."}
    # Appliquer la fonction de cryptage ou de hachage à chaque colonne spécifiée
    if input_data.colonnes:
        colonnes = input_data.colonnes.split(',')
    else:
        colonnes = df.columns.tolist()

    for col in colonnes:
        if input_data.operation == 'chiffrement':
            df[col] = df[col].apply(
                lambda x: aes_encrypt(str(x), input_data.cle_chiffrement, input_data.mode_chiffrement,
                                      iv=input_data.vecteur if input_data.mode_chiffrement == 'CBC' else None))
        elif input_data.operation == 'dechiffrement':
            df[col] = df[col].apply(
                lambda x: aes_decrypt(str(x), input_data.cle_chiffrement, input_data.mode_chiffrement,
                                      iv=input_data.vecteur if input_data.mode_chiffrement == 'CBC' else None))
        elif input_data.operation == 'hashage':
            df[col] = df[col].apply(lambda x: sha256_hash(str(x)))

    # Écrire le dataframe modifié dans un nouveau fichier csv
    df.to_csv(input_data.fichier_sortie, index=False, sep=input_data.separateur)

    return {"message": "Le traitement du fichier a été effectué avec succès."}

""" 
exemple d'execution :  http://localhost:8000/encrypt_file
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



