from flask import Flask, jsonify, request,render_template

app=Flask(__name__) #WSGI (Web server gateway interface) application

@app.route("/")
def home():
    return render_template("netflix_home.html")  # it will render the "home.html" template from templates folder when the user visits the root URL ("/") of the application.

@app.route("/Techstack")
def tech_stack():
    return render_template("tech_stack.html")   # it will return the tech_stack page which has all the list of skills

if __name__=="__main__":
    app.run(debug=True)
