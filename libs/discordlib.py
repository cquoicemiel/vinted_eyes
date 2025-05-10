import requests
from datetime import datetime, timezone

def send_item_to_discord(webhook_url, item):
    embed = {
        "title": f"{item['title']}",
        "url": f"{item['url']}",
        "description": f"**Prix:** {item['price']["amount"]}{item["price"]['currency_code']} **~** {item['total_item_price']["amount"]}{item['total_item_price']["currency_code"]}\n**Marque:** {item['brand_title']}\n**Taille:** {item['size_title']}\n**{item['favourite_count']}** ❤️ **~** **{item['view_count']}** 👁️\n**État:** {item['status']}",
        "image": {"url": item['photo']['full_size_url']},
        "color": 15548997 if item['photo']['is_suspicious'] else 5763719,
        "author": {
            "name": f"{item['user']['login']}",
            "url": f"{item['user']['profile_url']}",
            "icon_url": f"{"https://cdn.discordapp.com/embed/avatars/0.png" if item['user']['photo'] is None else item['user']['photo']['thumbnails'][0]['url']}"
        },
        "footer": {
            "text": "旺代柚子镇",
            "icon_url": "https://cdn.discordapp.com/avatars/1162747302486753452/8ec77d35c160ebd9ba7d6d93090590dc.webp?size=512"
        },
        "timestamp": f"{datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'}"
    }

    data = {
        "username": "VINTED EYES",
        "embeds": [embed]
    }

    response = requests.post(webhook_url, json=data)
    if response.status_code == 204:
        print("Article envoyé avec succès.")
    else:
        print(f"Erreur lors de l'envoi de l'article: {response.status_code}, {response.text}")


def send_alert_to_discord(webhook_url, status):
    colors = {"on": 5763719, "off": 15548997}
    embed = {
        "title": f"Mise à jour de l'état",
        "color": colors[status],
        "description": f"État: **{str.upper(status)}**",
        "timestamp": f"{datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'}",
    }

    data = {
        "username": "VINTED EYES",
        "embeds": [embed]
    }

    response = requests.post(webhook_url, json=data)
    if response.status_code == 204:
        print("Alerte envoyé avec succès.")
    else:
        print(f"Erreur lors de l'envoi de l'alerte: {response.status_code}, {response.text}")
