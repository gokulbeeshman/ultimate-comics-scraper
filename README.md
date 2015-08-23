# Ultimate Comics Scraper

### Project Aims:

* Simple tool to build a database of all popular webcomics - that is **multithreaded** and works even on bad networks
* Simple HTML page that lets you view all comics in a sequential/ random manner with all the original info

### Project Todos:
* Locally storing comics that have been downloaded already and the related information (like author, alt text etc)
* Making a page that lets viewers browse comics at convenience
* Completing download functions for a few comics
* Adding interface for users

### Comics supported as of now:
* XKCD
* Dog House Diaries
* Saturday Morning Breakfast Cereal
* Cyanide & Happiness
* Channelate
* PHD Comics

### Why I'm making this:

I've found several webcomic scraper on the internet - but  **not even a single one was usable** - they just dumped images, didn't account for timeouts or have any error handling. Most of them would crash halfway and were extremely slow.

### Usage instructions:

Use the foll if you don't have the Beautiful Soup library
> pip install BeautifulSoup4


Code written for Python 3. May need some minor changes for working in Python 2
Worse, there wasn't any good way for browsing the comics. Valuable extra jokes like XKCD's alt text were lost.
