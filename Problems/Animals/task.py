# read animals.txt
file1 = open("animals.txt", "r")
animals = file1.read().replace('\n', ' ')
file1.close()
# and write animals_new.txt
file2 = open("animals_new.txt", "w")
file2.write(animals)
file2.close()
