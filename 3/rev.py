import asyncio
import re
import sys
import os
import time
import socket
import aiohttp
import urllib3
import os.path
from os import path
from email.mime.text import MIMEText
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
os.system('clear || cls')

class xcol:
    LGREEN = '\033[38;2;129;199;116m'
    LRED = '\033[38;2;239;83;80m'
    RESET = '\u001B[0m'
    LBLUE = '\033[38;2;66;165;245m'
    GREY = '\033[38;2;158;158;158m'

class REV:
    def __init__(self, session):
        self.session = session

    async def reverse(self, cidr):
        total=""
        page = 0
        urx = f'https://rapiddns.io/s/{cidr}?full=1&down=1#result'
        try:
            async with self.session.get(urx) as r:
                resp = re.sub("<th scope=\"row \">.*",">>>>>>>>>>>>>>>>>>urx", await r.text()).replace ("<div style=\"margin: 0 8px;\">Total: <span style=\"color: #39cfca; \">","XP>>>>>>>>>>>>>").replace ("</span></div>","")
                urxc = resp.splitlines()
                urls = ""
                nm = 0
                for xc in urxc:
                    nm += 1
                    if ">>>>>>>>>>>>>>>>>>urx" in xc:
                        urls = urls+urxc[nm]+"\n"
                with open(os.path.join('', 'reversed.txt'), 'a') as output:
                    output.write(f'{urls.replace("<td>","").replace ("</td>","")}')
                print(f"[SAVED] : {cidr}")
        except Exception as e:
            print(e)

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        try:
            inpFile = 'liveip.txt'
            with open(inpFile) as urlList:
                argFile = urlList.read().splitlines()
            for data in argFile:
                rev = REV(session)
                tasks.append(asyncio.ensure_future(rev.reverse(data)))
            await asyncio.gather(*tasks)
        except:
            pass

if __name__ == '__main__':
    os.system('clear')
    asyncio.run(main())
    quit()
