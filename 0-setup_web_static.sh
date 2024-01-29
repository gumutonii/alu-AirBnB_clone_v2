#!/usr/bin/env bash
<<<<<<< HEAD
# Sets up the web servers for the deployment of web_static.

# Install Nginx if not already installed
apt update -y >/dev/null 2>&1
apt install nginx -y >/dev/null 2>&1

# Create required directories if they don't exist
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/

# Create fake index.html file
echo -e "<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>" >/data/web_static/releases/test/index.html

# Create the symbolic link
ln -sf /data/web_static/releases/test /data/web_static/current

# Change ownership of files and folders inside of /data folder
chown -hR ubuntu:ubuntu /data

# Add alias to serve the content of /data/web_static/current to hbnb_static
sed -i '51i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

# Restart the nginx service
service nginx restart
=======
# bash script that sets up your web servers for the deployment of web_static

sudo apt-get -y update
sudo apt-get -y install nginx
sudo service nginx start

sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html > /dev/null
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '44i \\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default

sudo service nginx restart
>>>>>>> 070b2400c65851cfed794515179027bbfa97752b
