# set_proxies.py
# https://github.com/jjaacckk
# 2021-03-25

from os import getenv, environ
from dotenv import load_dotenv
from requests import get as requests_get


def getIP() -> str:
    # gets IP address for testing purposes
    r = requests_get("https://api.ipify.org")
    IP = r.text
    r.close()
    return IP


# loads variables from the .env file containing the NordVPN credentials into the environment
load_dotenv()

# list of NordVPN's SOCKS5 hosts
hosts = [
    "amsterdam.nl.socks.nordhold.net",
    "atlanta.us.socks.nordhold.net",
    "dallas.us.socks.nordhold.net",
    "dublin.ie.socks.nordhold.net",
    "ie.socks.nordhold.net",
    "los-angeles.us.socks.nordhold.net",
    "nl.socks.nordhold.net",
    "se.socks.nordhold.net",
    "stockholm.se.socks.nordhold.net",
    "us.socks.nordhold.net",
]

# choose host from 'hosts' list above
host = hosts[0]

# NordVPN's SOCKS5 port
port = "1080"

# create a .env file with your NordVPN username (NORD_USERNAME) and password (NORD_PASSWORD)
nord_username = getenv("NORD_USERNAME")
nord_password = getenv("NORD_PASSWORD")

# prints unmasked IP
print("unmasked IP:", getIP())

print("setting proxies....")

# environment variables for http and https proxies
environ['HTTP_PROXY'] = f"socks5h://{nord_username}:{nord_password}@{host}:{port}"
environ['HTTPS_PROXY'] = f"socks5h://{nord_username}:{nord_password}@{host}:{port}"

# prints masked IP
print("masked IP:", getIP())
