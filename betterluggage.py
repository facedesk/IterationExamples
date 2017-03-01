'''
Create a loop such that you only ask to
add items when the size is less than 5
After you reach the limit, then display all luggage
items neatly
'''

luggage = []
print(luggage)
print ("you have space for 5 items")

while(len(luggage) < 5):
    item = raw_input("What would you like to bring?")
    luggage.append(item)
    #print(luggage)
    

for item in luggage:
	print(item)

