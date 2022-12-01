from .commands import Command


class Pylertatron:
    def __init__(self, webhook_url, balance_ratio, api_key_name):
        self.webhook_url: str = webhook_url
        self.balance_ratio: float = balance_ratio
        self.api_key_name: str = api_key_name

    def generate_alert(self, symbol: str, commands: list[Command], tags: list[str] = None):
        if commands is None:
            commands = []
        if tags is None:
            tags = ["bot"]

        string = f"{self.api_key_name}({symbol}) {{\n"
        for command in commands:
            string += f"    {command}\n"
        string += "}"

        for tag in tags:
            string += f"\n#{tag}"
        return string
