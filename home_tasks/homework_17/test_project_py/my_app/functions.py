# import necessary modules
import requests
import json
import os
import argparse
import logging

# set the logging level depending on the passed value
def configure_logging(verbosity):
    if verbosity == 0:
        logging.basicConfig(level=logging.WARNING)
    elif verbosity == 1:
        logging.basicConfig(level=logging.INFO)
    elif verbosity >= 2:
        logging.basicConfig(level=logging.DEBUG)
        
    # adding handler for CLI
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)

def main():
    parser = argparse.ArgumentParser(description='Script for fetching data from a URL and logging information.')
    parser.add_argument('url', type=str, help='URL to fetch data from')
    parser.add_argument('destination', type=str, help='Path to the destination file')
    parser.add_argument('-v', '--verbose', action='count', default=0, help='Increase verbosity (can be used multiple times)')

    args = parser.parse_args()
    configure_logging(args.verbose)
    get_data_json(args.url, args.destination)

def get_data_json(url, destination_file, verbosity=0):
    # adding "data" service folder on the same level with the current script
    data_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
    
    if not url:
        logging.error("!!! Parameter 'url' was not passed !!!")
        return
    if not isinstance(url, str):
        logging.warning("The 'url' parameter must be a string (website address)")
        return

    # define path for file where the data will be written
    destination_file = os.path.join(data_folder, destination_file)
    
    try:
        response = requests.get(url)
        response.raise_for_status()

        posts = response.json()
        users_posts_list = [{"userId": post.get("userId"), "postId": post.get("id")} for post in posts]

        # add data service folder if it doesn't exist
        os.makedirs(data_folder, exist_ok=True)

        with open(destination_file, "w") as file:
            json.dump(users_posts_list, file)
        logging.info(f"Users and their Posts written to file: {destination_file}")
        if logging.getLogger().getEffectiveLevel() == logging.DEBUG:
            print("Information about data written to file:")
            for entry in users_posts_list:
                print(entry)
    except requests.exceptions.RequestException as e:
        logging.error(f"Error: {e}")

if __name__ == '__main__':
    main()
