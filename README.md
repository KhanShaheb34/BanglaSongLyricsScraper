# BanglaSongLyricsScraper

Scrape 4000+ Bangla Song Lyrics with Title and Genre from [BanglaSongLyrics.com](https://banglasonglyrics.com/)

> I already uploaded lyrics dataset in [Kaggle/shakirulhasan/bangla-song-lyrics](https://www.kaggle.com/shakirulhasan/bangla-song-lyrics). You don't have to scrape it.

### Documentation

Run `python scrape.py filename.csv` to scrape all 4000+ lyrics. For help run `python scrape.py --help` or `python scrape.py -h`.

```
usage: python scrape.py [-h] [--start START] [--end END] [--verbose VERBOSE]
                        filename

Scrape Bangla song lyrics from https://banglasonglyrics.com/

positional arguments:
  filename           Filename for the csv file

optional arguments:
  -h, --help         show this help message and exit
  --start START      Select a starting page (default 0)
  --end END          Select an ending page (default 281)
  --verbose VERBOSE  0 = False, 1 = True (default 1)
```
