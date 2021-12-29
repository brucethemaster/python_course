#For / For Else loops - executes a block of code a number of times, depending on the sequence it iterates on; the "else" clause is optional
vendors = ["Cisco", "HP", "Nortel", "Avaya", "Juniper"]
 
for element in vendors: #interating over a sequence and executing the code indented under the "for" clause for each element in the sequence
    print(element)
else: #the indented code below "else" will be executed when "for" has finished looping over the entire list
    print("The end of the list has been reached")
    
#result of the above "for" block
Cisco
HP
Nortel
Avaya
Juniper
The end of the list has been reached


for element_index in range(len(vendors)):  #using range and len function to loop through list
    print(vendors[element_index])
else:  #the indented code below "else" will be executed when "for" has finished looping over the entire list
    print("The end of the list has been reached")


for index, element in enumerate(vendors):  #using enumerate to go through list
    print(index, element)
else:  #the indented code below "else" will be executed when "for" has finished looping over the entire list
    print("The end of the list has been reached")