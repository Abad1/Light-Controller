#Toggle.py
#Cody Abad

devIP = "IP"


import asyncio
from kasa import Discover

async def main():
    dev = await Discover.discover_single(devIP)
    await dev.update()
    if (dev.is_on):
        await dev.turn_off()
    else:
        await dev.turn_on()    
        

if __name__ == "__main__":
    asyncio.run(main())


