
#Import the xml data that will be analised 
import xml.etree.ElementTree as ET
tree = ET.parse('verbetesWikipedia.xml')
root = tree.getroot()

print("\n                                     second step".upper())
#second step: print the id and the title of each tag at the xml file
count1 = 0

for child in root:
    count1 += 1
    node = child.iter()
    for n in node:
        if n.tag != 'text':
            print(count1, n.tag, n.text)
