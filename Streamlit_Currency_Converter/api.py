import requests

url = 'https://www.frankfurter.app/'

def call_api(url):
    """
    Function that will call a provide GET API endpoint url and return its status code and either its content or error message as a string

    Parameters
    ----------
    url : str
        URL of the GET API endpoint to be called

    Returns
    -------
    int
        API call response status code
    str
        Text from API call response
    """
    resp = requests.get(url)
    if resp.status_code == 200:
        return resp.json()
    else:
        return "There is an error with Frankfurter API"
