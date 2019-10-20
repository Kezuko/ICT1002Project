import json
import objectpath
from twython import Twython

def twitterAPI():

    #Personal API key
    twitter = Twython("DubGZhfy08e2kF7r4Z1FnH5nu", "hfX9xdxvppgMIKaeJi2X8fzbood46UNyRJa25yzTQr931OOAmN",
                      "285684564-QgwQAfaSgFLwlWNzl6JIpD6WlDCYPyiZsGKfU4Uc", "Lcx2SpsfGoKaxrtqg3sZOnIHIntfYZJpBMgUkPZGAXoyI")

    #Search for either the word "procurement" or "#procurement"
    results = twitter.search(q='procurement OR #procurement', result_type='popular')


    #save the JSON output into a txt file for future usage
    with open("Twitter.txt", "w") as text_file:
        json.dump(results, text_file)

    json_data = json.load(open('Twitter.txt'))

    jsonnn_tree = objectpath.Tree(json_data['statuses'])
    result_list = list(jsonnn_tree.execute('$..expanded_url'))

    statusesText = [statuses['text'] for statuses in json_data['statuses']]


    twythonFinalOutput = dict(zip(statusesText, result_list))
    print twythonFinalOutput

#twitterAPI()
