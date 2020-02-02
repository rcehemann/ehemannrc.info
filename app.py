from flask import Flask, url_for, render_template, send_from_directory, redirect
import os

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

def render(page):
	return render_template("{}.html".format(page))

@app.route("/")
def index():
	return redirect(url_for('home', page="about"))

@app.route("/home/<page>")
def home(page):
	return render(page)

@app.route("/docs/<doc>")
def docs(doc):
	return send_from_directory(os.path.join(app.root_path, "static"),
						  "docs/rcehemann-{}.pdf".format(doc),
						  mimetype="application/pdf")

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                          'images/favicon.ico',
                          mimetype='image/vnd.microsoft.icon')

if __name__ == "__main__":
	app.run(host=os.environ.get("IP", "127.0.0.1"), port=5000,
		threaded=True, debug=True)
