import json
import yaml

# JSON inlezen
with open('myfile.json','r') as json_file:
    ourjson = json.load(json_file)

# Toon de dict (optioneel) en specifieke velden
print(ourjson)
print("The access token is: {}".format(ourjson['access_token']))
print("The token expires in {} seconds".format(ourjson['expires_in']))

# YAML-output
print("\n\n---")
print(yaml.dump(ourjson))
# Fill in this file with the code from parsing JSON exercise
