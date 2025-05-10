import csv
import datetime
import os
import libs.vintedlib as vintedlib
import libs.discordlib as discordlib

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "en-US,en;q=0.9",
    "X-Requested-With": "XMLHttpRequest",
    "DNT": "1",
    "Connection": "keep-alive",
    "Referer": "https://vinted.fr",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache"
}

cookies = {
    "_vinted_fr_session": "TmdQRzF1aDVyR0N0L1J5VzZacXh4VDBFTm83Z0tRZnJGOE4zVE5rUzRsWER4MjB4bkRsZm9ITXQ2eVc0QWJ1ME1IWWhYTmljNnhaSGYxZ0tXSENlOThwOUpzTjB3Q2hRU3JtYmZXNS9YcjFVWVlNb1lPcExNZHFyekxoZnhiM0ZzcHZLR3ptcTdiL25pdnVndCtHblQxSHpMZDUrcWNIbmpld05RS2swU2FnQ2ZjUGFtTEZ3NnN3eElDWVZvNS9KSHA1OURqaHhwZmptN291WjZxR0xIUnh3VDVXc1pvVTJKVXNSQmgySUU5cUZhSVByYm94WEZScUdRdVdQUUlLRTkvRm9PMHN4SDAxUWVXZ0I3amFKaDNieUpVTVlEVmwzODdodlpHMGwrVDRFa0l6Q05lL2EzdStBRUp2dXFRSGRGVUdWZ3hlQXhNOERZNlVDUGVQbTZUdzludnIwL2U3SEN4U1N1dUtybjFnVHc0SGJUdzQ5Q1FCWTZuMVJhV1RQZm1wSWs4MGs4ck9JSjJ2KzZUY3dWdkpSTjdUUjZxQ1QyaFl0RTdBblUrYjRXeXB5SkMzSUZxdGZoUXRtbTU5K2FkYW53ei94L0lsUmJTUk5UakVyaGw2NWxFUkVTRnhURjZtUkdiZVlNUndBdjRwUEZQd3BZTzBwc28xREN0QTl6R3BHTEhpSzZIVkc3ekVaZkU4RFYrd3FRcTFJc1htQmNrYmNQSUhzOUxDWEdqRm42N1N4RGF4TlZKSG9vc2tKb1BjWFl0UlVYZHo0cUtHNnFCOEZZUnMwNEpSTTBjNGFlUDVTSGF6bmlnb1dxVEhSaG40TTdBRXFaaXZnNTVrQkpIWW1hV3M2RWd3ODBhOGxEeitRcVBNZCt0b2EvakE3YlVyZG4vMDBaajhKZnlobzBwNEkzY0pkMzZJYm1td3RpMXhXNDRkYzJoWVNjUDV2VVdlU1FTZWtTeDlBOEMrTE9NZERpRnp4d0prdGllK3NjK3AySytyWnI3RXRhYlB5Y09wWlVMd1U3aE1lOE5uVEpseXRDajNZZUR4eStmd3JZUW5sY0RzTktoZW5HR1FxUFVJaGRCaVpPSVNOTFFiKzM4a3ExQlhJR1E5YWVTU0VmM2F1Q1d0VC9ETEpPSHFDOUxITVZIQVNQODF4blB3V1lTOG9Sam4xRU1RTld0eFNuemdPVmhlOENQeWpWRUFUeU80MkxOcmlTMFlwNFRXSldBdDdBbjkxeXN1UnIvUmlWWk4vY1hMWUhUaU5DVmVYUHJJMmZHUVFFVWFSTGNpMDRWeVRXR3RlV2h6ZFhxanBUaG11YlFZOG5CZmQxYzIzeEhEVVZ4c0F0RHRMYUxIV2xjVjdWaG9GUkhBRFR4cXFVa3lXNnNUeWczMmFsWkxNZHNHS3NxSDlzVERIdXQxRUhXTkI3UTBTWFc3SU9aV0hQZ2gzWXF5WEZkdFFaWFpicDlMOGxIbEQ4OHN6eFllQi9oRE1nRDVZYk00NVBrWUV5WXQ4cDI0NXFPdFNjT1FmRHh3Uko1eEZYR3BaTWszdzNZUDNGMlpOZ3MrS2g3TnZ6NEkwV2Jwamo0Mk90QytvS3hHUDRaa0dFK2NrcDZLaSs2VXFIUDFRN1NuZkFsc05KVUczK1FSb3E0ZlllNFEyNk81cDEvcjBXNWF0OC9aWGVYYTFMSEloUmJjV3dmQTVBcXNsN2tOS1hhSTk3cGFBRUp1OXRlTkRrTm1LanFsMmJWbWxkUGF0Y2wxS2l6QjBKN2NCbFRqTytjT0xmdDBJUngybEhXZ0xVQ0V1ZVVHdUIwYUljZ2orWG1YN3BUZzJoSk81NnBjMzlidktCZ0E2NWlvTWRhQlVSVGZHbzZwV2s0MnBEbXpFY1lCbzFnZ0ZLRXNNT3NxMGRqbjlFTG54cmNmdS9qL1NUek5neHY4SVVhWlkxN2lOT1BIR1pxb2RNWU9xQnd3cGtxVGF4VDdaSmxMZGE0dFduNm43Rm9KZzRnU2dSMlZPOFduZ0VFUG53OEcyTkI5UktVTTVhS3Y4T0NWRWlvRWNaUFR0MmYxSnVWWGlHU1g1a2ZyMDFlQVp1ek5WSWxwTEpHWTlZdDlXUVBkRC9XaSs3RS9tV0ltN0I4Mk05dWRGOGdpMmtYbFc4b3pkQVV0bnNocUJCSG9hSEhLbEtMVWVkQUUxcXRlQW8xZ05leXdvZEgwVTFiU2lpcTVtYnRWKzF6TGc0ZEQ2ekZGK05YUU9FZTk5a0xxQzY4bUNOSDVROXJJQ1lBUzgxSW4rK2xVUk9SbndMRDljcWMxMDYzK0d0bjg0T1pTN3Mwd2hMMTFZOWNuNzdma21Gb0J5d0NCSVMxUEpFWDB4bXBXNFE5OG51Wm54QzJrSmx3VFdYNi9LYnovVm1IWHdDYWdneFlocUN3aFZ3dnN4c0FrdndXbVJUTFJaWHJ3UnJmTk9rMExBa2VsaU1JNlM0MENyYmYvd3ByNmlMeXRaaExKTmozaTcwNUprbVNQcnVWcmhkcFBtWElCVVArWWhkOTBlSGMxQ3dUL2s2UUFoaWpabStRRUN1OGExckZGWkdoTWNoMG1MaEJRNVROUEJLYjJ4dUxDVkpDVENKZGlOVDhYNUpqc2VGSnFOaHdRa0dGdmFiKzB3VzJmT1NTRWp6cm9sQUJsdnpqdHRpQ1ZVSjY4T00zS09BUnM9LS10K1plTW56dmxacDhWT3JZVHVZQ0hnPT0%3D--a545a976fc931b5c212c45085231b63dc380b343",
}

