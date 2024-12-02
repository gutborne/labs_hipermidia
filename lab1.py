
#Import the xml data that will be analised 
import xml.etree.ElementTree as ET
tree = ET.parse('verbetesWikipedia.xml')
root = tree.getroot()

print("                                     first step".upper())
#tag and attributes of the root
print(root.tag, root.attrib)

#first step: count the number of pages of the xml file
counting_pages = 0
for child in root:
    counting_pages += 1
print(counting_pages)

print("\n                                     second step".upper())
#second step: print the id and the title of each tag at the xml file
count1 = 0
"""
for child in root:
    count1 += 1
    node = child.iter()
    for n in node:
        if n.tag != 'text' and n.tag != 'page':
            print(count1, n.tag, n.text)
"""
print("\n                                     third step".upper())
#third step: find some user-defined string in the title and show all the titles with such string;
#note: differences between letter cases must be ignored
count2 = 0
user_defined_str = "computers"
for child in root.findall('page'):
    title_words = child.find('title').text.split()
    title = child.find('title').text
    for word in title_words:
        if(word.lower() == user_defined_str.lower()):
            count2 += 1
            print(f"{count2}{' '}{title}")

print("\n                                     fourth step".upper())
#fourth step: find some user-defined string in the title and show all the titles with such string. 
#Such titles must be ordered in descending order by the number of occurrences of the user-defined
#string in the text that belongs to the page  
count3 = 1 #counts how many titles have the user-defined string
count_words_in_text = 0
user_defined_str = "computer"
dict_title_occur = {}
for child in root.findall('page'):
    text_words = child.find('text').text.split()
    title_words = child.find('title').text.split()
    title = child.find('title').text
    for word in title_words:
        if(word.lower() == user_defined_str.lower()):
            for word in text_words:
                if(word.lower() == user_defined_str.lower()):
                    count_words_in_text += 1;
                    dict_title_occur[title] = count_words_in_text
    count_words_in_text = 0

def value_getter(value):#callback function for capture the value from the key-value pair tuple
    return value[1]    
ordered_dict = sorted(dict_title_occur.items(), key=value_getter, reverse=True)
for item in ordered_dict:
    #print(f"{count3}{'->'}{item}")
    count3 += 1

print("\n                                     fifth step".upper())
#fifth step: find some user-defined string in the title and show all the titles with such string. 
#Such titles must be ordered in descending order by the number of occurrences of the user-defined
#string in the text that belongs to the page
#change the name of the dict
user_words_in_text = 0
total_words_in_text = 0
user_word_percentage = 0
user_defined_str = "computer"
dict_title_occur = {}
dict_data_pages = []#list of tuples in which each tuple is filled with (word percentage, title, id)
for child in root.findall('page'):
    text_words = child.find('text').text.split()
    title_words = child.find('title').text.split()
    title = child.find('title').text
    id = child.find('id').text
    for word in text_words:
        total_words_in_text += 1
        if(word.lower() == user_defined_str.lower()):
            user_words_in_text += 1
    user_word_percentage = round(user_words_in_text/total_words_in_text * 100, 3) #visualize the data better
    for word in title_words:
        if(user_defined_str.lower() == word.lower()):
            user_word_percentage = round(user_word_percentage + (0.1 * user_word_percentage), 3)
            break
    dict_data_pages.append((user_word_percentage, title, id))
    total_words_in_text = 0
    user_words_in_text = 0
def percentage_getter(tuple):
    return tuple[0]
dict_data_pages.sort(key=percentage_getter, reverse=True)
def escrever_out_file(dict_tuples: dict):
  with open("teste.txt", 'w') as f:
    lista_out = list()
    for tuple in dict_tuples:
      string = str(tuple) + "\n"
      lista_out.append(string)
    f.writelines(lista_out)
escrever_out_file(dict_data_pages)
