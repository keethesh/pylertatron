from alertatron import Command


class MarketOrder(Command):
    func_name = "market"

    def __new__(cls, side="buy", amount="0", position=None, reduceOnly=False):
        data = {
            "side": side,
            "amount": amount,
            "reduceOnly": str(reduceOnly).lower(),
        }
        if position is not None:
            data["position"] = position
        return cls.format(MarketOrder.func_name, data)


class Cancel(Command):
    func_name = "cancel"

    def __new__(cls, which, tag=None):
        if which is None:
            return ""

        data = {"which": which}
        if tag is not None:
            data["tag"] = tag

        return cls.format(Cancel.func_name, data)


class GridOrder(Command):
    func_name = "grid"

    def __new__(
        cls,
        buyAmount="0",
        sellAmount="0",
        grid="1%",
        gridUp="5%",
        gridDown="5%",
        postOnly=True,
        tag=None,
        background=True,
    ):
        data = {
            "buyAmount": buyAmount,
            "sellAmount": sellAmount,
            "grid": grid,
            "gridUp": gridUp,
            "gridDown": gridDown,
            "postOnly": str(postOnly).lower(),
            "background": str(background).lower(),
        }
        if tag is not None:
            data["tag"] = tag
        return cls.format(GridOrder.func_name, data)


class StopOrder(Command):
    func_name = "stopOrder"

    def __new__(
        cls,
        side="buy",
        amount="0",
        offset="1%",
        limit_offset=None,
        reduceOnly=True,
        trigger="mark",
        position=None,
        tag=None,
    ):
        data = {
            "side": side,
            "amount": amount,
            "offset": offset,
            "reduceOnly": str(reduceOnly).lower(),
            "trigger": trigger,
        }
        if position is not None:
            data["position"] = position
        if limit_offset is not None:
            data["limitOffset"] = limit_offset
        if tag is not None:
            data["tag"] = tag
        return cls.format(StopOrder.func_name, data)


class IcebergOrder(Command):
    func_name = "iceberg"

    def __new__(
        cls,
        limitPrice,
        side="buy",
        totalAmount="0",
        averageAmount="0",
        variance="0.1",
        timeLimit=None,
        reduceOnly=False,
        tag=None,
    ):
        data = {
            "side": side,
            "totalAmount": totalAmount,
            "averageAmount": averageAmount,
            "variance": variance,
            "reduceOnly": str(reduceOnly).lower(),
            "limitPrice": limitPrice,
        }
        if timeLimit is not None:
            data["timeLimit"] = timeLimit
        if tag is not None:
            data["tag"] = tag
        return cls.format(IcebergOrder.func_name, data)


class LimitOrder(Command):
    func_name = "limit"

    def __new__(
        cls,
        side="buy",
        amount="0",
        offset="1%",
        postOnly=True,
        reduceOnly=False,
        position=None,
        tag=None,
    ):
        data = {
            "side": side,
            "amount": amount,
            "offset": offset,
            "postOnly": str(postOnly).lower(),
            "reduceOnly": str(reduceOnly).lower(),
        }

        if position is not None:
            data["position"] = position
        if tag is not None:
            data["tag"] = tag
        return cls.format(LimitOrder.func_name, data)


class MarketMakerOrder(Command):
    func_name = "marketMaker"

    def __new__(
        cls,
        bidAmount="0",
        bidStep="5",
        bidCount="0",
        askAmount="0",
        askStep="5",
        askCount="0",
        spread="30",
        autoBalance=None,
        autoBalanceEvery="0",
        varyAmount="0",
        tag=None,
    ):
        data = {
            "bidAmount": bidAmount,
            "bidStep": bidStep,
            "bidCount": bidCount,
            "askAmount": askAmount,
            "askStep": askStep,
            "askCount": askCount,
            "spread": spread,
            "varyAmount": varyAmount,
        }
        if autoBalance is not None:
            data["autoBalance"] = str(autoBalance).lower()
        if autoBalanceEvery is not None:
            data["autoBalanceEvery"] = autoBalanceEvery
        if tag is not None:
            data["tag"] = tag
        return cls.format(MarketMakerOrder.func_name, data)


class OneCancelsOtherOrder(Command):
    func_name = "oneCancelsOther"

    def __new__(cls, which, tag=None):
        data = {"which": which}
        if tag is not None:
            data["tag"] = tag
        return cls.format(OneCancelsOtherOrder.func_name, data)


class PingPongOrder(Command):
    func_name = "pingPong"

    def __new__(
        cls,
        side="buy",
        amount="0",
        from_="0",
        to="100",
        orderCount="10",
        pongDistance="20",
        endless=False,
        pingAmount="0",
        pongAmount="0",
        easing="linear",
        postOnly=True,
        tag=None,
    ):
        data = {
            "side": side,
            "amount": amount,
            "from": from_,
            "to": to,
            "orderCount": orderCount,
            "pongDistance": pongDistance,
            "endless": str(endless).lower(),
            "pingAmount": pingAmount,
            "pongAmount": pongAmount,
            "easing": easing,
            "postOnly": str(postOnly).lower(),
        }
        if tag is not None:
            data["tag"] = tag
        return cls.format(PingPongOrder.func_name, data)


