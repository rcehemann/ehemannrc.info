from flask import Flask, url_for, render_template, send_file
import os

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["STATIC_DIR"] = os.getcwd() + "/static/"

def render(page):
	return render_template("{}.html".format(page))

@app.route("/")
@app.route("/index")
def index():
	return render("index")

@app.route("/experience")
def experience():
	return render("experience")

@app.route("/education")
def education():
	return render("education")

@app.route("/publications")
def publications():
	return render("publications")

@app.route("/presentations")
def presentations():
	return render("presentations")

@app.route("/awards")
def awards():
	return render("awards")

@app.route("/resume")
def resume():
	return send_file(app.config['STATIC_DIR'] + "docs/ehemannrc.pdf",
					mimetype="application/pdf")

if __name__ == "__main__":
	#run_simple('127.0.0.1', 5000, app, threaded=True)
	app.run(host='127.0.0.1', port=5000, debug=True)