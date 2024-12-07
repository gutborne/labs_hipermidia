
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
"""user_words_in_text = 0
total_words_in_text = 0
user_word_percentage = 0
user_defined_str = "the"
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
for i in dict_data_pages:
    print(i)"""
"""def escrever_out_file(dict_tuples: dict):
  with open("teste.txt", 'w') as f:
    lista_out = list()
    for tuple in dict_tuples:
      string = str(tuple) + "\n"
      lista_out.append(string)
    f.writelines(lista_out)
escrever_out_file(dict_data_pages)
"""
#sixth step: remove the stop words
print("\n                                     sixth step".upper())
"""user_words_in_text = 0
total_words_in_text = 0
user_word_percentage = 0
dict_title_occur = {}
dict_data_pages = []#list of tuples in which each tuple is filled with (word percentage, title, id)
print("type a word:")
user_defined_str = input()
while(len(user_defined_str) < 4):
    print("wrong length! type again")
    user_defined_str = input()

for child in root.findall('page'):
    text_words = child.find('text').text.split()
    title_words = child.find('title').text.split()
    title = child.find('title').text
    id = child.find('id').text
    for word in text_words:
        if(len(word) >= 4):
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
for i in range(100):
    print(dict_data_pages[i])
"""

#seventh step: cache the queries
print("\n                                     seventh step".upper())
class Result:
    keyword = ""
    results = []
    def __str__(self):
        return f"word: {self.keyword} \n queries: \n {self.results}"

#child 



def percentage_calculator(page, user_defined_str):
    words_in_text = 0 #user-defined string in the text
    total_words = 0 #total words in the text of the page in which the len(word) >= 4 
    user_word_perc = 0
    text_words = page.find('text').text.split()
    title_words = page.find('title').text.split()
    for word in text_words:
        if(len(word) >= 4):
            total_words += 1
        if(word.lower() == user_defined_str.lower()):
            words_in_text += 1
    user_word_perc = round(words_in_text/total_words * 100, 3) #visualize the data better
    for word in title_words:
        if(user_defined_str.lower() == word.lower()):
            user_word_perc = round(user_word_perc + (0.1 * user_word_perc), 3)
            break
    return user_word_perc

def is_cache_empty():
    if(len(cache_memory) == 0):
        return True
    else:
        return False
    
def is_keyword_not_found(cache_memory, user_def_str):
    if(is_cache_empty()):
        return True
    else:#if the cache isn't empty
        for result in cache_memory:
            if(result.keyword.lower() == user_def_str.lower()):
                return True
        return False

def percentage_getter(tuple):
            return tuple[0]
def print_result(result):
    for i in range(100):
        print(result[i])      

cache_memory = []#list of objects in which each one has a keyword and list of results
user_word_perc = 0
result = Result()
answer = int(input("would you like to search? "))
while(answer == 1):
    print("type a word: ")
    defined_str = input() #user-defined string
    while(len(defined_str) < 4):
        print("wrong length! type again!")
        defined_str = input("type a word: ")
    result.keyword = defined_str
    cache_is_empty = is_cache_empty()
    is_search_not_found = is_keyword_not_found(cache_memory, defined_str)#cache isn't empty, but even so the word searched wasn't found
    if(cache_is_empty or is_search_not_found):
        print("will read the xml page!\n")
        for page in root.findall('page'):
            title = page.find('title').text
            id = page.find('id').text 
            user_word_perc = percentage_calculator(page, defined_str)
            result.results.append((user_word_perc, title, id))
        result.results.sort(key=percentage_getter, reverse=True)
        cache_memory.append(result)
        print_result(result.results)
    else:
        print("going to find the word on cache!\n")
        for res in cache_memory:
            if(res.keyword.lower() == user_defined_str.lower()):
                print_result(res)
    answer = int(input("would you like to search again? "))
