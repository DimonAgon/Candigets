
import asyncio

from db import main as db_main
from bot import main as bot_main
from ad_collector.ad_collector import *
from ad_transmitter.ad_transmitter import *
from ad_deletor.ad_deletor import *

import os


async def collect_transmit_delete():
    delay = int(os.getenv('COLLECTING_TRANSMITTING_DELETING_DELAY'))
    while True:
        await AdCollector.collect_all_demands_ads()
        await AdTransmitter.trasmit_ads()
        await AdDeletor.delete_depleted_demands_and_ads()
        await asyncio.sleep(delay)

def main():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(db_main.main())
    loop.create_task(bot_main.main())
    loop.create_task(collect_transmit_delete())
    loop.run_forever()

if __name__ == "__main__":
    main()


