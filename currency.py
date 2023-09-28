from frankfurter import get_latest_rates, get_historical_rate

def round_rate(conversion_rate, from_currency, to_currency):
    """
    Function that will round an input float to 4 decimals places.

    Parameters
    ----------
    conversion_rate: float
        Rate to be rounded
    from_currency: string
        origin currency
    to_currency: string
        destination currency
    
    Returns
    -------
    float
        Rounded rate
    """
    conversion_rate, _ = get_latest_rates(from_currency, to_currency)
    if conversion_rate != 0:
        round_conversion = round(conversion_rate, 4)
        return round_conversion
    else:
        print(0)
    
def reverse_rate(conversion_rate, from_currency, to_currency):
    """
    Function that will calculate the inverse rate from the provided input rate.
    It will check if the provided input rate is not equal to zero.
    If it not the case, it will calculate the inverse rate and round it to 4 decimal places.
    Otherwise it will return zero.

    Parameters
    ----------
    conversion_rate: float
        Rate to be rounded
    from_currency: string
        origin currency
    to_currency: string
        destination currency

    Returns
    -------
    float
        Inverse of input FX conversion rate
    """
    inverse_rate = round(1/round_rate(conversion_rate, from_currency, to_currency), 4)
    return inverse_rate
    
def format_output(from_amount, from_currency, to_currency, conversion_rate, date):
    """
    Function that will take previously defined functions and return output message based on latest conversion rate.

    Parameters
    ----------
    from_amount: float
        input amount
    from_currency: string
        origin currency
    to_currency: string
        destination currency
    conversion_rate: float
        rounded rate
    date: date
        date of currency rate

    Returns
    -------
    string
        States latest conversion rate, origin currency, destination currency, date, converted amount and inverse rate.
    """
    final_rate = round_rate(conversion_rate, from_currency, to_currency)
    final_inverse = str(reverse_rate(conversion_rate, from_currency, to_currency))
    converted_amount = str(from_amount * final_rate)
    _, date = get_latest_rates(from_currency, to_currency)
    current_date = date
    output = ("The conversion rate on " + current_date + " from " + from_currency + " to " + to_currency + " was " + str(final_rate) + ".\n" + "So "
    + str(from_amount) + " in " + from_currency + " corresponds to " + converted_amount + " in " + to_currency + ".\n" + "The inverse rate was " + final_inverse)
    return output

def hist_format_output(from_amount, from_currency, to_currency, hist_conversion_rate, from_date):
    """
    Function that will take previously defined functions and return output message based on historical conversion rate.

    Parameters
    ----------
    from_amount: float
        input amount
    from_currency: string
        origin currency
    to_currency: string
        destination currency
    hist_conversion_rate: float
        rounded rate
    from_date: historical date
        date of currency rate

    Returns
    -------
    string
        States historical conversion rate, origin currency, destination currency, date, converted amount and inverse rate.
    """
    final_rate = round_rate(hist_conversion_rate, from_currency, to_currency)
    final_inverse = str(reverse_rate(hist_conversion_rate, from_currency, to_currency))
    converted_amount = str(from_amount * final_rate)
    _, from_date = get_historical_rate(from_currency, to_currency, from_date)
    hist_date = str(from_date)
    output = ("The conversion rate on " + hist_date + " from " + from_currency + " to " + to_currency + " was " + str(final_rate) + ".\n" + "So "
    + str(from_amount) + " in " + from_currency + " corresponds to " + converted_amount + " in " + to_currency + ".\n" + "The inverse rate was " + final_inverse)
    return output



