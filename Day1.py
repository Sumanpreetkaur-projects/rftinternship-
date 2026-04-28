# Data Cleaning (List Processing) 

data = [10 , None , 20 , 10 , "" , 30 , None , 40]
# To remove the duplicate 
result = list(set(data))
# To remove the empty strings 
result = [item for item in result if item != ""]
result = [item for item in result if item != None]

print(result)
duplicate_removed = len(data)-len(result)
print("The number of duplicate removed values are : " , duplicate_removed)
result.sort()
print("sorted data will be : " ,result)
