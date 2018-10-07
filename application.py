# import dependencies
from flask import Flask, render_template, request

try: 
	from googlesearch import search 
except ImportError: 
	print("No module named 'google' found")

# create an instance of the Flask class
app = Flask(__name__)

# '/handle_data' triggers this function
@app.route('/handle_data', methods=['POST'])
def handle_data():
    # user search query input from browser
    user_input = request.form['projectFilePath']
    # split search queries into array
    user_input_arr = user_input.split(",")
    # result variable - contains result of search
    result = []
    # loop through user_input_arr
    for i in range(len(user_input_arr)):
	# handle each array item as query
        query = user_input_arr[i]
	# perform google search on query in position i
        for j in search(query, tld="com", num=1, stop=1, pause=2): 
	    # store result of search 
            result.append([query, j])
    # return result to browser		
    return render_template("index.html", result=result)

# '/' triggers this function
@app.route("/")
def output():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()


