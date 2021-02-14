import feedparser


# scraping medium.com, a popular programming news/tutorials site

class MediumScrape:

    # writing the article titles and links of the first 5 articles under the tag 'programming'
    def medium_prog(self):
        feed_prog = feedparser.parse(
            "https://medium.com/feed/tag/programming"
        )
        with open('H:/code/content_agg/docs/attachment.json', 'a', encoding="utf-8") as f:
            f.write("PROGRAMMING TODAY: \n \n")
            for i in range(5):
                entry = feed_prog.entries[i]
                f.write(entry.title)
                f.write('\n')
                f.write(entry.link)
                f.write('\n \n')
            f.close()

    # writing the article titles and links of the first 5 articles under the tag 'python'
    def medium_py(self):
        feed_python = feedparser.parse(
            "https://medium.com/feed/tag/python"
        )
        with open('H:/code/content_agg/docs/attachment.json', 'a', encoding="utf-8") as f:
            f.write("PYTHON TODAY: \n \n")
            for i in range(5):
                entry = feed_python.entries[i]
                f.write(entry.title)
                f.write('\n')
                f.write(entry.link)
                f.write('\n \n')
            f.close()
