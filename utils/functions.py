from typing import List


def postprocess(data, tickers: List[str]) -> dict:
    """Post process results because of the way it has been organized."""

    data.dropna(axis=1, inplace=True)
    result = dict({ticker: dict() for ticker in tickers})

    try:
        for key, value in data.to_dict().items():
            if isinstance(key, tuple):
                (action, ticker) = key
                result[ticker][action] = value
            else:
                result[tickers[0]][key] = value
    except ValueError as e:
        raise e

    return result
