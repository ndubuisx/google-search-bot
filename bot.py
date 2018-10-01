import sys

try: 
	from googlesearch import search 
except ImportError: 
	print("No module named 'google' found") 

string = input("Input search queries separated by commas: ") # ask user for input
str_arr = string.split(",") # split search queries into array items

# loop through each array item and run search
for i in range(len(str_arr)):
    query = str_arr[i]

    for j in search(query, tld="com", num=1, stop=1, pause=2): 
        print(query+" - "+j) 
