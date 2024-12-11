#Import the xml data that will be analised 
import xml.etree.ElementTree as ET
tree = ET.parse('verbetesWikipedia.xml')
root = tree.getroot()

print("\n                                     third step".upper())
#third step: find some user-defined string in the title and show all the titles with such string;
#note: differences between letter cases must be ignored
count2 = 0
user_defined_str = input("type a word: ")
for child in root.findall('page'):
    title_words = child.find('title').text.split()
    title = child.find('title').text
    for word in title_words:
        if(word.lower() == user_defined_str.lower()):
            count2 += 1
            print(f"{count2}{' '}{title}")
