
# Project Title: URL Shortener

import hashlib

def shorten_url(url):
    # Generate MD5 hash of the URL
    md5_hash = hashlib.md5(url.encode()).hexdigest()
    # Take the first 8 characters of the hash to create a short URL
    short_url = md5_hash[:8]
    return short_url

original_url = input("Enter the URL to shorten: ")
shortened_url = shorten_url(original_url)
print("Shortened URL:", shortened_url)









