import os
import platform
import json

import utils
from config import CONFIG_FILE, CONFIG_DIR, get_config
from scrapers import medium, reddit


def create_config():
    os.makedirs(CONFIG_DIR, exist_ok=True)
    with open(CONFIG_FILE, 'w') as f:
        f.write(json.dumps(dict(
            reddit_config=update_reddit_details(),
            email=update_email_details(),
            content_followed=update_content_followed()
        ), indent=2))


def update_content_followed():
    medium_tags = input('enter medium tags separated by commas: ').replace(' ', '').split(',')
    subreddits = input('enter subreddits separated by commas: ').replace(' ', '').split(',')
    return dict(medium_tags=medium_tags, subreddits=subreddits)


def update_email_details():
    sender_email_address = input('enter sender email address:')
    sender_email_password = input('enter sender email password:')
    receiver_email_address = input('enter receiving email address:')

    return dict(
        receiver_email=receiver_email_address, sender=dict(email=sender_email_address, password=sender_email_password)
    )


def update_reddit_details():
    reddit_client_id = input('enter reddit client id:')
    reddit_secret_key = input('enter reddit secret key:')
    reddit_username = input('enter reddit username:')
    os_name = platform.system().lower()
    reddit_user_agent = f'{os_name}.py_agg:v1.1 (by u/{reddit_username})'
    return dict(client_id=reddit_client_id, client_secret=reddit_secret_key, user_agent=reddit_user_agent)


def update():
    config = get_config()

    update_reddit = input('Update reddit config? y/n')[0].lower()
    if update_reddit == 'y':
        config['reddit'] = update_reddit_details()

    update_email = input('Update email details? y/n')[0].lower()
    if update_email == 'y':
        config['email'] = update_email_details()

    update_content = input('Update content followed? y/n')[0].lower()
    if update_content == 'y':
        config['content_followed'] = update_content_followed()

    with open(CONFIG_FILE, 'w') as f:
        f.write(json.dumps(config, indent=2))


def main():

    if not os.path.exists(CONFIG_FILE):
        # Function to create config. Ask user for each value. Create additional function to update config values
        create_config()

    scraper_results = dict()
    config = get_config()

    if medium_tags := config['content_followed']['medium_tags']:
        scraper_results['medium'] = medium.Medium.by_tags(medium_tags)

    if subreddits := config['content_followed']['subreddits']:
        reddit_conn = reddit.Reddit(**config['reddit_config'])
        scraper_results['reddit'] = reddit_conn.subreddits_top(subreddits=subreddits)

    if scraper_results:
        utils.send_results(
            config['email']['sender']['email'],
            config['email']['sender']['password'], config['email']['receiver_email'],
            scraper_results
        )


if __name__ == '__main__':
    main()

