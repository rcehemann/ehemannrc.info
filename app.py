from flask import Flask, url_for, render_template, send_file
import os

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["STATIC_DIR"] = os.getcwd() + "/static/"
@app.route("/index")
@app.route("/")
def index():
	#return render_template(url_for("static", filename="templates/index.html"))
	return render_template("index.html")

@app.route("/resume")
def resume():
	return send_file(app.config['STATIC_DIR'] + "docs/ehemannrc.pdf",
					mimetype="application/pdf")

if __name__ == "__main__":
	#run_simple('127.0.0.1', 5000, app, threaded=True)
	app.run(host='127.0.0.1', port=5000, debug=True)