"""
Web Scraping Script for BSE India Stock Exchange Website

Description:
This Python script is designed to scrape realtime bse summary and sensex trends.

Website:
[https://www.bseindia.com/index.html]

Important Notes:
- Please ensure you comply with the website's 'robots.txt' file and scraping 
  policies to avoid violating any terms of service.
- Use this script responsibly and ensure you're not overwhelming the website 
  with too many requests in a short period (implement delay or use proxies as needed).
- For educational purposes only. The script may need to be updated if the 
  website structure changes.

Requirements:
- pip install aiohttp, loguru

Author:
Prajjwal Pathak | itspyguru
linkedin.com/in/itspyguru/
Python Developer, Ethical Hacker

Last Updated:
[30 January 2024]
"""

import aiohttp
import asyncio
from loguru import logger
from datetime import datetime

headers = {
    "authority": "api.bseindia.com",
    "accept": "application/json, text/plain, */*",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "no-cache",
    "origin": "https://www.bseindia.com",
    "pragma": "no-cache",
    "referer": "https://www.bseindia.com/",
    "sec-ch-ua": '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": '"Android"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36",
}


async def get_bse_response(session, url):
    logger.info(f"Scraping : {url=}")
    async with session.get(url, headers=headers) as response:
        if response.status == 200:
            return await response.json()

        return {}


async def fetch_bse_summary():
    try:
        realtime_bse = (
            "https://api.bseindia.com/RealTimeBseIndiaAPI/api/GetSensexData/w"
        )
        market_cap = "https://api.bseindia.com/BseIndiaAPI/api/MarketCap/w?code=16"
        announcements = "https://api.bseindia.com/BseIndiaAPI/api/Ann/w?code=16"
        volume_toppers = "https://api.bseindia.com/BseIndiaAPI/api/VolTopper/w?code=16"
        heatmap = "https://api.bseindia.com/BseIndiaAPI/api/HeatMapData/w?flag=HEAT&alpha=D&indexcode=16&random=18920241526"
        index_contribution = (
            "https://api.bseindia.com/BseIndiaAPI/api/IndexContri/w?code=16"
        )
        market_stat = "https://api.bseindia.com/BseIndiaAPI/api/MarketStat2/w"
        listing_stat = "https://api.bseindia.com/BseIndiaAPI/api/ListingStat/w"

        async with aiohttp.ClientSession() as session:
            tasks = [
                get_bse_response(session, realtime_bse),
                get_bse_response(session, market_cap),
                get_bse_response(session, announcements),
                get_bse_response(session, volume_toppers),
                get_bse_response(session, heatmap),
                get_bse_response(session, index_contribution),
                get_bse_response(session, market_stat),
                get_bse_response(session, listing_stat),
            ]

            responses = await asyncio.gather(*tasks)

            heatmap = responses[4].replace("bseindia$#$", "").split("|")
            heatmap = [item.split(",") for item in heatmap if item and "," in item]

            return {
                "scraped_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "realtime_bse": responses[0],
                "market_cap": responses[1],
                "announcements": responses[2],
                "volume_toppers": responses[3],
                "heatmap": heatmap,
                "index_contribution": responses[5],
                "market_stat": responses[6],
                "listing_stat": responses[7],
            }
    except Exception as e:
        logger.error(f"Error in fetching realtime BSE data: {e}")
        return {}


print(asyncio.run(fetch_bse_summary()))
