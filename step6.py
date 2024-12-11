#Import the xml data that will be analised 
import xml.etree.ElementTree as ET
tree = ET.parse('verbetesWikipedia.xml')
root = tree.getroot()

#sixth step: remove the stop words and cache the researches
print("\n                                     sixth step".upper())
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
    user_word_perc = round(words_in_text/total_words * 100, 3)
    for word in title_words:
        if(user_defined_str.lower() == word.lower()):
            user_word_perc = round(user_word_perc + (0.1 * user_word_perc), 3)
            break
    return user_word_perc

def is_cache_empty(cache_memory):
    if(len(cache_memory) == 0):
        return True
    else:
        return False
    
#this function returns True if the some keyword isn't found in the cache, but if it is returns False 
def is_keyword_not_found(cache_memory, user_def_str):
    if(is_cache_empty(cache_memory)):
        return True
    else:#if the cache isn't empty
        for key in cache_memory:
            if(key.lower() == user_def_str.lower()):
                return False
        return True

def percentage_getter(tuple):
    return tuple[0]


def set_result(user_def_str):
    print("->inside set_result()" + "\n" + "user_def_str: " + user_def_str + "\n")
    dict_result = {}
    result = []
    root_tree = tree.getroot()
    count = 0
    for page in root_tree.findall('page'):
        title = page.find('title').text
        id = page.find('id').text
        user_word_perc = percentage_calculator(page, user_def_str)
        result.append((user_word_perc, title, id))
    result.sort(key=percentage_getter, reverse=True)
    dict_result = {user_def_str: result}
    return dict_result

user_word_perc = 0
cache_memory = {}#dict in which each key is a user-defined string and the value is a list of results
answer = int(input("would you like to search? "))
while(answer == 1):
    defined_str = input("type a word: ") #user-defined string
    while(len(defined_str) < 4):
        print("wrong length! type again!")
        defined_str = input("type a word: ")
    cache_is_empty = is_cache_empty(cache_memory)
    is_search_not_found = is_keyword_not_found(cache_memory, defined_str)#cache isn't empty, but even so the word searched wasn't found
    print(f"\nis_keyword_not_found: {is_search_not_found}\n")
    if(cache_is_empty or is_search_not_found):
        print("will read the xml page!\n")
        print("user-defined string: " + defined_str + "\n")
        cache_memory.update(set_result(defined_str))
        list_result = cache_memory[defined_str]
        for tuple in list_result[:10]:
            print(tuple)
    else:
        print("going to find the word on cache!\n")
        list_result = cache_memory[defined_str]
        for tuple in list_result[:10]:
            print(tuple)
    answer = int(input("would you like to search again? "))
