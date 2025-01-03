FROM nginx:1.27.3-alpine

USER root

RUN chown -R nginx:nginx /var/cache/nginx/ /var/run/ /var/log/nginx/ /etc/nginx/conf.d/default.conf
RUN chmod -R 755 /var/cache/nginx/ /var/run/ /var/log/nginx/ /etc/nginx/conf.d/default.conf
RUN apk update && apk add bash

CMD envsubst '\$PORT \$REVERSE_PROXY_PORT \$REVERSE_PROXY_HOST' < /etc/nginx/templates/default.conf.template > /etc/nginx/conf.d/default.conf && exec nginx -g 'daemon off;'

USER nginx
