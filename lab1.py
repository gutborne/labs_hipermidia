
#Import the xml data that will be analised 
import xml.etree.ElementTree as ET
tree = ET.parse('verbetesWikipedia.xml')
root = tree.getroot()

#tag and attributes of the root
print(root.tag, root.attrib)

#first step: count the number of pages of the xml file
counting_pages = 0
for child in root:
    counting_pages += 1
print(counting_pages)


