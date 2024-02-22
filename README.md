# Telegram Scraping Script

This script allows you to scrape data from Telegram channels and categorize them based on different topics. It can be used to save time and effort by aggregating information from multiple channels into a single platform.

## Prerequisites

Before using the script, ensure that you have the following prerequisites installed:

- Python 3.x
- Python packages: telethon, firebase-admin, and any other necessary dependencies (provide a requirements.txt file if applicable)

## Setup

1. Clone or download the repository to your local machine.

2. Install the required Python packages by running the following command:

```pip install -r requirements.txt```

3. Obtain Telegram API credentials:

- Create a Telegram application at https://my.telegram.org/auth.
- Note down the **API_ID** and **API_HASH** provided for your application.


4. Update the configuration file:

- Open the `config.py` file in a text editor.
- Enter your Telegram API credentials (`API_ID` and `API_HASH`).
- Specify the desired channels to scrape by adding their names or IDs to the `CHANNELS` list.
- Customize any other relevant settings as necessary.

## Usage

1. Run the script by executing the following command:

```python index.py ```


## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository.

2. Create a new branch for your feature or bug fix.

3. Make your changes and commit them.

4. Push your changes to your fork.

5. Submit a pull request to the main repository.
