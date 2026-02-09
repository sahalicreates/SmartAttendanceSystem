import requests

# Replace with your bot token and chat ID
bot_token = '7544558349:AAGBqq8uGUkMWELhH0x3epbsLsP8g7BD1n0'
chat_id = '1540191367'
grp_chat_id = '-4543164219'
message = 'Hello, World!'

#To get chatid use the api given below
# api = f'https://api.telegram.org/bot{bot_token}/getUpdates'

api = f'https://telegram.rest/bot{bot_token}/sendMessage?chat_id={grp_chat_id}&text="Hello guys"'


# Set up the URL
# url = f"https://telegram.rest/bot{bot_token}/sendMessage"

# Prepare the data payload
payload = {
    "chat_id": chat_id,
    "text": message
}

# Send the POST request
response = requests.post(api, json=payload)

# Print the response
print(response.json())

# 7544558349:AAGBqq8uGUkMWELhH0x3epbsLsP8g7BD1n0

#https://api.telegram.org/bot<token>/METHOD_NAME