from httpx import Client

from ..alert import Alert
from ..commands.command import Command


class Pylertatron:
    def __init__(self, webhook_url, balance_ratio, api_key_name, client):
        self.webhook_url: str = webhook_url
        self.client: Client = client
        self.balance_ratio: float = balance_ratio
        self.api_key_name: str = api_key_name

    def send_alert(self, symbol: str, commands: list[Command], tags: list[str] = None):
        if tags is None:
            tags = ["bot"]
        alert = Alert(self.api_key_name, symbol, commands, tags)
        self.client.post(self.webhook_url, data=alert)


def create_pylertatron(webhook_url, balance_ratio, api_key_name) -> Pylertatron:
    client = Client()
    return Pylertatron(webhook_url, balance_ratio, api_key_name, client=client)
