data =[]
for i in range (5):
  card = int(input("Enter the next item"))
  data.append(card)           
                  
def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers
print(sum_list(data))
