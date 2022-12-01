from .command import Command

__all__ = ['Comment', 'Space', 'Balance', 'Continue', 'DynamicTakeProfit', 'ExchangeSettings', 'Stop', 'Wait']


class Comment:
    def __new__(cls, comment):
        return f"# {comment}"


class Space:
    def __new__(cls):
        return "\n"


class Balance(Command):
    func_name = "balance"

    def __new__(cls):
        return "balance();"


class Continue(Command):
    func_name = "continue"

    def __new__(cls, _if, value=None):
        data = {"if": _if}
        if value is not None:
            data["value"] = value
        return cls.format(Continue.func_name, data)


class DynamicTakeProfit(Command):
    func_name = "dynamicTakeProfit"

    def __new__(
            cls,
            offset="e1%",
            size="100%p",
            cancelOtherOnFill=None,
            tag=None,
            postOnly=True,
            reduceOnly=True,
    ):
        data = {
            "offset": offset,
            "size": size,
            "postOnly": str(postOnly).lower(),
            "reduceOnly": str(reduceOnly).lower(),
        }
        if cancelOtherOnFill is None:
            data["cancelOtherOnFill"] = "none"
        if tag is not None:
            data["tag"] = tag
        return cls.format(DynamicTakeProfit.func_name, data)


class ExchangeSettings(Command):
    func_name = "exchangeSettings"

    def __new__(cls, leverage=None, max_order_size=None):
        if leverage is None and max_order_size is None:
            return ""
        data = {}
        if leverage is not None:
            data["leverage"] = leverage
        if max_order_size is not None:
            data["maxOrderSize"] = max_order_size
        return cls.format(ExchangeSettings.func_name, data)


class Stop(Command):
    func_name = "stop"

    def __new__(cls, _if, value=None):
        data = {"if": _if}
        if value is not None:
            data["value"] = value
        return cls.format(Stop.func_name, data)


class Wait(Command):
    func_name = "wait"

    def __new__(cls, duration="60s"):
        return f"wait({duration});"
