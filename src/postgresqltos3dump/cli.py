from argparse import ArgumentParser #2
from argparse import Action #4

known_drivers = ['local', 's3'] #5

class DriverAction(Action): #4
    def __call__(self, parser, namespace, values, option_string=None): #4
        driver, destination = values #4
        if driver.lower() not in known_drivers: #5
            parser.error("Unknown driver. Drivers are 'local' and 's3'") #5
        namespace.driver = driver.lower() #4
        namespace.destination = destination #4

def create_parser(): #1
    #pass #1
    parser = ArgumentParser() #2
    parser.add_argument("url", help="URL of the PostgreSQL") #3
    parser.add_argument("--driver", '-d',
    	help="how and where to store the dump",
    	nargs=2,
    	action=DriverAction,
        metavar=('driver', 'destination'),
    	required=True) #4
    return parser #2

def main(): #6
    import time #7
    import boto3 #6
    from postgresqltos3dump import pgdump, storage #6
    args = create_parser().parse_args() #6 not parser_args()
    dump = pgdump.dump(args.url) #6
    if args.driver == 's3': #6
        client = boto3.client("s3") #6
        timestamp = time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime()) #7
        file_name = pgdump.dump_file_name(args.url, timestamp) #7
        #storage.s3(client, dump.stdout, args.destination, 'example.sql') #6
        storage.s3(client, dump.stdout, args.destination, file_name) #7
        print(f"Dumping database up to {args.destination} in S3 as {file_name}") #7
    else:
        outfile = open(args.destination, 'wb')
        print(f"Dumping database up locally {args.destination}") #7
        storage.local(dump.stdout, outfile)   


#1failure unrecognized arguments: postgres://mao@example.com:5432/db_one --driver local /some/path\n'
#2 we are passing too much stuff at a time SystemExit: 2
#3 unrecognized arguments: --driver local /some/path\n'
#4 PASS
#test_parser_with_unknown_driver: Failed: DID NOT RAISE <class 'SystemExit'>
#5 PASS
#FINAL ERROR: postgresqltos3dump --driver local ./local-dump.sql postgres://postgres:password@18.220.100.208:80/sample
#

