Teamwork project with [v-nafise](https://github.com/v-nafiseh/textProcessing)
## IMDb-storyline-TextProccessing 

#### A Python program web crawling and text proccessing of storylines for 250 top IMDb movies


At first the app needs to extract storyline text of movies via web crawlling using :
- BeautifulSoap
+ RegEx

Then analysing and extracting the keywords of the prepared text through TextRank algorithm + text proccessing like tokenizing, deleting stopwords and lemmatizing are implemented on story-line text of each movie

After that trying to find the common keywords employed on each movie's storyline text
And to show the result by a weighted graph in which the weight refers to the number of common keywords and the nodes are movies, using :
- Netwokrx

Finally the weighted graph is stored in a csv file.

output example of 250 movie's common words computed graph:


![Figure_1 (1)](https://user-images.githubusercontent.com/56467180/133266167-f70cc948-5028-48d8-9cf0-6828aae4cf4b.png)

</br>
 

## Digikala-Offers Scraping 

#### A Python program scraping the special offers of products and showing the results in a web using django framework 

technologies used in this app are:
+ craping with BeautifulSoup library
+ using regex for extracting exact details
+ saving files into json and csv format file


+ using django fixtures for populating database with the data derived from previous steps
