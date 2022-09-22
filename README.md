# Shorten a bulk list of URLs with TinyURL

This repository presents a simple Python program that shortens a URL or a list of URLs by employing [TinyURL](https://tinyurl.com/) service. Before running this program, you need to obtain an API token from TinyURL at [here](https://tinyurl.com/app/settings/api). You should note that TinyURL is a paid service, so if you are using a Free plan, you will have some limitations such as 600 URLs/month when using API.

## How to run this program
First, you need to obtain an API token from TinyURL and insert it to line `34` in the `main.py`. Then, you have two options to run the program:

 - To shorten a URL, execute `$ python main.py -u "LONG_URL"`
 - To shorten a list of URLs, you need to insert those URLs to the `urls.txt`, and just execute the `main.py` without `-u` argument, i.e., `$ python main.py`

*Note:* when shortening a list of URLs, the results will be placed in the `short_urls.txt` where the short URLs together with their original ones are separated by a `\t` character.

## Links

 - Obtain API token - [https://tinyurl.com/app/settings/api](https://tinyurl.com/app/settings/api)
 - TinyURL OpenAPI - [https://tinyurl.com/app/dev](https://tinyurl.com/app/dev)

