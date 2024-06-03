import json
import random
import string

dataset = []
email = "renato.contreras798@gmail.com"

for i in range(1, 1001):
    name_length = random.randint(1, 100)
    name = ''.join(random.choices(string.ascii_letters + string.digits, k=name_length))
    product = {
        "name": name,
        "price": random.uniform(1, 1000000),
        "email": email
    }
    dataset.append(product)

# Guardando el conjunto de datos en un archivo JSON
json_path = "products_dataset.json"
with open(json_path, "w") as file:
    file.write("[\n")  # Iniciar la lista JSON
    for index, item in enumerate(dataset):
        json.dump(item, file)
        if index != len(dataset) - 1:
            file.write(",\n")  # Agregar coma y salto de línea después de cada objeto, excepto el último
    file.write("\n]")  # Cerrar la lista JSON

json_path
