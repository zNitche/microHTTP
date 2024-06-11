import asyncio
import json
import network
from microHTTP import MicroHttpClient


async def run_examples():
    client = MicroHttpClient(logging=False)

    res = await client.get("httpbin.org", "/ip")
    print(f"GET -> status: {res.status_code} -> {res.body}")

    dummy_data = json.dumps({"data": "test"})
    res = await client.send("httpbin.org", "/anything", method="POST", data=dummy_data)
    print(f"POST -> status: {res.status_code} -> {res.body}")


def load_env():
    print("loading env config...")

    with open("/env.json", "r") as env_file:
        data = json.loads(env_file.read())

    print("config has been loaded...")
    return data


def connect_to_network():
    env_data = load_env()

    print("enabling wlan...")
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    print("connecting to network...")
    wlan.connect(env_data["WIFI_SSID"], env_data["WIFI_PASSWORD"])

    print("connected to network...")


def main():
    connect_to_network()
    asyncio.run(run_examples())


if __name__ == '__main__':
    main()
