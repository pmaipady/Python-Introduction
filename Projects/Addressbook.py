print ("Problem #3: create an address book")

decision = int(input("Do you want to enter a new record? Enter 1 for yes; 0 for no: "))

while decision == 1:
   f = open("address.txt", "a")

   Name = input("Enter the name: ")
   Address = input("Enter street address: ")
   City = input("Enter city: ")
   State = input("Enter state: ")
   Zip = int(input("Enter zip: "))
   Tel = input("Enter telephone number: ")
   Email = input("Enter email address: ")


   f.write("Name: %s \n" %Name)
   f.write("Address: %s \n" %Address)
   f.write("City: %s \n" %City)
   f.write("State: %s\n" %State)
   f.write("Zip: %d\n" %Zip)
   f.write("Tel: %s\n" %Tel)
   f.write("Email: %s\n\n" %Email)

   decision = int(input("Do you want to enter a new record? Enter 1 for yes; 0 for no: "))


f.close()
