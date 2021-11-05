import requests
from urlextract import URLExtract

apiKey = '***'

def grabData():
    response = requests.get(f"https://api.giphy.com/v1/gifs/search?api_key={apiKey}&q={query}&limit={limit + 1}")
    data = response.json()

    extractUrls(data)

def extractUrls(data):
    extractor = URLExtract()
    urls = extractor.find_urls(str(data))

    print('Writing...')
    listingFinalUrls(urls)

def listingFinalUrls(urls):
    listUrls = []

    for i in range(len(urls)):
        if 'giphy.gif' in urls[i]:
            if (urls[i] not in listUrls):
                listUrls.append(urls[i])

    print(listUrls)
    print('Done ✅')


query = input('Enter Query: ')
limit = input('Limit: ')

print('Searching...')
print('*Turn Off The VPN Or Use OpenVPN!*')

grabData()
