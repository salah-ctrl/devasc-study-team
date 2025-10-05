
import xml.etree.ElementTree as ET
import re

xml = ET.parse("myfile.xml")
root = xml.getroot()

# namespace string zoals '{urn:ietf:params:xml:ns:netconf:base:1.0}'
ns = re.match(r'{.*}', root.tag).group(0)

editconf = root.find(f"{ns}edit-config")
defop   = editconf.find(f"{ns}default-operation")
testop  = editconf.find(f"{ns}test-option")

print(f"The default-operation contains: {defop.text}")
print(f"The test-option contains: {testop.text}")
# Fill in this file with the code from parsing XML exercise
