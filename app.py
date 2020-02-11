from flask import Flask, url_for, render_template, send_from_directory, redirect
from static.utils import parse_cv_section
import os

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

data = {
	"about" : dict(),

	"experience" : dict(experience=parse_cv_section("Experience", pattern="entries"),
						education=parse_cv_section("Education", pattern="entries")),

	"publications" : dict(publications=parse_cv_section("Publications", pattern="items"),
						  presentations=parse_cv_section("Presentations", pattern="items"),
						  awards=parse_cv_section("Awards \\& Honors", pattern="items"))
}

"""
MAIN ROUTES
"""
def render(page):
	return render_template("{}.html".format(page), **data[page])

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

"""
UTILITY FUNCTIONS
"""
#@app.context_processor
#def list_element_processor():
	#def list_element(raw):
	#	pass
	#pass

if __name__ == "__main__":
	app.run(host=os.environ.get("IP", "127.0.0.1"), port=5000,
			threaded=True, debug=True)
