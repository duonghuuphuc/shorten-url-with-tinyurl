import http.client
import json
import string
import random
import time
import argparse


def generate_random_alias(length=7):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))


def generate_short_url(url, api_token=None, tinyurl_domain="tiny.one"):
    if api_token is not None and url is not None:
        conn = http.client.HTTPSConnection("api.tinyurl.com")
        headers = {
            'Authorization': 'Bearer ' + api_token,
            'Content-Type': 'application/json'
        }
        payload = json.dumps({
            "url": str(url),
            "domain": str(tinyurl_domain),
            "alias": str(generate_random_alias())
        })
        conn.request("POST", "/create", payload, headers)
        res = conn.getresponse()
        data = json.loads(res.read().decode("utf-8"))
        short_url = data.get('data').get('tiny_url')
        return str(short_url)


def main():
    # configuration
    api_token = 'INSERT_API_TOKEN_HERE'
    tinyurl_domain = "tiny.one"  # tinyurl.com, tiny.one, rotf.lol

    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "-url", help="Place a correct URL between a pair of quotation marks")
    args = parser.parse_args()

    # Case 1: shorten one URL only
    if args.u is not None:
        print(generate_short_url(url=args.u, api_token=api_token, tinyurl_domain=tinyurl_domain))
    else:
        # Case 2: shorten a list of urls
        # Step 2.1: reading a list of long urls from text file
        file = open('urls.txt', 'r', encoding='latin1').readlines()
        urls = []
        for u in file:
            urls.append(u.replace('\n', '').replace('\t', ''))

        # Step 2.2: create short URLs
        f = open('short_urls.txt', 'w', encoding='utf-8')

        print("Shortening URLs\n...\n")
        for url in urls:
            short_url = generate_short_url(url=url, api_token=api_token, tinyurl_domain=tinyurl_domain)
            f.write(short_url + '\t' + url + '\n')
            time.sleep(.5)
        print("Done\n")
        f.close()


if __name__ == '__main__':
    main()
