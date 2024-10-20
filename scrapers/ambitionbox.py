"""
Web Scraping Script for AmbitionBox

Description:
This Python script is designed to scrape top company by reviews in the given industry
from AmbitionBox using requests. The data collected includes "Company","Industry",
"Employee Count", "Age","Tag","Location","Rating","Review Count", which will be 
extracted from the website and stored in excel file.

Website:
[https://www.ambitionbox.com]

Important Notes:
- Please ensure you comply with the website's 'robots.txt' file and scraping 
  policies to avoid violating any terms of service.
- Use this script responsibly and ensure you're not overwhelming the website 
  with too many requests in a short period (implement delay or use proxies as needed).
- For educational purposes only. The script may need to be updated if the 
  website structure changes.

Requirements:
- pip install requests, openpyxl

Author:
Prajjwal Pathak | itspyguru
linkedin.com/in/itspyguru/
Python Developer, Ethical Hacker

Last Updated:
[9 September 2024]
"""

import requests
import json
import openpyxl
import time


def scrape_results_from_ambitionbox(page):
    url = "https://www.ambitionbox.com/servicegateway-ambitionbox/company-services/v0/listing/cards/search"

    payload = json.dumps(
        {
            "isFilterApplied": True,
            "industries": ["logistics"],
            "page": str(page),
            "sortBy": "popular",
            "limit": 50,
        }
    )
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "appid": "901",
        "cache-control": "no-cache",
        "content-type": "application/json",
        "cookie": "_t_ds=40f399c1719921056-4140f399c-040f399c; ak_bmsc=A425628766B873F9A5734AE78703161E~000000000000000000000000000000~YAAQDY0sMZpAhpqRAQAANusO1RndXi6srkLEy/Tfy/T0vhPbrX769p2057noGRR1oqhhf/2uPSHsm2h8Mc76zatv06lAEs/8JhcoUUUJpHfDhB6k61xi1x1rLy3mrp8TIxlNucMT5W97dNP0SPcIv7X5AAi1hPJHmNnjjFOjAxJMRFF0FHHyrLFoX+5yGcvk1M32GXKku6c6yF+1vioer7JpA+ZD4AvSO84mwNAjdcQ6urT94iAzzKWvGDaehEHWjBmnYcdvULE4G+l6KDlgfBdWzmYv9uAWTQDBdxbXODgtW5byhOVyMy4fDkP1nQ1u77u4kGfCtgkAM624VnNAZ+smMpMdSmURCtM7u0HTYSRfs2aUIEcduhhzIRceiawi1qo3c2K+S7+OzSm0V619sTFHYpPLO0YqRldY/M/GvcYEDp/pqi6owYs=; showChatbot=y; bm_mi=CB4A11D7AADBDB4B484CB31D080C8013~YAAQqdxVuMovDsCRAQAAqwIa1RnavB0jqexhOVACPUUYzm17lUCH1UQmj45lSqg9VgjerLCQa4GlZE5l8qUKQbHREcujMR2KoqP62BbKa5I1WvUZbXXaIxSiDMRYIDLtkH7MYs1fnpWuKjffrD/86q2gZBm3g2Uvzz+0nB++HT6xAK/eqi0Ev0bRF2zQNTDsx+47+7c8xXIVymBrhAHW7eiA/JVBqSua+3Ufu+eD8U0I7+VXYBwe4egyKsr3CaaPi1tgVCZn28ze9+1/OOyibQTsDLhQqELF1RXeJRzFOdBKh1sSWFPVtyLxXEK9NUfcbtDH4U5KbJBBn9nDPlhM6MO6jXX3V/Gj1mBYZJVnCQ==~1; bm_sv=DD14377E510F560D8E2120EEA2CDCA53~YAAQqdxVuMsvDsCRAQAAqwIa1RkTnAaD7bojGXwVq/I47VxOxkokgEeQtvENGUmupWxCAlWAKWbNHYM+xKeFtaFr5FlJ7tFmr+JCtHq47vznBYZCNDSfuxE/qVo0+dHYLQnTu++aqquzdQW0l3wXP4272cZbgQAaqW1gcBczmpnIyS8zvatWQRAG059lg9PPdIiLaBFXuAbLdvvft8hnlF9f+mop6x+6N5IzUXI6/8nxwHz8mYs2Ad8ePdoG0CCY9z7WaLkN~1; bm_sv=DD14377E510F560D8E2120EEA2CDCA53~YAAQTI0sMZWbcJeRAQAASCMc1RmC/A2MXQ23ucoClv2hVBu+euDGbfsDtVkOdV4IV0mPtxvAer6HFrHxUA07JDk0p375dg2JByiax/pm3VvBd/kA/ggn9JZx5zPR91csXbDNNmKwjzrAuatE0GnluC9sB086ukvutO3d7d1fSfoVkTd/kXfRwi5s7na/hvTtVnYwi4MO+17L46u8hAXjzcU90ykq1ZlJQ8lXX5sk82CHbL91+XwNHmwu0LuWr37tklLBEplq~1",
        "origin": "https://www.ambitionbox.com",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://www.ambitionbox.com/logistics-companies-in-india?page=4",
        "sec-ch-ua": '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "systemid": "loc",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()


wb = openpyxl.Workbook()
ws = wb.active
ws.append(
    [
        "Company",
        "Industry",
        "Employee Count",
        "Age",
        "Tag",
        "Location",
        "Rating",
        "Review Count",
    ]
)

for page in range(1, 14):
    results = scrape_results_from_ambitionbox(page)
    for card in results.get("cards", []):
        try:
            tag = card.get("tag", {}).get("Name", "")
        except:
            tag = ""
        try:
            location = card["topLocationDetail"].get("name", "")
        except:
            location = ""
        ws.append(
            [
                card["name"],
                card["primaryIndustry"],
                card["totalEmployees"],
                card["age"],
                tag,
                location,
                card["companyRating"],
                card["reviewCount"],
            ]
        )
    wb.save("ambitionbox.xlsx")
    print(f"Page {page} done")
    time.sleep(1)
print("All pages done")
