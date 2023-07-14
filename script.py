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

def export_data_to_mailchimp(data):
    url = f'https://usX.api.mailchimp.com/3.0/lists/{MAILCHIMP_LIST_ID}/members'
    headers = {'Authorization': f'Bearer {MAILCHIMP_API_KEY}'}

    for item in data:
        merge_fields = {
            'FNAME': item['first_name'],
            'LNAME': item['last_name'],
            'PHONE': item['phone'],
            'BIRTHDATE': item['birthdate'],
            'PRODUCT_USED': item['product_used'],
            'PRIVACY_POLICY': item['privacy_policy'],
            'DATA_USAGE': item['data_usage']
        }

        payload = {
            'email_address': '',  # Adicione o endereço de e-mail do destinatário
            'status': 'subscribed',
            'merge_fields': merge_fields,
            'tags': item['tags']
        }

        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            print('Data exported to Mailchimp successfully.')
        else:
            print('Failed to export data to Mailchimp.')

data_from_webflow = import_data_from_webflow()
export_data_to_mailchimp(data_from_webflow)
