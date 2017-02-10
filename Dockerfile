FROM python:2.7-alpine

RUN apk add --no-cache nginx supervisor

ADD nginx.conf /etc/nginx/nginx.conf

WORKDIR /app

ADD app/requirements.pip /app/

RUN apk add --no-cache --virtual .build-deps  \
		bzip2-dev \
		gcc \
		gdbm-dev \
		libc-dev \
		linux-headers \
		make \
		openssl \
		openssl-dev \
		pax-utils \
		readline-dev \
		sqlite-dev \
		zlib-dev \
	&& pip install --no-cache-dir -r requirements.pip \
	&& apk del .build-deps \
	&& rm -rf /usr/src/python ~/.cache

ADD . /app

# ADD root/dist/* /app/static/

EXPOSE 80

CMD [ "/app/entrypoint.sh" ]