from scrapers import medium_scrape, reddit_scrape
import yagmail
import sys

# telling yagmail which address the message will be sent from
yag = yagmail.SMTP(user='', password='')

# initialize the reddit and medium objects
medium_obj = medium_scrape.MediumScrape()
reddit_obj = reddit_scrape.RedditScrape()


if __name__ == '__main__':

    medium_obj.medium_py()
    medium_obj.medium_prog()
    reddit_obj.daily_top()

    # open and read the content of the json file into the body variable, which will be the body of the message
    with open('H:/code/content_agg/docs/attachment.json', 'r', encoding="utf-8") as f:
        body = f.read()
        # even though the contents of the file are sent directly in text, I also attach the .json file to the message
        file = 'H:/code/content_agg/docs/attachment.json'

    f.close()

    # the email that should receive the message
    receiver = "jc.davis3795@gmail.com"
    yag.send(
        to=receiver,
        subject="Content Aggregator",
        contents=body,
        attachments=file
    )
    # just open the file in write mode and enter blank character into the file to clear it
    with open('H:/code/content_agg/docs/attachment.json', 'w') as f:
        f.write('')
        f.close()

    sys.exit()
