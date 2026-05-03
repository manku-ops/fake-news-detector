import requests

trusted_sites = ["bbc.com", "reuters.com", "thehindu.com"]

def check_url(url):
    for site in trusted_sites:
        if site in url:
            return "Trusted Source"

    return "Unknown / Low Credibility"
