# Objective
This tutorial aims to show how to use the Python programming language to web scrape a website. Specifically, we will use the requests and Beautiful Soup libraries to scrape and parse data from companiesmarketcap.com and retrieve the “Largest Companies by Market Cap”.

We will learn how to scale the web scraping process by first retrieving the first company/row of the table, then all companies on the website’s first page, and finally, all 6024 companies from multiple pages. Once the scraping process is complete, we will preprocess the dataset and transform it into a more readable format before using matplotlib to visualise the most important information.

# Web Scraping Workflow
The workflow for web scraping with Python can be divided into the following three steps:

Obtaining the HTML: Firstly, we need to send an HTTP request to the web page server that we want to scrape. If the request is successful, the server will respond with the HTML content of the page.

Parsing the HTML: Most of the obtained HTML data is nested, making it difficult to extract information using stand string processing techniques. Instead, we need a parser, i.e. an algorithm designed to parse the HTML and create a parse/syntax tree of the HTML data.

Extracting the Data: Once the syntax tree is created, we need to navigate it and retrieve the information that we are interested in

To complete those steps, we need two third-party Python libraries:

Requests: a simple but powerful library for sending all kinds of HTTP requests to a web server,

Beautiful Soup: a library for parsing HTML and XML documents. It works with a user-selected parser to provide idiomatic ways of navigating, searching, and modifying the parse tree.
