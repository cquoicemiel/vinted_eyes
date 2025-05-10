import time
import libs.vintedlib as vintedlib
import libs.discordlib as discordlib
import atexit
import os
from dotenv import load_dotenv


@atexit.register
def on_close():
    discordlib.send_alert_to_discord(discord_webhook_url, "off")

load_dotenv()


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
    "_vinted_fr_session": "WXRmeEZIOE1CM0M2alBQMEVtaVhZd1hVMFhkNFRHaU5YQVgrL0d5RkpkZ0NEc2pCU3dpM0owSXp5ZWdBZ0RlR0ZNaEJ5OFdSN0NpNUxieVhiSW5UZVFIalB0NU9iV3FvMjV4enpaQm1IZ2JuRUVkT0t6Ty9FWG5iNWtONkhlUks4MSs4bURmdHNWWFJSNjVoRmFWMFFtSWZjT3lhNlo4Q3VmakNSZTlzZHYvSUtKWnQ0ZjF5NEl3T3lQNzhPS1hodzZMTnhzc0pHdEJYeTNEblZVaTl2M3BWTmRUMmxGNmkyODNIUEFLdDdhRlpsekhpNlQxSlpWTU5WWlBxa1AzdmxtZFFzY2hKaTZOMEZFSitmbkFvcG1NZHI2SWk4OHJmbERaU1ljOE9Ob0ZrZlRpTlRXYlR6UTYzTnpiUGsyelZvK0dianlhRzBwejZBWmFsTWdkYTl1NEY3NWkwY3VLT3AyWHA0cy9HWUJqS0tTWGZUL21seWJoZ2ZGd0JSTUl0V1BNbGhic1QzMkZZQWo3U2VMR1ZGKzFuRW5VUjJQcnd4SHh4cmVtMWNZenFTSUZiSmQ2eHRoY1YzS1M0TldUVUR4dXVNdlZJbmJWc1M5SVRoN2hFWUFDTHhjSVcvV21DaU9hMzVlRUFYelJBTDl2czlpL1NGOGQ2cFVvZ2ovZXViQk5pR0lqZ21YQTNQOGV2a3c5WXV3ZHVIODhEeDhSRUd2QkFwelhoMkNjaXlFbTJsVWVoUXRSMy9uZlVoeWkzUkZYM0pGa3RXZXprYXFjY3ZVYkFMc01hTHV5ZXJ0elE3d1duZjBjL2FtMmY2U0svcW1aN0w4Z3Fobyt2MTNvc3QrTENhc1lmZHl6NzdCUmU3TE9kOWRCcVdzajkyQmVCb0NnUlJxNGp6dURzd0pwY3BZNkhaVlRPVWZLTVI2eGZPSjNla25nSWwyYUFRUXZVR3BFSXc2VERRQTFMU1d2QmtsWUVibWd4U2dza3RIZFNtTGhWWFRrWk94RmRwZkk5RGpWSUUwMjdhVTNxS0NxU0lmMUZKR2k2a1gyOENQc2lZTGRNS001UmVkVldzeFBWeVRWbjdyMnNEWi9ZVkFUOW03eTZCakw5MlVrZW9ZbU9RaC9VWklKQ2ZmclVvNUd5dGgwZ1NNdTNXekdlaEtIMThpa3NOdGdMK0ZYQmNUZFlLTml3V0NZTUNUaDdFWHJJSUNYdFZOZndDc2hkZHBNMDU1ZklXU08xR0Q3M0t6Vm56aWNMbGphR05LUmt0OTZLNWpZT0tWdlpRUlpVdjhtZjFmVTU3eGVncThwYngrVERqemlCS2txdFN1ZHlJNndTSi9UUlNJcFNQZFNmWllyRXJ2VUJxMGQ1bTlKUG5VendqY3kvT1o1aUk5NW9NWEpEOVQ1K2RCV1JLNDc3UlFtaTljQThIM1g0bmhRRWtOU252TU1ZWnA2TWU5M1ZYN0tKdm5NRjh4bkhHN1d1NmpaeGsvdG12b1NMN3c3MmU3Ukw1WThXTUVoNmk2dVFiREdVQVFHZ2FGZ2k1TW1xcWtMbkFVbi9hRlJzV0FlMkR4SThtZWEzRmRWM0Vkc2d2azdXb0ExV1BIWHV1YlRNcTJnSkN2enptbzdIQmZKcGcxUjRtQjU0aEF1eklWdmYreXozSUJUY09NTVdpRVNIN09VTGdqejdEY1Z3UVYwc2hiQkpUdE00ZUFCL0liRkhlSHZzeG9MMmJ0Q25tYUNyNjhWQ2ZZVWVaK3phd1prMGx2d0Z4bnJpZmFxam1jOU5VdkMyK0IrNXhXbHpYQjV6cFFSRGdmaEU4MHN3WnhsLzZoZkp6Qlk0NlN4eWx1MFV1UXc3WVU1ZUs5V0lPZzlFbVpTdnp6cGR0aEQ4TzlseHhLSlhmUGlJZUtHZ01nVGZZNFZSd0EvU1RlbFhzNnUwb2JGWldMenNXM2tmVitxVmUvWXJha2dqT01OMEJ2Y04yK1Vtb0ZLM2hxS3VQZ0tzUUNoejNSNGQra0VjSFppRWJsb3lhaXAyVDBDMVBIdnQxZWlkYXBtdkRVeVNXMWFldjFXQ2JIdFF3LzRwUHlaREdRWGh1WXFYbTBsa1B1eTdyVEJUY2VvTnljWitPWWMzYkhlOU1maFZmMTdXQ2JubDNkZ2lObGpXQlFkNFFsOUhuazZ5dFZsZnhWTDdPWFkxZ25kM2JDUEpJY04vbFR3YVhEZ0NpNDBEZWtqUDZ2ZHE2aWREdjk3L3U2eWJ5eFgxR2t2MXJlcmxuQTJoQ2svK3dTYjVnY1FxZUhBTzR6blp5am9SUEdNdzJjMmNXb1ZRbnU4RjUxT0VpVkJqaVN0bDVFU2Y2cTRTbDJMUEwveU0wdVBxY3Jpdmo3ajF5QWMxOUhDRytualF3S0ltTkFTbWV3T0dUamIzTXQxaElHTGlkbCs2TDZya2JwdEV6VWZjb0NFSnJzOEk0bGNkaW9oZUhIWEJ3VjRrcTlZanQvMWdUUk1NejFDeGdETVQrSFNkeGVyT3p2aFV0M0lWUzdRK1NsOTJwUjlPaC9xLzVaNDNFMWJGTC9FMDhwMDF6VXNiNDFLSjV1Y1NtSHhzRlJpdTdlam1WRlZwQ2hRM29SSzhycUI3Q3Vja1h2OE9qQWpwQ2RGdmpRak1sSGJOdE16elJrWUEyTXRmL3kxNzV2SmRYWEM2T0FFWWowMkZJRTA9LS0xbXFQTmlZUERabjlnTVJJYVJPRUNBPT0%3D--6ec90023ce965315ae74ba8e24024f03fcb8c7ca",
}

# url à surveiller
vinted_url = "https://www.vinted.fr/api/v2/catalog/items?page=1&per_page=96&search_text=jean%20levis%20homme%20w31%20l31&order=newest_first&catalog[]=257&order=newest_first"
# url du webhook discord
discord_webhook_url = os.getenv("DISCORD_WEBHOOK_URL")

response = vintedlib.fetch_vinted_data(vinted_url, headers, cookies)

seen_ids = {item["id"] for item in response}
fetch_count = 0

discordlib.send_alert_to_discord(discord_webhook_url, "on")

while True:

    time.sleep(120)
    print(f"{fetch_count} | recherche... 🐉🐉😶‍🌫️ | {len(seen_ids) - 96} items sniped")
    items = vintedlib.fetch_vinted_data(vinted_url, headers, cookies)
    fetch_count += 1
    for item in items:
        if item["id"] not in seen_ids:
            discordlib.send_item_to_discord(discord_webhook_url, item)
            seen_ids.add(item["id"])
            print(item["title"], "added to seen items")
            time.sleep(1)
