from fastapi import FastAPI
import sqlite3
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    email: str
    age: int

# Connexion à la base de données
db = sqlite3.connect("users.db")

# Création de la table 'users' si elle n'existe pas encore
db.execute(
    "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT, age INTEGER)"
)

@app.post("/users/")
async def create_user(user: User):
    with db:
        db.execute("INSERT INTO users VALUES (?, ?, ?, ?)", (user.id, user.name, user.email, user.age))
        return {"message": "User created successfully"}

@app.get("/users/")
async def read_user():
    with db:
        result = db.execute("SELECT * FROM users").fetchall()
        if result:
            users = []
            for row in result:
                users.append({"id": row[0], "name": row[1], "email": row[2], "age": row[3]})
            return {"users": users}
        else:
            return {"message": "No users found"}


@app.get("/users/{user_id}")
async def read_user(user_id: int):
    with db:
        result = db.execute("SELECT * FROM users WHERE id=?", (user_id,)).fetchone()
        if result:
            return {"id": result[0], "name": result[1], "email": result[2], "age": result[3]}
        else:
            return {"message": "User not found"}

@app.put("/users/{user_id}")
async def update_user(user_id: int, user: User):
    with db:
        db.execute("UPDATE users SET name=?, email=?, age=? WHERE id=?", (user.name, user.email, user.age, user_id))
        return {"message": "User updated successfully"}

@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    with db:
        db.execute("DELETE FROM users WHERE id=?", (user_id,))
        return {"message": "User deleted successfully"}
