import requests
import time

def fetch_vinted_all_data(fetch_url, headers, cookies, params):
    all_items = []
    page = 1

    while True:
        print(f"Fetching page {page}...")
        params["page"] = page
        response = requests.get(fetch_url, headers=headers, params=params)
        response.raise_for_status()  # Vérifie les erreurs HTTP
        data = response.json()

        items = data.get("items", [])
        if not items:
            break  # Arrête la boucle si aucune donnée n'est retournée

        all_items.extend(items)
        page += 1
        time.sleep(50)  # Pause pour éviter de surcharger l'API

    return all_items

def fetch_vinted_data(vinted_url, headers, cookies, params):

    response = requests.get(vinted_url, headers=headers, cookies=cookies, params=params)
    if response.status_code == 200:
        data = response.json()
        if 'items' in data and len(data['items']) > 0:
            return data['items']
        else:
            print("Aucun item trouvé.")
            return None
    else:
        print(f"Erreur lors de la requête: {response.status_code}")

        return None