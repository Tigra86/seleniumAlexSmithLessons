# a - запись новых данных в файл и помещение их в конец файла
fw = open('doc/new.txt', 'a')
fw.write("Here I am entering some text\n")
fw.close()

# w - запись новых данных в файл и удаление старых данных
fw = open('doc/new_2.txt', 'w')
fw.write("Here I am entering some new text to make sure that it deletes an old text\n")
fw.close()

fr = open('doc/new_2.txt', 'r')
text = fr.read()
fr.close()

print(text)
