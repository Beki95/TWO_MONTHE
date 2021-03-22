import websockets
import asyncio
import json
import time


async def main():
    url = "wss://stream.binance.com:9443/stream?streams=btcusdt@miniTicker"
    async with websockets.connect(url) as client:
        while True:
            data = json.loads(await client.recv())["data"]
            event_time = time.localtime(data["E"] // 1000)
            event_time = f"{event_time.tm_hour}:{event_time.tm_min}:{event_time.tm_sec}"
            btc = data["c"]
            print(event_time, btc)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
