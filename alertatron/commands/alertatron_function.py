class AlertatronFunction:
    @staticmethod
    def format(func_name, data):
        return f"{func_name}({', '.join(f'{k}={v}' for k, v in data.items())});"
