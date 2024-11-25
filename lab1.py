
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

#second step: print the id and the title of each tag at the xml file
counting_pages = 0
for child in root:
    counting_pages += 1
    node = child.iter()
    for n in node:
        if n.tag != 'text' and n.tag != 'page':
            print(counting_pages, n.tag, n.text)

#some useful functions from the etree documentation
#this is being a different way to do the second step 
"""
for i in range(counting_pages):
    for j in range(2):
        print(root[i][j].text)
"""
#how to use iter()
"""for title in root.iter('title'):
    print(title.text)
"""
#this is being a different way to do the second step using findall and find
"""
for page in root.findall('page'):
    count += 1
    id = page.find('id').text
    title = page.find('title').text
    print(f"{count}{' '}{id}{' '}{title}")
"""
