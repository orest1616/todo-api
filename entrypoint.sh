#!/bin/bash

echo "⏳ Waiting for DB to be ready..."
until PGPASSWORD=$DB_PASSWORD psql -h "$DB_HOST" -U "$DB_USER" -d "$DB_NAME" -c '\q' 2>/dev/null; do
  echo "🛑 DB is unavailable - sleeping"
  sleep 1
done
echo "✅ DB is up - continuing"

echo "🛠 Running migrations..."
python manage.py migrate --noinput

echo "👤 Creating superuser..."
python manage.py create_superuser || echo "⚠️ Superuser already exists"

echo "🚀 Starting server..."
exec "$@"
