import json
import requests
import sqlite3


# Fetch the data from the API endpoint
response = requests.get('https://restcountries.com/v3.1/all')
data = response.json()

# Filter the data
filtered_data = []
for country in data:
    if 'capital' in country:
        capitale = country['capital'][0]
    else:
        capitale = 'NULL'

    filtered_country = {
        'name': country['name']['common'],
        'region': country.get('region', ''),
        'population': country.get('population', 0),
        'capital': capitale
    }
    filtered_data.append(filtered_country)

# Write the filtered data to a new JSON file
with open('filtered_countries.json', 'w', encoding='utf-8') as f:
    json.dump(filtered_data, f, ensure_ascii=False, indent=4)

# Load the JSON data from file
with open("filtered_countries.json", "r", encoding='utf-8') as file:
    data = json.load(file)

# Connect to the SQLite database
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

# Create a table to store the data
cursor.execute("""CREATE TABLE countries (
                    name TEXT,
                    region TEXT,
                    population INTEGER,
                    capital TEXT
                )""")

# Loop through the JSON data and insert each row into the table
for country in data:
    name = country["name"]
    region = country["region"]
    population = country["population"]
    capital = country["capital"]
    cursor.execute("""INSERT INTO countries
                      VALUES (?, ?, ?, ?)""",
                   (name, region, population, capital))

# Commit the changes to the database and close the connection
conn.commit()
conn.close()
