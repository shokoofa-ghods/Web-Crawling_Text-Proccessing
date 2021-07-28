# IMDb-storyline-TextProccessing

### A Python program proccessing text of storylines for 250 top IMDb movies


At first the app needs to extract storyline text of movies via web crawlling using :
- BeautifulSoap
- RegEx

Then analysing and extracting the keywords of the prepared text through TextRank algorithm

Finally trying to find the common keywords employed on the each movie's storyline text
And to show the result by a weighted graph of which the weight refers to the number of common keywords, using :
- Netwokx

example of first top 5 movie's common words:

![image](https://user-images.githubusercontent.com/56467180/127338837-3bac9866-cc2e-4c7e-8877-f8acc3dd9dbc.png)
