import requests


def fetch_vinted_data(vinted_url, headers, cookies):

    response = requests.get(vinted_url, headers=headers, cookies=cookies)
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