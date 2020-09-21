sudo mysql -uroot -e "create django_db"
sudo python manage.py makemigrations 
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart 
sudo gunicorn -c hello.py hello:wsgi_application
cd /home/box/web/ask
sudo gunicorn -b 0.0.0.0:8000 ask.wsgi:application
