import requests
import os
from dotenv import load_dotenv

load_dotenv()

WEBFLOW_API_KEY = os.getenv("WEBFLOW_API_KEY")
MAILCHIMP_API_KEY = os.getenv("MAILCHIMP_API_KEY")
MAILCHIMP_LIST_ID = os.getenv("MAILCHIMP_LIST_ID")

def import_data_from_webflow():
    url = 'https://api.webflow.com/collections/<collection-id>/items'
    headers = {'Authorization': f'Bearer {WEBFLOW_API_KEY}'}

    response = requests.get(url, headers=headers)
    data = response.json()

    # Process and format the data as needed
    formatted_data = []

    for item in data['items']:
        formatted_item = {
            'first_name': item['first_name'],
            'last_name': item['last_name'],
            'phone': item['phone'],
            'birthdate': item['birthdate'],
            'product_used': item['product_used'],
            'privacy_policy': item['privacy_policy'],
            'data_usage': item['data_usage'],
            'tags': ['Webflow Form', '<site-name>']  # Adicione aqui o nome do site específico
        }

        formatted_data.append(formatted_item)

    return formatted_data
