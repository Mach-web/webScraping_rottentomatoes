# webScraping_rottentomatoes
Website Scraped: rottentomatoes.com
This folder was first created through 'scrapy startproject' command and therefore has many dependent files that I did not necessarily create. The file I worked with are found in 'rotten_tomatoes/spiders' folder.

rotten.py
Run the following command in virtual environment: scrapy crawl rotten -O rotten.csv This command crawls the website defined in the file and stores the results in a csv file. Scrapy is able to move to the description page of a movie.
