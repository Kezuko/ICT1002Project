import json
from twython import Twython

#Personal API key
twitter = Twython("DubGZhfy08e2kF7r4Z1FnH5nu", "hfX9xdxvppgMIKaeJi2X8fzbood46UNyRJa25yzTQr931OOAmN",
                  "285684564-QgwQAfaSgFLwlWNzl6JIpD6WlDCYPyiZsGKfU4Uc", "Lcx2SpsfGoKaxrtqg3sZOnIHIntfYZJpBMgUkPZGAXoyI")

#Search for either the word "procurement" or "#procurement"
results = twitter.search(q='procurement OR #procurement', result_type='popular')

#save the JSON output into a txt file for future usage
with open("Twitter.txt", "w") as text_file:
    json.dump(results, text_file)