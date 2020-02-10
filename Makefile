dev:
	FLASK_ENV=development flask run --host 127.0.0.1 --port 5000 --reload --debugger --lazy-loader --without-threads

prod:
	sudo /usr/local/bin/gunicorn --bind 0.0.0.0:80 app:app
