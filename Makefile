resume:
	@echo "Cloning resume repository..."
	git clone https://github.com/rcehemann/resume tmp
	mv tmp/main.pdf ./static/docs/rcehemann-resume.pdf
	mv tmp/main.tex ./static/docs/resume.tex
	rm -rf tmp

dev: resume
	@echo "Configuring development environment"
	FLASK_ENV=development flask run --host 127.0.0.1 --port 5000 --reload --debugger --lazy-loader --without-threads

prod: resume
	@echo "Deploying to production"
	sudo /usr/local/bin/gunicorn --bind 0.0.0.0:80 app:app
