import requests

def get_auth_header():
    bearer_token = "<insert bearer token here>"
    return {"Authorization": f"Bearer {bearer_token}"}

tweet_id = "1340562560000000000"
api_url = "https://api.twitter.com/2/tweets/{tweet_id}"
response = requests.get(api_url, get_auth_header())

print(response.json())

