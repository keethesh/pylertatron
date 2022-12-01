from httpx import AsyncClient

from ..alert import Alert
from ..commands.command import Command


class Pylertatron:
    def __init__(self, webhook_url, balance_ratio, api_key_name, client):
        if type(client) is not AsyncClient:
            raise TypeError("client must be of type httpx.AsyncClient, "
                            "use create_pylertatron() to create a Pylertatron instance")
        self.webhook_url: str = webhook_url
        self.client: AsyncClient = client
        self.balance_ratio: float = balance_ratio
        self.api_key_name: str = api_key_name

    async def send_alert(self, symbol: str, commands: list[Command], tags: list[str] = None):
        if tags is None:
            tags = ["bot"]
        alert = Alert(self.api_key_name, symbol, commands, tags)
        await self.client.post(self.webhook_url, data=alert)


async def create_pylertatron(webhook_url, balance_ratio, api_key_name) -> Pylertatron:
    client = AsyncClient()
    return Pylertatron(webhook_url, balance_ratio, api_key_name, client=client)
