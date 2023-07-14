# Webflow-Mailchimp Data Automation

This repository contains a Python script that enables the automation of importing data from Webflow and exporting it to a Mailchimp audience. It provides a seamless integration between Webflow and Mailchimp, allowing for efficient data synchronization.

## Prerequisites

Before running the script, ensure you have the following:

- Python installed on your machine
- Dependencies installed: `requests` and `python-dotenv`

## Setup

1. Clone the repository:
   ```bash git clone https://github.com/your-username/webflow-mailchimp-data-automation.git```

2.Install the dependences:
   ```pip install requests python-dotenv```

3. Set up the required API keys:

Obtain your Webflow API key and update the `.env` file with `WEBFLOW_API_KEY=<your-webflow-api-key>`.
Obtain your Mailchimp API key and list ID, and update the `.env` file with `MAILCHIMP_API_KEY=<your-mailchimp-api-key>` and `MAILCHIMP_LIST_ID=<your-mailchimp-list-id>`.

## Usage

1. Customize the data processing and formatting logic in the `import_data_from_webflow()` function in `script.py` to match your specific requirements.

2. Run the script:
   ```python script.py```
The script will import data from Webflow, format it according to your logic, and export it to the specified 
Mailchimp audience.

## Notes

Make sure to keep the .env file containing the API keys and sensitive information private. Add it to the `.gitignore` file to prevent accidental exposure on public repositories.

For more information and details on the script implementation, refer to the comments within the `script.py` file.

## Contributing

Contributions are welcome! If you have any improvements or suggestions, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.


