Steps to install and setup NGINX server for SSL: - 
1. Refer this site for installation - https://github.com/cloudkeep/barbican/wiki/Deploy-OpenStack-Barbican-with-Nginx-web-server
2. Put nginx.key, nginx.crt and ca.crt in /etc/nginx/ssl
3. Create a site file in /etc/nginx/sites-available and link the symfile -
   sudo ln -s /etc/nginx/sites-available/<servername> /etc/nginx/sites-enabled/<servername>
4. Set "ssl_verify_client on;" in sites-enabled file
5. Add paths to ca.crt, nginx.crt, and nginx.key in site file
	    ssl on;
            ssl_certificate /etc/nginx/ssl/nginx.crt;
            ssl_certificate_key /etc/nginx/ssl/nginx.key;
            ssl_client_certificate /etc/nginx/ssl/ca.crt;
            ssl_verify_client on;
6. sudo service nginx restart


Steps to setup barbican for ssl: - 
1. Change /etc/barbican/vassals/barbican-api.ini and barbican-admin.ini with the following change: - 
   protocol = uwsgi #Instead of http
2. start pyenv shell
   	pyenv shell barbican27
3. Create env var $hostname as servername 
	export hostname=<servername> 
        echo $hostname
4. bin/barbican.sh start
