x = {
 'Cat': ['American Shorthair Cat','Bombay Cat','Burmese Cat','Himalayan Cat Breed','Manx Cat'],
 'Dog': ['German Shepherd','Poodle','Siberian Husky','Gold Retriever','Alaskan Malamute'],
}

print(x['Dog'][1])


y = {
 'American Shorthair':{'type':'cat', 'color':'black'},
 'Bombay':{'type':'cat', 'color':'brown'},
 'Burmese':{'type':'cat', 'color':'black'},
 'Himalayan':{'type':'cat', 'color':'white'},
 'Manx':{'type':'cat', 'color':'grey'},
 'German Shepherd':{'type':'dog', 'color':'black'},
 'Poodle':{'type':'dog', 'color':'black'},
 'Siberian Husky':{'type':'dog', 'color':'white'},
 'Gold Retriever':{'type':'dog', 'color':'yellow'},
 'Alaskan Malamute':{'type':'dog', 'color':'white'}
}

print(y['Gold Retriever'])