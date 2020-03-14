#Red > Green > Refactor
#postgresqltos3dump postgres://mao@example.com:5432/db_one --driver s3 backups

import pytest
from postgresqltos3dump import cli 

url = "postgres://mao@example.com:5432/db_one" #1

@pytest.fixture #3 adding a decorator
def parser():
	return cli.create_parser() #3

#def test_parser_without_driver(): #1
def test_parser_without_driver(parser): #3
    """
    Without the driver the parser exit
    https://docs.pytest.org/en/latest/assert.html#assertions-about-expected-exceptions
    """
    with pytest.raises(SystemExit): #1
         #parser = cli.create_parser() #1
         parser.parse_args([url]) #1

#def test_parser_with_driver(): #1
def test_parser_with_driver(parser): #3
    """
    The parser exit for driver without destination
    """
    #parser = cli.create_parser() #1
    with pytest.raises(SystemExit): #1
         parser.parse_args([url, "--driver", "local"]) #1

#def test_parser_with_unknown_driver(): #2
def test_parser_with_unknown_driver(parser): #3
    """
    The parser exit for unkown driver
    """
    #parser = cli.create_parser() #2
    with pytest.raises(SystemExit): #2
         parser.parse_args([url, "--driver", "azure", "destination"]) #2   

#def test_parser_with_known_driver(): #
def test_parser_with_known_driver(parser): #3
    """
    The parser will not exit for known driver
    """
    #parser = cli.create_parser() #2
    for driver in ["local", "s3"]: #2
    	assert parser.parse_args([url, "--driver", driver, "destination"]) #2
    
#def test_parser_with_driver_and_destination(): #2
def test_parser_with_driver_and_destination(parser): #3
    """
    sucess with driver and destination
    """
    #parser = cli.create_parser() #1
    args = parser.parse_args([url, "--driver", "local", "/some/path"]) #1
    assert args.url == url #1
    assert args.driver == "local" #1
    assert args.destination == "/some/path" #1

#First failure ImportError: cannot import name 'cli' touch src/postgresqltos3dump/cli.py
#First-b failure AttributeError: module 'postgresqltos3dump.cli' has no attribute 'create_parser'    
#First-c failure AttributeError: 'NoneType' object has no attribute 'parse_args': parser = None
#failure unrecognized arguments: postgres://mao@example.com:5432/db_one --driver local /some/path\n'
#we are passing too much stuff at a time SystemExit: 2
#test_parser_without_driver fail and test_parser_with_driver_and_destination fail
#unrecognized arguments: --driver local /some/path\n'
#2 it is implemented after #4 in cli.py PASS

