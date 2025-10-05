import json
import yaml

# YAML inlezen
with open('myfile.yaml','r') as yaml_file:
    ouryaml = yaml.safe_load(yaml_file)

# Toon de dict en specifieke velden
print(ouryaml)
print("The access token is {}".format(ouryaml['access_token']))
print("The token expires in {} seconds.".format(ouryaml['expires_in']))

# JSON-output (pretty)
print("\n\n")
print(json.dumps(ouryaml, indent=4))
# Fill in this file with the code from parsing YAML exercise
