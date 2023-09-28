from api import call_api
from datetime import date
import json

url = "https://api.frankfurter.app"
currencies = "/currencies"
latest = "/latest"
historical = "/{from_date}"

def get_currencies_list():
    """
    Function that will call the relevant API endpoint from Frankfurter in order to get the list of available currencies.
    After the API call, it will perform a check to see if the API call was successful.
    If it is the case, it will load the response as JSON, extract the list of currency codes and return it as Python list.
    Otherwise it will return the value None.

    Parameters
    ----------
    None

    Returns
    -------
    list
        List of available currencies or None in case of error
    """
    endpoint = f"{url}{currencies}"
    response = call_api(url=endpoint)
    if response is not None:
        return(response)
    else:
        return None


def get_latest_rates(from_currency, to_currency):
    """
    Function that will call the relevant API endpoint from Frankfurter in order to get the latest conversion rate between the provided currencies. 
    After the API call, it will perform a check to see if the API call was successful.
    If it is the case, it will load the response as JSON, extract the latest conversion rate and the date and return them as 2 separate objects.
    Otherwise it will return the value None twice.

    Parameters
    ----------
    from_currency : str
        Code for the origin currency
    to_currency : str
        Code for the destination currency

    Returns
    -------
    str
        Date of latest FX conversion rate or None in case of error
    float
        Latest FX conversion rate or None in case of error
    """
    endpoint = f"{url}{latest}?from={from_currency}&to={to_currency}"
    response = call_api(url=endpoint)
    if "rates" in response:
        rates = response["rates"]
    if to_currency in rates:
        conversion_rate = rates[to_currency]
        date = response.get("date")
        return conversion_rate, date
    else:
        return None, None

def get_historical_rate(from_currency, to_currency, from_date):
    """
    Function that will call the relevant API endpoint from Frankfurter in order to get the conversion rate for the given currencies and date
    After the API call, it will perform a check to see if the API call was successful.
    If it is the case, it will load the response as JSON, extract the conversion rate and return it.
    Otherwise it will return the value None.

    Parameters
    ----------
    from_currency : str
        Code for the origin currency
    to_currency : str
        Code for the destination currency
    from_date : str
        Date when the conversion rate was recorded

    Returns
    -------
    float
        Latest FX conversion rate or None in case of error
    str
        Date of latest FX conversion rate or None in case of error
    """
    endpoint = f"{url}{historical}?from={from_currency}&to={to_currency}"
    response = call_api(url=endpoint)
    historical_rates = {}
    hist_conversion_rate = None
    if "rates" in response:
        historical_rates = response["rates"]
    if to_currency in historical_rates:
        hist_conversion_rate = historical_rates[to_currency]
        from_date = date(response.get("date"))
        return hist_conversion_rate, from_date
    else:
        return None, None



