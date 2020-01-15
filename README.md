News Source Trust Tracker: Sentiment analysis for headlines from various news sources

News source headlines were scraped from their respective websites using Beautiful Soup (https://pypi.org/project/beautifulsoup4/), a Python library. They were scraped once per day for multiple months. Once the headlines were
acquired, sentiment analysis was conducted using Text Blob (https://textblob.readthedocs.io/en/dev/), a Python library for text processing. Text Blob scores strings on their polarity and subjectivity, which I used as the main axes of this visualization. 

The visualization was created using d3 (https://d3js.org/), a javascript library, as well as HTML and CSS.

If you find a bug, or if you would like more information, please feel free to reach out. 
