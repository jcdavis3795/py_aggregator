import praw


class Reddit:

    def __init__(self, client_id: str,
                 client_secret: str,
                 user_agent: str):
        self.conn = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)

    def subreddits_top(self, subreddits: list, time_range: str = 'day', max_results: int = 10) -> dict:
        """
        :param subreddits:
        :param time_range: Default all. Options - all, day, hour, month, week, year
        :param max_results: Default 10. Max number of results to return.
        :return: dict
        """
        return_dict = dict()

        for subreddit in subreddits:
            results = self.conn.subreddit(subreddit).top(time_filter=time_range, limit=max_results)
            return_dict = dict(**return_dict, **{
                f'{submission.subreddit.display_name} - {submission.id}': dict(title=submission.title, link=submission.url)
                for submission in results
            })

        return return_dict
