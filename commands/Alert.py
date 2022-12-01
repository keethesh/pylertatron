class Alert:
    def __new__(cls, api_key_name, symbol, commands=None, tags=None):
        if commands is None:
            commands = []
        if tags is None:
            tags = ["bot"]

        string = f"{api_key_name}({symbol}) {{\n"
        for command in commands:
            string += f"    {command}\n"
        string += "}"

        for tag in tags:
            string += f"\n#{tag}"
        return string
