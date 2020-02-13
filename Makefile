documents:
	if ! [ -d static/docs ]; then \
		mkdir static/docs; \
		git clone https://github.com/rcehemann/resume tmp; \
		mv tmp/main.pdf ./static/docs/rcehemann-resume.pdf; \
		mv tmp/main.tex ./static/docs/resume.tex; \
		rm -rf tmp; \
		git clone https://gist.github.com/rcehemann/25c57f517e012456318379f6c826830b.git tmp; \
		mv tmp/rcehemann-dissertation.pdf ./static/docs/; \
		rm -rf tmp; \
	fi

dev: documents
	@echo "Configuring development environment"
	FLASK_ENV=development flask run --host 127.0.0.1 --port 5000 --reload --debugger --lazy-loader --without-threads

prod: documents
	@echo "Deploying to production"
	sudo /usr/local/bin/gunicorn --bind 0.0.0.0:80 app:app

clean:
	rm -rf static/docs
	rm -rf tmp
	rm -rf tmp2
	rm -rf __pycache__
