import praw

# using praw to access the reddit api with our client key and secret key
reddit = praw.Reddit(client_id='Qhb0z9XPv8moKQ',
                     client_secret='bxlHri4EHzYTd5ZH7YRFYjuPqldEzg',
                     user_agent='windows.agg_content:v1.0 (by u/BlueMilk_and_Wookies)'
                     )


# using reddit's api to write the titles and links to the top 10 submissions across the specified subreddits
class RedditScrape:

    def daily_top(self):

        with open('H:/code/content_agg/docs/attachment.json', 'a', encoding="utf-8") as f:
            f.write("TODAY'S TOP REDDIT SUBMISSIONS: \n \n")
            # this is the string where the subreddits, sorting process and limit of submissions are declared
            for submission in reddit.subreddit('learnpython+Python+learnprogramming').top('day', limit=10):
                    f.write(submission.title)
                    f.write('\n')
                    f.write(submission.url)
                    f.write('\n \n')
            f.close()
