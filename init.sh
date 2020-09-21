sudo /etc/init.d/mysql start
sudo mysql -uroot -e "create database stepic_web;"
sudo mysql -uroot -e "grant all privileges on stepic_web.* to 'box'@'localhost' with grant option;"
sudo python manage.py makemigrations 
sudo python manage.py migrate
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart 
sudo gunicorn -c hello.py hello:wsgi_application
cd /home/box/web/ask
sudo gunicorn -b 0.0.0.0:8000 ask.wsgi:application
