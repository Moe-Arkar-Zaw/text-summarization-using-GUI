import tkinter as tk
import nltk # natural language processing toolkit
from textblob import TextBlob # text processing of NLP capabilities
from newspaper import Article, ArticleException # article for web scraping and ArticleException for error handling

# function to summarize the article from the provided URL
def summarize():

    url = url_text.get('1.0', 'end').strip()

    # article processing
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    
    # enable text widgets to manipulate content
    title.config(state='normal')
    author.config(state='normal')
    publication.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')

    # clear previous content and insert new content
    title.delete('1.0', 'end')
    title.insert('1.0', str(article.title) if article.title else "N/A")

    author.delete('1.0', 'end')
    author.insert('1.0', str(article.authors) if article.authors else "N/A")

    publication.delete('1.0', 'end')
    publication.insert('1.0',str(article.publish_date) if article.publish_date else "Unknown")

    summary.delete('1.0', 'end')
    summary.insert('1.0', str(article.summary) if article.summary else "No summary avalible")

    analysis = TextBlob(article.text)
    sentiment.delete('1.0', 'end')
    polarity = analysis.sentiment.polarity
    sentiment_text = f'Polarity: {polarity:.2f}, Sentiment: {"positive" if polarity > 0 else "negative" if polarity < 0 else "neutral"}'
    sentiment.insert('1.0', sentiment_text)

    # disable text widgets to prevent user editing
    title.config(state='disabled')
    author.config(state='disabled')
    publication.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state='disabled')



# Initialize the main application window
root = tk.Tk()
root.title("News Summarizer")
root.geometry('1200x600')

title_label = tk.Label(root, text="Title")
title_label.pack()

title = tk.Text(root, height=1, width=140)
title.config(state='disabled', bg="#bfa6a6")
title.pack()

author_label = tk.Label(root, text="Authors")
author_label.pack()

author = tk.Text(root, height=1, width=140)
author.config(state='disabled', bg="#bfa6a6")
author.pack()

publication_label = tk.Label(root, text="Publication Date")
publication_label.pack()

publication = tk.Text(root, height=1, width=140)
publication.config(state='disabled', bg="#bfa6a6")
publication.pack()

summary_label = tk.Label(root, text="Summary")
summary_label.pack()

summary = tk.Text(root, height=15, width=140)
summary.config(state='disabled', bg="#bfa6a6")
summary.pack()

sentiment_label = tk.Label(root, text="Sentiment Analysis")
sentiment_label.pack()

sentiment = tk.Text(root, height=1, width=140)
sentiment.config(state='disabled', bg="#bfa6a6")
sentiment.pack()

url_label = tk.Label(root, text="URL")
url_label.pack()

url_text = tk.Text(root, height=1, width=140)
url_text.pack()

button = tk.Button(root, text="Summarize", command=summarize)
button.pack()

root.mainloop()
