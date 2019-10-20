import requests
import json

def newsAPI():

    def jprint(obj):
        # create a formatted string of the Python JSON object
        text = json.dumps(obj, sort_keys=True, indent=4)
        print(text)

    url = ('https://newsapi.org/v2/everything?' #API URL
           'q=procurement AND tender&' #keywords on procurement AND tender
           'sortBy=popularity&' #Sort them by popularity
           'apiKey=365fe4d44dba4aa98a00a7497200e6f9') #Personal API key

    # GET
    response = requests.get(url)

    #storing the output into variable "results"
    results = response.json()

    # save the JSON output into a txt file for future usage
    with open("NewsAPI.txt", "w") as text_file:
        json.dump(results, text_file)

    articles = response.json()['articles']

    titlelist = []
    for d in articles:
        title = d['title']
        titlelist.append(title)

    urlList = []
    for d in articles:
        url = d['url']
        urlList.append(url)

    finalOutput = dict(zip(titlelist, urlList))
    print finalOutput
