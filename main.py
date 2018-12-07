from flask import Flask, render_template
import foaf_parse

app = Flask(__name__)
filepath = "static/foaf.rdf"

@app.route("/")
def start_page():
    return render_template("home.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/aboutme")
def aboutme():
    return render_template("aboutme.html", me=foaf_parse.get_me(filepath))

@app.route("/soa")
def soa():
    return render_template("soa.html")

@app.route("/rdf")
def rdf():
    return render_template("rdf.html")

@app.route("/gcp")
def gcp():
    return render_template("gcp.html")

if __name__ == "__main__":
    app.run(debug=True)
