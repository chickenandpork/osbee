"""Connect to an OSBee and parse/dump status (the /jc method), showing we understand that OSBee."""

import aiohttp
import asyncio
from json import dumps
from osbee import OSBeeAPI


async def main():
    async with aiohttp.ClientSession() as client:

        host = "192.168.0.1"
        token = "opendoor"  # default password for OSBee

        # The (0) (index) in fetch_data didn't pan out, may disappear
        body = await OSBeeAPI(host, 30, token, client).fetch_data(0)

        print(dumps(body, indent=4, sort_keys=True))


asyncio.run(main())
