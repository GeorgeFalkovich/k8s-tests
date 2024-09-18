# Base image with Apache and PHP
FROM php:8.0-apache

# Install gcloud
RUN  apt-get update && apt-get install -y python3 \
    && curl https://sdk.cloud.google.com | bash

# Copy index.php from local to container
COPY index.php /var/www/html

RUN META_REGION_STRING=$(curl "http://metadata.google.internal/computeMetadata/v1/instance/zone" -H "Metadata-Flavor: Google" || echo "mock-region") && \
    REGION=$(echo "$META_REGION_STRING" | awk -F/ '{print $4}') && \
    sed -i "s|region-here|$REGION|" /var/www/html/index.php

# Expose port 80 for Apache
EXPOSE 80

# Keep container running
CMD ["apache2-foreground"]