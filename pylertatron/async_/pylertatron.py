from httpx import AsyncClient

from ..Pylertatron import Pylertatron
from ..commands import Command


class AsyncPylertatron(Pylertatron):
    def __init__(self, webhook_url, balance_ratio, api_key_name, client):
        if type(client) is not AsyncClient:
            raise TypeError("client must be of type httpx.AsyncClient, "
                            "use create_pylertatron() to create a Pylertatron instance")
        self.client: AsyncClient = client
        super().__init__(webhook_url, balance_ratio, api_key_name)

    async def send_alert(self, symbol: str, commands: list[Command], tags: list[str] = None):
        alert = self.generate_alert(symbol, commands, tags)
        await self.client.post(self.webhook_url, data=alert)


async def create_pylertatron(webhook_url, balance_ratio, api_key_name) -> Pylertatron:
    client = AsyncClient()
    return Pylertatron(webhook_url, balance_ratio, api_key_name, client=client)
