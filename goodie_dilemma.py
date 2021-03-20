items = []
file_one = open("sample_input.txt","r") #open sample_input file in read mode 
fline = file_one.readlines()
employee_count = int(fline[0][-2])
for i in range(4, len(fline)):#read line from file which are the goods and its respective price
  item = fline[i].split(":")
  items.append([item[0],int(item[1])])
items =sorted(items, key=lambda price:price[1]) #sort list according to increasing order of price
min_diff = float('inf') #positive infinite value

for i in range(0,len(items)-employee_count+1):
  diff = items[i+employee_count-1][1]-items[i][1]
  if diff<min_diff:
    index_minimum=i
    min_diff=diff #difference between max and min value
file_one.close()

file_two = open("sample_output.txt","w") #open output_file in write mode
file_two.write("Here the goodies that are selected for distribution are: \n\n")
for i in range(index_minimum, index_minimum+employee_count):
  file_two.write("%s : %s\n" % (str(items[i][0]),int(items[i][1])))

file_two.write("And the difference between the chosen goodie with highest price and the lowest price is "+ str(min_diff))
file_two.close()