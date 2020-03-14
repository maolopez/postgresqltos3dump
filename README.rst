postgresqltos3
==============

CLI for backing up remote PostgreSQL databases locally or to AWS S3.
Follow up the original project: 
https://github.com/linuxacademy/content-python3-sysadmin/tree/master/pgbackup

Preparing for Development
-------------------------

1. Ensure ``pip`` and ``pipenv`` are installed
2. Clone repository: ``git clone git@github.com:example/postgresqltos3``
3. ``cd`` into repository
4. Fetch development dependencies ``make install``
5. Activate virtualenv: ``pipenv shell``

Usage
-----

Pass in a full database URL, the storage driver, and destination.

S3 Example w/ bucket name:

::

    $ postgresqltos3dump postgres://mao@example.com:5432/db_one --driver s3 backups

Local Example w/ local path:

::

    $ postgresqltos3dump postgres://mao@example.com:5432/db_one --driver local /var/local/db_one/backups
    $ postgresqltos3dump --driver local ./local-dump.sql postgres://postgres:password@18.220.100.208:80/sample
    $ postgresqltos3dump --driver s3 mao1 postgres://postgres:password@18.220.100.208:80/sample

Running Tests
-------------

Run tests locally using ``make`` if virtualenv is active:

::

    $ make

If virtualenv isn’t active then use:

::

    $ pipenv run make

Verifying the local dump manually
---------------------------------

PYTHONPATH=./src python

from postgresqltos3dump import pgdump

proc = pgdump.dump('postgres://postgres:password@18.220.100.208:80/sample')

f = open('dump.sql', 'wb')

f.write(dump.stdout.read())

f.write(proc.stdout.read())

f.close()

exit()

cat dump.sql 


Verifying the s3 dump manually
------------------------------

echo "UPLOADED" > example.txt

PYTHONPATH=./src python

import boto3

from postgresqltos3dump import storage

client = boto3.client('s3')

infile = open('example.txt', 'rb')

storage.s3(client, infile, 'mao1', infile.name)

exit()


Verify the wheel remotely
-------------------------
python

import boto3

f = open('dist/postgresqltos3dump-1.0-py36-none-any.whl', 'rb')

client = boto3.client('s3')

client.upload_fileobj(f, 'mao1', 'postgresqltos3dump-1.0-py36-none-any.whl')

exit()

NOTE: my_bucket = mao1
