sudo apt-get update
sudo apt-get install -y python3.8
sudo apt-get install -y python3.8-dev
sudo unlink /usr/bin/python3
sudo ln -s /usr/bin/python3.8 /usr/bin/python3
sudo pip3 install --upgrade pip
sudo pip3 install --upgrade django==3.1.1
sudo pip3 install --upgrade gunicorn
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart 
sudo gunicorn -c hello.py hello:wsgi_application
sudo gunicorn -b 0.0.0.0:8000 ask.ask.wsgi:application
