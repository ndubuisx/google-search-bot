from flask import Flask, render_template, request

try: 
	from googlesearch import search 
except ImportError: 
	print("No module named 'google' found")

app = Flask(__name__)

@app.route('/handle_data', methods=['POST'])
def handle_data():
    user_input = request.form['projectFilePath']
    user_input_arr = user_input.split(",")
    result = []
    for i in range(len(user_input_arr)):
        query = user_input_arr[i]

        for j in search(query, tld="com", num=1, stop=1, pause=2): 
            result.append([query, j])

    return render_template("index.html", result=result)

@app.route("/")
def output():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()


