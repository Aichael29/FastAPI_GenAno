from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import sqlite3

app = FastAPI()

# Connect to the database
conn = sqlite3.connect('mydatabase.db')
c = conn.cursor()

# Define Pydantic models
class Country(BaseModel):
    name: str
    capital: str
    region: Optional[str] = None
    population: Optional[int] = None

# Define endpoints
@app.get("/countries")
async def get_all_countries():
    c.execute("SELECT name, capital, region, population FROM countries")
    countries = []
    for row in c.fetchall():
        countries.append(Country(name=row[0], capital=row[1], region=row[2], population=row[3]).dict())
    return countries

@app.get("/countries/{name}")
async def get_country_by_name(name: str):
    c.execute("SELECT name, capital, region, population FROM countries WHERE name=?", (name,))
    row = c.fetchone()
    if row:
        return Country(name=row[0], capital=row[1], region=row[2], population=row[3]).dict()
    return {"error": "Country not found"}

@app.get("/countries/region/{region}")
async def get_countries_by_region(region: str):
    c.execute("SELECT name, capital, region, population FROM countries WHERE region=?", (region,))
    countries = []
    for row in c.fetchall():
        countries.append(Country(name=row[0], capital=row[1], region=row[2], population=row[3]).dict())
    if len(countries) == 0:
        return {"error": "Region not found"}
    return countries

@app.post("/countries")
async def add_country(country: Country):
    c.execute("SELECT name FROM countries WHERE name=?", (country.name,))
    row = c.fetchone()
    if row:
        return {"error": "Country already exists"}
    c.execute("INSERT INTO countries (name, capital, region, population) VALUES (?, ?, ?, ?)", (country.name, country.capital, country.region, country.population))
    conn.commit()
    return {"message": "Country added successfully"}

@app.put("/countries/{name}")
async def update_country_by_name(name: str, country: Country):
    c.execute("SELECT name FROM countries WHERE name=?", (name,))
    row = c.fetchone()
    if not row:
        return {"error": "Country not found"}
    c.execute("UPDATE countries SET capital=?, region=?, population=? WHERE name=?", (country.capital, country.region, country.population, name))
    conn.commit()
    return {"message": "Country updated successfully"}

from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import sqlite3

app = FastAPI()

# Connect to the database
conn = sqlite3.connect('mydatabase.db')
c = conn.cursor()

# Define Pydantic models
class Country(BaseModel):
    name: str
    capital: str
    region: Optional[str] = None
    population: Optional[int] = None

# Define endpoints
@app.get("/countries")
async def get_all_countries():
    c.execute("SELECT name, capital, region, population FROM countries")
    countries = []
    for row in c.fetchall():
        countries.append(Country(name=row[0], capital=row[1], region=row[2], population=row[3]).dict())
    return countries

@app.get("/countries/{name}")
async def get_country_by_name(name: str):
    c.execute("SELECT name, capital, region, population FROM countries WHERE name=?", (name,))
    row = c.fetchone()
    if row:
        return Country(name=row[0], capital=row[1], region=row[2], population=row[3]).dict()
    return {"error": "Country not found"}

@app.get("/countries/region/{region}")
async def get_countries_by_region(region: str):
    c.execute("SELECT name, capital, region, population FROM countries WHERE region=?", (region,))
    countries = []
    for row in c.fetchall():
        countries.append(Country(name=row[0], capital=row[1], region=row[2], population=row[3]).dict())
    if len(countries) == 0:
        return {"error": "Region not found"}
    return countries

@app.post("/countries")
async def add_country(country: Country):
    c.execute("SELECT name FROM countries WHERE name=?", (country.name,))
    row = c.fetchone()
    if row:
        return {"error": "Country already exists"}
    c.execute("INSERT INTO countries (name, capital, region, population) VALUES (?, ?, ?, ?)", (country.name, country.capital, country.region, country.population))
    conn.commit()
    return {"message": "Country added successfully"}

@app.put("/countries/{name}")
async def update_country_by_name(name: str, country: Country):
    c.execute("SELECT name FROM countries WHERE name=?", (name,))
    row = c.fetchone()
    if not row:
        return {"error": "Country not found"}
    c.execute("UPDATE countries SET capital=?, region=?, population=? WHERE name=?", (country.capital, country.region, country.population, name))
    conn.commit()
    return {"message": "Country updated successfully"}

@app.delete("/countries/{name}")
async def delete_country_by_name(name: str):
    c.execute("SELECT name FROM countries WHERE name=?", (name,))
    row = c.fetchone()
    if not row:
        return {"error": "Country not found"}
    c.execute("DELETE FROM countries WHERE name=?",(name,))
    return {"message": "Country deleted successfully"}

# Close the database connection on exit
@app.on_event("shutdown")
def shutdown_event():
    conn.close()

# Close the database connection on exit
@app.on_event("shutdown")
def shutdown_event():
    conn.close()
