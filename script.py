import time
import vintedlib
import discordlib
import atexit


@atexit.register
def on_close():
    discordlib.send_alert_to_discord(discord_webhook_url, "off")


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "en-US,en;q=0.5",
    "X-Requested-With": "XMLHttpRequest",
    "DNT": "1",
    "Connection": "keep-alive",
    "Referer": "https://www.vinted.fr/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "TE": "Trailers"
}

cookies = {
    "_vinted_fr_session": "SGtWZFhNNDk3cnRBbmdMVTlKV2Z6ZFdyK1IxejlLYUhjcWdUK0NBVDdJbkh5TjNYZmFHR1lzRFpBR1dqZUNVSEVpMzBiM1lJNkk5L09YcEVoa3J6S0JXVHcvUUp4ZmM3M0JmUDI2cUQwK3pnZjR5WDIyK1prR0hOZ2JZL283cWRsSzI2VDcrWjJ0MnBIc3NraGZwSVNHU01jaHVMNGE4VGFVNEhndlc3aTRkSFVUV1FuN1BFdnhNSk5iUkY5ZEFscmVQaHJBUXRTcGZHcVlFaG11MDBhMTRKaFpWSmR6NDBOU0lEbDlLUEFVTzV6dkxuQlBpY1hkbHRzRnlySW5SRG56TzFuNWk0RUJDOVpUMHZlZEU1U3VRMmxKQjlJbHQ5Zjc5dFBmK1BJTzVaOSszUlk2TjNmSHk5NlJhU1ZwMHprZGJaNkR6V3BGYXVhcUVZMGFTZ1NabDUyWmczeU1aQ2lkZ0ZOblNFdnRaMG9KMUloQ1ppQk4ya0REbW5Gb0xIOE1kNjQxTlNGMEpuckJNRVJCakhXZUJLc0dFUjRYWjBCSUJNOGY2RWZOZE9wTDBoSHpxdU9obmwyUG4yNGQvTW5uQXBlc3U4Mk1oUU91d3VwMnRDZ1JFT284WEoreVpWOU5idmwwMGNhVlU3bk9zZEdGb2phUXVSZ0pXY3dDWXNRTERKOXdjL3Jhcy9tL1k2cE9PWGhNZVpyeFVBU29CYmhHaGZpdmtSNnNmUDdacldoQWZBbXZ6Zm1QK1kyMUhjTWo1OCtzbGVyWUJFTDRydVd0eUM3SmlidGxIVjVxRDZDNjZuT1FHbHB5N0xOTDB2amRsekVBV2l4V0xDSE1CRVdnNHRRR1EwTnExcFF6MnhEd3hCdlU0Z09mSmlSRFR4T1drdVdHTTdaNmpEQUpVU2VSQktqSVhOaFBFeEZJWkoySGdCeUlER2hQYkRKdDVWODl2dnRCcTBVaVYxR3NFTnRBdCt2UlNYb2h3WnVOMGdBMUVWZERUS25RdmR4SlNZRFRFUkljNUZadGdjTURuS2hPZXNuMWo5eDZvSEY0Rmh2MmV0UkRkMGNpM0tZUWxuZkVOREl3OXdPMWgyT29wWUxKY1c5UnFGbkRYMFFNazFOaXFXQjVWRFRPbTdUakxyUXIzZzBjYndNeXV5Vk1vU0hRbjRBUUhzbXlHaW1RZmJlbVRDWm5JeSs3bkJVUkVlVzB6cDNCd1RHWSs4MDhBYXFTS0pUcldJaG4ydXZkajd4cVFMSHVjTDV2aHAvUjlJZ0lhQmJ0YUpGQXlCQ3psSnp0OWZKVGpwQVdJb21JLzZ4NUdzaVVIY20rUjA5T1o4V0FZclBmV25vbTlGdzZNeExadE5zL0FYWi9rVzJoWFd0MWVJWTlMVnpnais3SFdhdU8vUmhmSUJITzcxNkNSdUl6YUM3L2Y2TjBwanh4eGdxMUNySE4xMkFnUWFMd0lqVis2aUtYNDdpQzB2R1hndmRJY25JdjVMZkErbG9tWU1FV1RQeVdVMDhSKytrL0hlWW5HZE9jMHYxeDRHYTR6emVWd3BJc1ZIVWlBMUdrWHh0NmJuUHlFb2psK09SMml0YVFJUU1TSHVmdW83UmpQSGoxNTU2bE0vYlA5TmhpZnB0ZGhQdlNrRnpLZ05reTdoNjZFeEJYMFJ4RlpFMHJxWWd0blNaZlhLRUlWQjdITUFIaC9zTkxOUVRFTjdVbHNMMm9kWjJIeVd6cFBIVHQ5aStGSUJjN0dqMDNRUVpjZERleVhPZmlQKzk0cStmS3ptSzhkZ0NqbDJCc1EwU3FCWEx2eVlFWmRuZDhrN3Z6eUUrZ2dmMy9vNHFkU1ExZG9uYzV3U09iL3RnZG5jUEozbG1kK25xemtPRnVrakxBd1ZWNWc5b0t1WGJSWCt0L081NGYyNVdZRzg4OWxDdWdpOTYwOENRdGZtNFBoYjZvSmZOMStSVHVMOXpqTnYzNFBTMG4yMjRmcFFPakFPRHczSmMzdGVnU21qbDd3V09BTUs1R1pONUNBUUdPOFhVbW9kQTc1angwY0o1T2NpeW5Rd1U1VkJNZW1UQkRySVdIdFVlVmlZM3RQbzBLWDdIbS9ISlJLU3pRWDN4NmdFRlRqNW5rc1pDbThLMk93VEttT05tVzlQbko1azJoUTBmZXJGSU1RUkJwSi9BM3BFMUY0dzNTT1lHMkw3K0MyQ1lDS05uNURZemM4MEtUaDZoaWF2K0Q4djRXZVUwMEJhbWNIbVZUTERtOFNUczVxZkRZaldxYVl2cXhFVUNjVk1YQWlBbWFEcFNBam9kQjcvOWNRZmlYSGJ0Z2FQNGgwTlVFL0YvcDhMMUFhZGxHMGFiYS9Bb2NsLzM2N0lNUCsxSDV0TkVBbmF6d1BQb3p5UldaQmxRR0pTZzZuTjAvejZFcEg3a1RkRGd0dFd6MHpCQlViMmRjLy9YTUNCSDNXRXd3bDZWeGhzK2RLeXBXNW1sQ0dGTFZFWml0RUVTMWxYUXJHWG9IcGNQZUUxNU1vdHVhNDJnbkJLSERudG9XS2JGOHFRMWVDbERpTzBCT2dtTkhxSk92YzFuYlYxS0NDd2xGdkJ3V2ZBc3dKZ0ZJbENFem9IR0x6YW5OdHdwSnJBS3dDaFJoL2w5RlhwbzZOdFRocGQ1cG41VUQrZGZUT0xMTk5vLzRBNkpBUkRTbzhUUjVIcUpoZXN0R0lybi9uanhpalF0ZGEyK2l0Q3pzN0NmTmsvaDdGekhRPT0tLXBtb2JqT3NhZElCekZmZVptQUNOVEE9PQ%3D%3D--06d71ee8a10127b2ef1d29446f4dbec74da837aa",
}

# url à surveiller
vinted_url = "https://www.vinted.fr/api/v2/catalog/items?page=1&per_page=96&search_text=jean%20501%20homme&search_id=16383489761&brand_ids[]=10&brand_ids[]=6413639&order=newest_first"

discord_webhook_url = "https://discord.com/api/webhooks/1273472019563941890/VR8TPuM5aENonzjU20VCF0XxNmYJch3J3PmmdyABxH5c1-_2trWMnenudYCIRnllVDx9"

response = vintedlib.fetch_vinted_data(vinted_url, headers, cookies)

seen_ids = {item["id"] for item in response}
fetch_count = 0

discordlib.send_alert_to_discord(discord_webhook_url, "on")

while True:

    time.sleep(240)
    print(f"{fetch_count} | recherche... 🐉🐉😶‍🌫️ | {len(seen_ids) - 96} items sniped")
    items = vintedlib.fetch_vinted_data(vinted_url, headers, cookies)
    fetch_count += 1
    for item in items:
        if item["id"] not in seen_ids:
            discordlib.send_item_to_discord(discord_webhook_url, item)
            seen_ids.add(item["id"])
            print(item["title"], "added to seen items")
            time.sleep(1)
