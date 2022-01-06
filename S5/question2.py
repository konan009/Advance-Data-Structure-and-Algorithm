hash_table = {}

def get_key(txt):
    x = txt.split()
    hash_key = ''
    for item in x:
        hash_key += item[:3]
    return hash_key

def insert(txt):
    key = get_key(txt)
    # COLLISION HANDLER
    if key not in hash_table:
        hash_table[key] = [txt]
    else:
        hash_table[key].append(txt)

def remove(text):
    key = get_key(text)
     # COLLISION HANDLER
    if(len(hash_table[key])>0):
        hash_table[key].remove(text)
    else:   
        hash_table.pop(key)
        
        
insert("bun")
insert("funny")
insert("fun")
insert("tras")
remove("funny")
hash_table

"""
HASHING INFO: Gets the first 3 letter of a word as a hashing key

Pros:
1. Provide more complexity and different combinations compared to hashing using first words.

Cons:
1. Collision happens when first 3 words 
2. Collision happens in verb words that has different tenses, like "study", "studying" and "studied".
"""