fetch_label = "jean_levis_w30_l31"
base_url = "https://www.vinted.fr/api/v2/catalog/items"
params = {
    "page": 1,
    "per_page": 96,
    "search_text": "jean%20levis%20homme%20w31%20l31",
    "order": "newest_first",
    "catalog[]": 257,
    
}


fetched_items = vintedlib.fetch_vinted_all_data(base_url, headers, cookies, params)

# Fonction pour charger les articles déjà enregistrés
def load_existing_items(file_path):
    if not os.path.exists(file_path):
        return set()  # Aucun article n'existe encore

    with open(file_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return {row["id"] for row in reader}  # Récupère les IDs des articles déjà présents

existing_ids = load_existing_items(f"{fetch_label}.csv")

new_items = [
    {
        "title": item["title"],
        "url": item["url"],
        "price": item["price"]["amount"],
        "total_price": item["total_item_price"]["amount"],
        "currency": item["price"]["currency_code"],
        "brand": item["brand_title"],
        "size": item["size_title"],
        "condition": item["status"],
        "likes": item["favourite_count"],
        "views": item["view_count"],
        "photo": item['photo']['full_size_url'],
        "is_suspicious": item['photo']['is_suspicious'],
        "seller_name": item['user']['login'],
        "seller_url": item["user"]["profile_url"],
        "seller_icon": "" if item['user']['photo'] is None else item['user']['photo']['thumbnails'][0]['url'],
        "date": datetime.datetime.fromtimestamp(item["photo"]["high_resolution"]["timestamp"]).strftime("%d/%m/%y-%H:%M"),
        "id": item["id"]
    }
    for item in fetched_items if str(item["id"]) not in existing_ids
]

write_header = not os.path.exists(f"{fetch_label}.csv")  # Écrire l'en-tête uniquement si le fichier est nouveau

with open(f"{fetch_label}.csv", mode="a", encoding="utf-8", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=["title", "url", "price", "total_price", "currency", "brand", "size", "condition", "likes", "views", "photo", "is_suspicious", "seller_name", "seller_url", "seller_icon", "date", "id"])

    if write_header:
        writer.writeheader()

    for item in new_items:
        writer.writerow({
            "title": item["title"],
            "url": item["url"],
            "price": item["price"],
            "total_price": item["total_price"],
            "currency": item["currency"],
            "brand": item["brand"],
            "size": item["size"],
            "condition": item["condition"],
            "likes": item["likes"],
            "views": item["views"],
            "photo": item['photo'],
            "is_suspicious": item['is_suspicious'],
            "seller_name": item["seller_name"],
            "seller_url": item["seller_url"],
            "seller_icon": item["seller_icon"],
            "date": item["date"],
            "id": item["id"]
        })
