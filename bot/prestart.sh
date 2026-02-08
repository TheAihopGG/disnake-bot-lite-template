#!/bin/sh
set -e
echo Applying migrations
yoyo apply --database postgresql+psycopg://$POSTGRES_USERNAME:$POSTGRES_PASSWORD@postgres:5432/$POSTGRES_DB --batch
echo Migrations applied
exec "$@"