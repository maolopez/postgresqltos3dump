from postgresqltos3dump import storage #1
import tempfile #1
import pytest #2

@pytest.fixture #2
def infile(): #2
    f = tempfile.TemporaryFile() #2
    f.write(b"Testing") #2
    f.seek(0) #2
    return f

#def test_storing_file_locally(): #1
def test_storing_file_locally(infile): #2
    """
    Writes content from one file-like to another
    """
    #infile = tempfile.TemporaryFile() #1
    #infile.write(b"Testing") #1
    #infile.seek(0) #1
    outfile = tempfile.NamedTemporaryFile(delete=False) #1
    storage.local(infile, outfile) #1
    with open(outfile.name, "rb") as f: #1
    	assert f.read() == b"Testing" #1

def test_storing_file_locally(mocker, infile): #2
    """
    Writes content to AWS S3
    """
    client = mocker.Mock() #3
    storage.s3(client, infile, "bucket", "file-name") #2
    client.upload_fileobj.assert_called_with(infile, "bucket", "file-name")#2   	



#NameError: name 'tempfile' is not defined  import tempfile
#AttributeError: module 'postgresqltos3dump.storage' has no attribute 'local'
#2#3 AttributeError: module 'postgresqltos3dump.storage' has no attribute 's3'

#https://docs.python.org/3/library/tempfile.html
#https://docs.python.org/3/library/tempfile.html#tempfile.TemporaryFile
#https://docs.python.org/3/library/tempfile.html#tempfile.NamedTemporaryFile	
#https://boto3.readthedocs.io/en/latest/reference/services/s3.html#S3.Client.upload_fileobj