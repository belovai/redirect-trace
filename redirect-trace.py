#!/usr/bin/python3

import sys
import requests
import urllib3


def trace_url(url):
    urllib3.disable_warnings()
    response = requests.get(url, verify=False)
    for r in response.history:
        print(r.url, r.status_code)
    print(response.url, response.status_code)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("missing url")
        exit(1)
    for arg_url in sys.argv[1::]:
        trace_url(arg_url)
        print("---")

