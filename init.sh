sudo pip3 install django==2.0.7
sudo /etc/init.d/mysql start
sudo mysql -uroot -e "create database stepik_web;"
sudo mysql -uroot -e "grant all privileges on stepik_web.* to 'box'@'localhost' with grant option;"
sudo python3 /home/box/web/ask/manage.py makemigrations 
sudo python3 /home/box/web/ask/manage.py migrate
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart 

