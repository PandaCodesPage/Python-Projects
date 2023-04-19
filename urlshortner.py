import pyshorteners
link = input("URL to shorten: ")

Shortener1 = pyshorteners.Shortener()
tinyurl= Shortener1.tinyurl.short(link)

print("The Shortened URL is: " + tinyurl)
