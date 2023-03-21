import asyncio
import random
import string
import aiohttp


async def generate_ips(num_ips):
    ips = []
    for i in range(num_ips):
        a = random.randrange(0, 255, 1)
        b = random.randrange(0, 255, 1)
        c = random.randrange(0, 255, 1)
        d = random.randrange(0, 255, 1)
        ips.append(f"{a}.{b}.{c}.{d}")
    return ips


async def check_ip(ip):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"http://{ip}", timeout=5) as resp:
                if resp.status == 200:
                    text = await resp.text()
                    print(f"Live IP: {ip}")
                    with open("reversed.txt", "a") as f:
                        f.write(ip + "\n")
                else:
                    print(f"Dead IP: {ip}")
    except Exception:
        pass


async def check_ips(num_ips):
    ips = await generate_ips(num_ips)
    tasks = [asyncio.create_task(check_ip(ip)) for ip in ips]
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    threads = []
    thrd = 1000000
    num_ips = 15000
    print(f"Generating {num_ips} IPs...")
    asyncio.run(check_ips(num_ips))
