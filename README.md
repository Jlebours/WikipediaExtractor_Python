# Wikipedia Matrix Python

Wikipedia Matrix is a table extractor by means : HTML.
The aim of this project is to create a new version of extractor and compare the results 
with previous version of the project that have been made
in the last years by the students of Master degree in order to make a global review. 

The aim of the project was to extract as many relevant tables as possible from wikipedia links, the output format being csv.
We must now analyse the quality of the  data extractor HTML in order to
draw conclusions and propose areas for improvement while correcting any problems that arise.

Like any project, we have several different versions and the aim is to improve it,
from version to version over time to make it more powerful and better than the other versions. 
The current objective is to have a better extractor than the other versions.
The previous versions were in Java and now we have to make it in Python.

## Getting Started
clone https://github.com/Jlebours/WikipediaExtractor_Python.git for development and testing purposes.

## Prerequisites
### For Users
* Python interpreter 3.8 or 3.9
* Python IDE : PyCharm, Visual Studio Code, etc..
* for installing and testing we are inviting you to click on, this below link
[Install.md](https://github.com/Jlebours/WikipediaExtractor_Python/blob/master/INSTALL.md)




### For Developers
After having those prerequisites above you should add these below :
* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) is a Python library for working with real-world HTML.
* [Pandas](https://pandas.pydata.org/) is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool,
built on top of the Python programming language.
* [Requests](https://requests.readthedocs.io/en/master/) is an elegant and simple HTTP library for Python, built for human beings.
* [Os](https://docs.python.org/3/library/os.html/) this module provides a portable way of using operating system dependent functionality
* [urllib.request ](https://docs.python.org/3/library/urllib.request.html#module-urllib.request) The urllib.request module defines functions and classes which help in opening URLs (mostly HTTP) in a complex world — basic and digest authentication, redirections, cookies and more.
 

## Functionalities of  the application
* extraction of csv files through tables from wikipedia pages whose urls are in the wikiurls.txt file of the inputdata directory
* implementation of some tests to verify a good extraction 
* statistics on extracted files and tables not taken into account according to the selection criteria of the tables to be extracted
* automatic testing of file extraction quality , these tests will show also the  weaknesses of the extractor.

## Authors
As we have already said it this project has been developed in Java by those students :
* Jocelin DEGNI
* Yann ATTOUBE
* Anderson KONAN
* Kiko DAGNOGO

This team improved already their work in Java too :

* Emmanuel CHAUVEL 
* Narcisse KOUADIO
* Oceane THELISMA
* Noussi AMAL
* Karima GRAMI

Now we make a review of the project in Python :
* Johan LE BOURSICAUD
* Léo VARIERAS
* Rabeaa KESSAL
* Karla ROSAS
