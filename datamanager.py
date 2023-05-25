import json

def load_data(file_name):
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Le fichier '{file_name}' n'existe pas.")
        return None
    except json.JSONDecodeError:
        print(f"Le fichier '{file_name}' ne contient pas de données JSON valides.")
        return None

def save_data(data, file_name):
    with open(file_name, 'w') as file:
        json.dump(data, file)

# Exemple d'utilisation

# Charger les données à partir d'un fichier
file_name = "data.json"
data = load_data(file_name)
if data is not None:
    print("Données chargées avec succès !")
    print(data)

# Modifier les données
if data is not None:
    data['example'] = 'Nouvelle donnée'

# Sauvegarder les données dans le fichier
save_data(data, file_name)
print("Données sauvegardées avec succès !")
