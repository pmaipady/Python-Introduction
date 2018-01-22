data =[]
for i in range (5):
  card = int(input("Enter the next item"))
  data.append(card)
for i in range (5):
  data.pop()
  print data
  if not data:
    print ("List is empty")
