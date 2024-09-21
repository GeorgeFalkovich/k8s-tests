# Base image with Apache and PHP
FROM php:8.0-apache

# Copy index.php from local to container
COPY index.php /var/www/html

RUN sed -e '2i \\tRewriteEngine On\n\tRewriteRule ^/(.*)$ / [L]' /etc/apache2/sites-available/000-default.conf
RUN  a2enmod rewrite && service apache2 restart
    

# Expose port 80 for Apache
EXPOSE 80

# Keep container running
CMD ["apache2-foreground"]