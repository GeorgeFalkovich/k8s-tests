# Base image with Apache and PHP
FROM php:8.0-apache

# Copy index.php from local to container
COPY index.php /var/www/html

RUN mv /etc/apache2/sites-available/000-default.conf /etc/apache2/sites-available/old.conf
RUN sed '1 a\\tRewriteEngine On\n\tRewriteRule ^/(.*)$ /index.php [L] \n' /etc/apache2/sites-available/old.conf > /etc/apache2/sites-available/000-default.conf
RUN a2enmod rewrite && service apache2 restart
    

# Expose port 80 for Apache
EXPOSE 80

# Keep container running
CMD ["apache2-foreground"]

