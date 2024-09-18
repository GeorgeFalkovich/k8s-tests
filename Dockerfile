# Base image with Apache and PHP
FROM php:8.0-apache

# Install gcloud
RUN  apt-get update && apt-get install -y python3 \
    && curl https://sdk.cloud.google.com | bash

# Copy index.php from local to container
COPY index.php /var/www/html

# Expose port 80 for Apache
EXPOSE 80

# Keep container running
CMD ["apache2-foreground"]