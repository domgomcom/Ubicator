
boxes_file = open('C:/Users/MainUser/Documents/Ubicator/db/Ubicator - BOXES.tsv','r')
boxes_text = boxes_file.read()
items_file = open('C:/Users/MainUser/Documents/Ubicator/db/Ubicator - ITEMS.tsv','r')
items_text = items_file.read()


#print (len(items_text))
#print(items_text)

#supress last \
items_text = items_text[0:-1]
boxes_text = boxes_text[0:-1]

#print (len(items_text))
#print(items_text)

js_file = open('C:/Users/MainUser/Documents/Ubicator/db/Ubicator.js','w')
js_file.write('let boxes="')
js_file.write(boxes_text)
js_file.write('";\x0A\x0A')
# \t\t\t\t\t\t\r\n";

js_file.write('let items="')
js_file.write(items_text)
js_file.write('";\r\n')

js_file.close()

#text_file = open('C:/Users/MainUser/Documents/Ubicator/db/Text.txt','r')
#text_file.read()
#print (text_file)


