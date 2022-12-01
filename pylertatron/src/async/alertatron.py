from httpx import AsyncClient

from pylertatron import Alert, Command


class Alertatron:
    def __init__(self, webhook_url, balance_ratio, api_key_name, client):
        self.webhook_url: str = webhook_url
        self.client: AsyncClient = client
        self.balance_ratio: float = balance_ratio
        self.api_key_name: str = api_key_name

    async def send_alert(self, symbol: str, commands: list[Command], tags: list[str] = None):
        if tags is None:
            tags = ["bot"]
        alert = Alert(self.api_key_name, symbol, commands, tags)
        await self.client.post(self.webhook_url, data=alert)


async def create_alertatron(webhook_url, balance_ratio, api_key_name) -> Alertatron:
    client = AsyncClient()
    return Alertatron(webhook_url, balance_ratio, api_key_name, client=client)
