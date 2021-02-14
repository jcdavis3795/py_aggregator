# content_agg

	This program aggregates content from medium.com and reddit.com into a single file, which is sent to the
user's email. I accomplished this with feedparser(medium) and praw(reddit) to grab the content, and yagmail to mail it to myself. 

I attempted to organize the project in a modular way, with the intention of later adding more websites to this content aggregator without altering any the source code other than inserting another function call in agg.py.

	The focus of this aggregator is on python and programming news/tutorials. I may later add other 
programming websites or news from other categories such as sports/weather. For now however, these were the two sites I felt I wanted to have in one place.

	There is not a lot of code and I have commented most of it to make it self explanatory. The only thing you would need to do to make it ready
for your own use is adjust the path 'H:/code/content_agg/docs/attachment.json' to match the path that you have content_agg in. Then, in agg.py, you need to change the values in 'yagmail.SMTP()' to match your sender's email and password, and the value of 'reciever' to your recieveing email.
