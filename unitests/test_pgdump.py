import pytest #1
import subprocess #1
from postgresqltos3dump import pgdump #1

url = "postgres://mao@example.com:5432/db_one" #1

def test_dump_calls_pg_dump(mocker): #1
	"""
	utilize pg_dump with the database URL
	"""
	mocker.patch("subprocess.Popen") #1
	assert pgdump.dump(url) #1
	subprocess.Popen.assert_called_with(["pg_dump", url], stdout=subprocess.PIPE) #1

def test_dump_handles_oserror(mocker): #4
    """
    pgdump.dump returns error if pg_dump is not installed
    """
    mocker.patch("subprocess.Popen", side_effect=OSError("not such file")) #4
    with pytest.raises(SystemExit):
        pgdump.dump(url) #4	

def test_dump_file_name_without_timestamp(): #5
    """
    returns the name of the database
    """
    assert pgdump.dump_file_name(url) == "db_one.sql" #5

def test_dump_file_name_with_timestamp(): #5
    """
    add a timestamp name for the s3 dump file timestamp.sql
    """
    timestamp = "2020-03-14T00:00:00"
    assert pgdump.dump_file_name(url, timestamp) == f"db_one-{timestamp}.sql" #5


#	https://docs.pytest.org/en/latest/
#https://docs.pytest.org/en/latest/assert.html#assertions-about-expected-exceptions
#https://github.com/pytest-dev/pytest-mock/#usage
#https://docs.python.org/3/library/subprocess.html#subprocess.Popen
#1 Failure : ImportError: cannot import name 'pgdump'
#5 reference pgdump.py
#5 AttributeError: module 'postgresqltos3dump.pgdump' has no attribute 'dump_file_name' go to pgdump.py
