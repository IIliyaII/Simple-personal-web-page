from flask import Flask , render_template , redirect  , url_for


app = Flask("Web Page")

@app.route("/")
def index():
    return render_template("home.html")
@app.route("/home")
def home():
    return render_template("home.html")
@app.route("/Github")
def github_link():
    return redirect("https://github.com/IIliyaII")

@app.route("/linkedin")
def linkedin():
    return redirect("https://www.linkedin.com/in/iliya-sharif-482001384?utm_source=share_via")

@app.route("/instagram")
def instagram():
    return redirect("https://www.instagram.com/call.me.eeliya?stkn=MTQyYzU2NXJsMHQwNA==")

@app.route("/reddit")
def reddit():
    return redirect("https://www.reddit.com/u/HoneydewLegitimate99/s/c8PSQBvZCk")
@app.route("/projects")
def projects():
    return redirect("https://github.com/IIliyaII/-Showcase-Website-")
app.run(debug=True)