class ScaledOrder(Command):
    func_name = "scaled"

    def __new__(
        cls,
        side="buy",
        amount="0",
        from_="0",
        to="100",
        orderCount="10",
        easing="linear",
        method="base",
        varyAmount="0",
        varyPrice="0",
        position=None,
        postOnly=True,
        reduceOnly=False,
        tag=None,
        background=True,
    ):
        data = {
            "side": side,
            "amount": amount,
            "from": from_,
            "to": to,
            "orderCount": orderCount,
            "easing": easing,
            "method": method,
            "varyAmount": varyAmount,
            "varyPrice": varyPrice,
            "postOnly": str(postOnly).lower(),
            "reduceOnly": str(reduceOnly).lower(),
            "background": str(background).lower(),
        }
        if position is not None:
            data["position"] = position
        if tag is not None:
            data["tag"] = tag
        return cls.format(ScaledOrder.func_name, data)


class StopOrTakeProfitOrder(Command):
    func_name = "stopOrTakeProfit"

    def __new__(
        cls, side="buy", amount="0", tp="100", sl="100", tag=None, reduceOnly=False
    ):
        data = {
            "side": side,
            "amount": amount,
            "tp": tp,
            "sl": sl,
            "reduceOnly": str(reduceOnly).lower(),
        }
        if tag is not None:
            data["tag"] = tag
        return cls.format(StopOrTakeProfitOrder.func_name, data)


class TrailingLimitOrder(Command):
    func_name = "trailingLimit"

    def __new__(
        cls,
        side="buy",
        amount="0",
        minOffset="0.01%",
        maxOffset="0.03%",
        timeLimit=None,
        slippageLimit=None,
        onLimitAction="cancel",
        position=None,
        reduceOnly=False,
        postOnly=True,
        background=True,
        tag=None,
    ):
        data = {
            "side": side,
            "amount": amount,
            "minOffset": minOffset,
            "maxOffset": maxOffset,
            "onLimitAction": onLimitAction,
            "reduceOnly": str(reduceOnly).lower(),
            "postOnly": str(postOnly).lower(),
            "background": str(background).lower(),
        }
        if timeLimit is not None:
            data["timeLimit"] = timeLimit
        if slippageLimit is not None:
            data["slippageLimit"] = slippageLimit
        if position is not None:
            data["position"] = position
        if tag is not None:
            data["tag"] = tag
        return cls.format(TrailingLimitOrder.func_name, data)


class TrailingStopOrder(Command):
    func_name = "trailingStop"

    def __new__(
        cls,
        side="buy",
        amount="0",
        offset="0",
        limitOffset=None,
        reduceOnly=True,
        trigger="mark",
        trailingMethod="continuous",
        stepSize="0",
        maxSteps="0",
        position=None,
        tag=None,
        background=True,
    ):
        data = {
            "side": side,
            "amount": amount,
            "offset": offset,
            "reduceOnly": str(reduceOnly).lower(),
            "trigger": trigger,
            "trailingMethod": trailingMethod,
            "stepSize": stepSize,
            "maxSteps": maxSteps,
            "background": str(background).lower(),
        }
        if limitOffset is not None:
            data["limitOffset"] = limitOffset
        if position is not None:
            data["position"] = position
        if tag is not None:
            data["tag"] = tag
        return cls.format(TrailingStopOrder.func_name, data)


class TrailingTakeProfitOrder(Command):
    func_name = "trailingTakeProfit"

    def __new__(
        cls,
        side="buy",
        amount="0",
        triggerOffset="1%",
        offset="1%",
        limitOffset=None,
        reduceOnly=True,
        trigger="last",
        trailingMethod="continuous",
        stepSize="0",
        maxSteps="0",
        position=None,
        tag=None,
        background=True,
    ):
        data = {
            "side": side,
            "amount": amount,
            "triggerOffset": triggerOffset,
            "offset": offset,
            "reduceOnly": str(reduceOnly).lower(),
            "trigger": trigger,
            "trailingMethod": trailingMethod,
            "stepSize": stepSize,
            "maxSteps": maxSteps,
            "background": str(background).lower(),
        }
        if limitOffset is not None:
            data["limitOffset"] = limitOffset
        if position is not None:
            data["position"] = position
        if tag is not None:
            data["tag"] = tag
        return cls.format(TrailingTakeProfitOrder.func_name, data)


class TwapOrder(Command):
    func_name = "twap"

    def __new__(
        cls,
        side="buy",
        amount="0",
        orderCount="10",
        duration="60s",
        varyAmount=0,
        position=None,
        tag=None,
    ):
        data = {
            "side": side,
            "amount": amount,
            "orderCount": orderCount,
            "duration": duration,
            "varyAmount": varyAmount,
        }
        if position is not None:
            data["position"] = position
        if tag is not None:
            data["tag"] = tag
        return cls.format(TwapOrder.func_name, data)


class WaitingLimitOrder(Command):
    func_name = "waitingLimit"

    def __new__(
        cls,
        side="buy",
        amount="0",
        offset="1%",
        timeLimit=None,
        postOnly=True,
        reduceOnly=False,
        position=None,
        tag=None,
    ):
        data = {
            "side": side,
            "amount": amount,
            "offset": offset,
            "postOnly": str(postOnly).lower(),
            "reduceOnly": str(reduceOnly).lower(),
        }
        if timeLimit is not None:
            data["timeLimit"] = timeLimit
        if position is not None:
            data["position"] = position
        if tag is not None:
            data["tag"] = tag
        return cls.format(WaitingLimitOrder.func_name, data)
