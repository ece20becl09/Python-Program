#!/usr/bin/env python3
"""
connect_postgres.py
Simple script to connect to a PostgreSQL server using psycopg2 and ensure basic tables exist.
Usage examples:
  python connect_postgres.py --host localhost --port 5432 --dbname mydb --user myuser
Or set environment variables: PGHOST, PGPORT, PGDATABASE, PGUSER, PGPASSWORD
"""

import psycopg2
import os
import argparse
import getpass
import sys


def main():
    parser = argparse.ArgumentParser(description='Connect to PostgreSQL and ensure tables exist')
    parser.add_argument('--host', default=os.getenv('PGHOST', 'localhost'))
    parser.add_argument('--port', default=os.getenv('PGPORT', '5432'))
    parser.add_argument('--dbname', default=os.getenv('PGDATABASE', 'postgres'))
    parser.add_argument('--user', default=os.getenv('PGUSER', getpass.getuser()))
    parser.add_argument('--password', default=os.getenv('PGPASSWORD'))
    args = parser.parse_args()

    if not args.password:
        try:
            args.password = getpass.getpass(f"Password for {args.user}@{args.host}:{args.port} (leave empty if not needed): ")
        except Exception:
            args.password = None

    conn = None
    try:
        conn = psycopg2.connect(host=args.host, port=args.port, dbname=args.dbname, user=args.user, password=args.password, connect_timeout=5)
    except Exception as e:
        print('Connection failed:', e)
        sys.exit(1)

    print(f"Connected to database '{args.dbname}' on {args.host}:{args.port} as {args.user}")
    cur = conn.cursor()

    # Create simple tables if they don't exist
    cur.execute("""
    CREATE TABLE IF NOT EXISTS todos (
      id TEXT PRIMARY KEY,
      title TEXT NOT NULL,
      description TEXT,
      status TEXT DEFAULT 'pending',
      created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
      updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS todo_deps (
      todo_id TEXT,
      depends_on TEXT,
      PRIMARY KEY (todo_id, depends_on)
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS inbox_entries (
      id SERIAL PRIMARY KEY,
      content TEXT,
      created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    conn.commit()
    cur.close()
    conn.close()

    print('Ensured tables: todos, todo_deps, inbox_entries')


if __name__ == '__main__':
    main()
