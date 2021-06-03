
import requests
# newest = number
url = 'https://shopee.vn/api/v2/search_items?by=pop&limit=100&facet=13650&keyword=iphone&minPrice=500000&noCorrection=true&newest=1&order=desc'
# url = 'https://shopee.vn/api/v2/search_items/?facet=1979&keyword=iphone&noCorrection=true'
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': 'https://shopee.vn/search?keyword=iphone%20shop',
}
lst_json = []
i = 1
while(1):
    #url = 'https://shopee.vn/api/v2/search_items?by=pop&limit=100&facet=1979&keyword=iphone&minPrice=500000000000&noCorrection=true&newest='+ str(i) +'&order=desc'
    r = requests.get(url, headers=headers)
    print(url)
    data = r.json()
    if data['items'] == None:
        break

    # print(data['items'][0].keys())
    for item in data['items']:
        print('name:', item['name'])
        print('price:', item['price'])
        print(i)
        i = i + 1
    break

