# Author: Meesam Amir Syed

# Running:
# To run web app, you can directly visit: https://decompress-message.herokuapp.com/
# To run it locally via terminal, locate this directory ("Decompress-Message_Flask") on your machine, and start terminal
#  inside it. Use python command:  "python main.py" to compile; this outputs the web app link.

import re
from flask import Flask, render_template, request


app = Flask(__name__)
app.config['SECRET_KEY'] = "tempkey" #encrypts cookies and session data related to website, it can be whatever we want

#Requests:
# GET: when a page is reloaded or searched via URL its a GET request
# POST: when a button is clicked, all the info inputted by user is "posted" to backend of the system, hence POST

# Decorators
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/results", methods= ["POST", "GET"])
def results():
    input = request.form.get("int_input")
    if request.method == "POST":
        return render_template("home.html", results = uncompressor(input))


# 'Uncompressor' function takes a string as input, the compressed message (ex. 1a2b3c), 
#   and returns the uncompressed form (abbccc) of it
# The message will always be formatted by a leading single integer (1-9) followed 
#   by an alphanumeric character

def uncompressor(input):

    # Check placed to see if input is in the correct format, if not then program displays
    #  error message 
    if (input[0].isdigit() == False) :
        errorMsg = "Message does NOT have a leading integer (1-9). \nValid input examples: 1a2b3c, 3m5a"
        return errorMsg

    # Using Regular Expressions (regex) we can extract a group of an integer and an alphanumeric character
    # Functionality of this has been extended to extracting a group of an integer 
    #  followed a string of any length
    #   example1: '1a2b3c' = ['1a', '2b', '3c] 
    #   example2: '3mno5abcd6xyz' = ['3mno', '5abcd', '6xyz']
    match = re.findall(r'\d{1}[a-zA-Z]*', input)

    # string variable to hold the decompressed message
    decompString = ''
    
    for i in match:
        # After the 'match' array is created, iterate on each element and by using 
        #  string manipulations (slicing) we can repeat the alphanumeric part 'n' times 
        #  (according to the leading integer) and finally, join the strings using the '+' character and output
        decompString = decompString + (i[1:]*int(i[0])) 
            
    return input + " => " + decompString


if __name__ == '__main__':
    app.run(debug=True)  # update flask server with changes we make

    
