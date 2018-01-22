print ("Problem 4: Create a to do application")
sample_list = {}
print (sample_list)

decision = int(input("Do you want to add an item to the list? Enter 1 for yes; 0 for no: "))
counter = 1
f = open("to_do_app.txt", "w")

while decision == 1:
   f = open("to_do_app.txt", "a")

   item = input("Enter the item: ")
   sample_list[counter] = item

   f.write("item %d: %s \n" %(counter, item))
   counter = counter +1

   decision = int(input("Do you want to add another item to the list? Enter 1 for yes; 0 for no: "))

f.write("list: %s \n" %sample_list)
f.close()
print (sample_list)

