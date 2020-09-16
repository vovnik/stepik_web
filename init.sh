sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart 
sudo gunicorn -c hello.py hello:wsgi_application
sudo gunicorn -b 0.0.0.0:8000 ask.ask.wsgi:application
