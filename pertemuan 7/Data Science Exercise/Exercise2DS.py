data = {
    "Negara": ["Indonesia","Jepang","malaysia","inggris", "china", "singapura", "chile"],
    "Capital": ["Jakarta", "Tokyo", "New Delhi", "Beijing", "Washington DC", "Brasilia", "Moscow"],
    "Continent": ["Asia", "Asia", "Asia", "Asia", "America", "America", "Asia"],
    "Area": [1905, 377, 3287, 9597, 9834, 8515, 17098],
    "Population": [264, 143, 1252, 1357, 329, 210, 146]
}

df = pd.DataFrame(data)
print(df)
df.to_csv("datanegara.csv")
