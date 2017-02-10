#!/bin/sh

cat <<EOT > /etc/supervisord.conf

[supervisord]
nodaemon=true


[program:proxy]
command=nginx -g "daemon off;"
autorestart=true
startsecs=0
stderr_logfile=/dev/stderr
stderr_logfile_maxbytes=0
stdout_logfile=/dev/stdout
stdout_logfile_maxbytes=0

[program:api_server]
command=python /app/gunicorn_runner.py
autorestart=true
startsecs=0
stderr_logfile=/dev/stderr
stderr_logfile_maxbytes=0
stdout_logfile=/dev/stdout
stdout_logfile_maxbytes=0

EOT

exec /usr/bin/supervisord
