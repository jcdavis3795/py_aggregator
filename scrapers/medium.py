import feedparser


class Medium:
    # scraping medium.com, a popular programming news/tutorials site

    @staticmethod
    def by_tags(tags: list, max_results: int = 10):
        """Retrieve a link

        :param tags:
        :param max_results:
        :return:
        """

        return_dict = dict()

        for tag in tags:
            medium_feed = feedparser.parse(f"https://medium.com/feed/tag/{tag}")
            return_dict = dict(**return_dict, **{
                f'{tag} {i}': dict(title=medium_feed.entries[i].title, link=medium_feed.entries[i].link)
                for i in range(min(max_results, len(list(medium_feed.entries))))
            })

        return return_dict
