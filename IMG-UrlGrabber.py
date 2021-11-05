from serpapi import GoogleSearch
from urlextract import URLExtract

def searchQuery():
  search = GoogleSearch(params)
  results = str(search.get_dict())

  extractUrls(results)

def extractUrls(results):
  extractor = URLExtract()
  urls = extractor.find_urls(results)

  print('Writing...')
  FinalUrls(urls)

def FinalUrls(urls):
  listUrls = []

  for i in range(len(urls)):
    if 'jpeg' in urls[i] or 'jpg' in urls[i] or 'png' in urls[i] or 'webp' in urls[i]:
      if 'serpapi' not in urls[i]:  # thumbnail
        listUrls.append(urls[i])

  print('Successful ✅')
  print(listUrls)




Query = input('Enter Query: ')

apiKey = '***'
params = {
  "engine": "google",
  "ijn": "0",
  "q": Query,
  "google_domain": "google.com",
  "tbm": "isch",
  # "num": "300",
  # "start": "200",
  "device":"desktop",
  "api_key": apiKey
}

print('Searching...')
print('*Turn Off The VPN Or Use OpenVPN!*')

searchQuery()
