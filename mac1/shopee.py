import requests
import json
#url = 'https://shopee.vn/api/v2/search_items/?by=pop&limit=100&match_id=1819984&newest=0&order=desc&facet=1979&keyword=iphone&noCorrection=true'
url = 'https://shopee.vn/api/v2/search_items/?by=pop&limit=100&newest=0&order=desc&facet=1979&keyword=iphone&noCorrection=true'
# url = 'https://shopee.vn/api/v2/search_items/?facet=1979&keyword=iphone&noCorrection=true'
#url = 'https://shopee.vn/api/v2/search_items/?by=pop&limit=100&match_id=1819984&newest=0&order=desc&facet=13065&keyword=macbook&minPrice=55837611542796&noCorrection=true'
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': 'https://shopee.vn/search?keyword=macbook',
}    

r = requests.get(url, headers=headers)

data = r.json()
json_object = json.dumps(data)
lst_obj = []
i = 0
print(data['items'][0].keys())
for item in data['items']:
    it = dict()
    it['name'] = item['name'].strip()
    it['price'] = item['price']
    lst_obj.append(it)
    #print('name:', item['name'])
    #print('price:', item['price'])
    #print(item)
    print(i)
    i = i + 1
with open("sample.json", "w") as outfile:
    for element in lst_obj:
        outfile.write(json.dumps(element) + "\n")
# i = 0
# lst_obj = []
# while(1):
#     url = 'https://shopee.vn/api/v2/search_items/?by=pop&limit=100&match_id=1819984&newest=' + str(i) +'&order=desc&facet=13065&keyword=macbook&minPrice=5000000&noCorrection=true'
#     r = requests.get(url, headers=headers)
#     data = r.json()
#     if(data['items'] == None):
#         break
#     for item in data['items']:
#         it = dict()
#         it['name'] = item['name'].strip()
#         it['price'] = item['price']
#         lst_obj.append(it)
#         print('name:', item['name'])
#         print('price:', item['price'])
#         print(i)
#         i = i + 1

# with open("test.json", "w") as outfile:
#     for element in lst_obj:
#         outfile.write(json.dumps(element) + "\n")
