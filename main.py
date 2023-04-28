
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from fastapi.responses import JSONResponse

import json

app = FastAPI()

# Load data from file
with open("data.json", encoding="utf-8") as f:
    countries_data = json.load(f)

# Define Pydantic models
class Country(BaseModel):
    name: str
    capital: str
    region: Optional[str] = None
    population: Optional[int] = None

# Define endpoints
@app.get("/countries")
async def get_all_countries():
    countries = []
    for country in countries_data:
        countries.append(Country(name=country["name"]["common"], capital=country["capital"][0]).dict())
    return countries

@app.get("/countries/{name}")
async def get_country_by_name(name: str):
    for country in countries_data:
        if country["name"]["common"].lower() == name.lower():
            return Country(name=country["name"]["common"], capital=country["capital"][0], region=country["region"], population=country["population"]).dict()
    return {"error": "Country not found"}

@app.get("/countries/region/{region}")
async def get_countries_by_region(region: str):
    countries = []
    for country in countries_data:
        if country["region"].lower() == region.lower():
            countries.append(Country(name=country["name"]["common"], capital=country["capital"][0]).dict())
    if len(countries) == 0:
        return {"error": "Region not found"}
    return countries

@app.post("/countries")
async def add_country(country: Country):
    for c in countries_data:
        if c["name"]["common"].lower() == country.name.lower():
            return {"error": "Country already exists"}
    new_country = {
        "name": {"common": country.name},
        "capital": [country.capital]
    }
    if country.region:
        new_country["region"] = country.region
    if country.population:
        new_country["population"] = country.population
    countries_data.append(new_country)
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(countries_data, f, indent=4)
    return {"message": "Country added successfully"}

@app.put("/countries/{name}")
async def update_country_by_name(name: str, country: Country):
    for c in countries_data:
        if c["name"]["common"].lower() == name.lower():
            c["capital"][0] = country.capital
            if country.region:
                c["region"] = country.region
            if country.population:
                c["population"] = country.population
            with open("data.json", "w", encoding="utf-8") as f:
                json.dump(countries_data, f, indent=4)
            return {"message": "Country updated successfully"}
    return {"error": "Country not found"}




