http {
     server {

        listen 80 default;

	location ^~ /uploads/ {
	    root /home/box/web;
        }

        location ~*(\\\w+)*\.\w+ {
	   root /home/box/web/public;
	}

        location ~* [^(\.\w+)] {
	   return 404;
	}
     }
}
