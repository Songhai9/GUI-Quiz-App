import requests

quiz_endpoint = "https://opentdb.com/api.php"
parameters = {
    'amount':10,
    'type': 'boolean'
}
question_data = requests.get(url=quiz_endpoint, params=parameters).json()["results"]

