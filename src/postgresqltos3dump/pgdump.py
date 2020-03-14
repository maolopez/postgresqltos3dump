import subprocess #3
import sys #5

def dump(url): #1
	#pass #1
    #return 1 #2
    try: #5
        return subprocess.Popen(["pg_dump", url], stdout=subprocess.PIPE) #3
    except OSError as err: #5
        print(f"Error: {err}") #5
        sys.exit(1) #5  

def dump_file_name(url, timestamp=None): #5
    #pass  #5
    db_name = url.split("/")[-1] #6
    db_name = db_name.split("?")[0] #6
    if timestamp: #6
        return f"{db_name}-{timestamp}.sql" #6
    else:
        return f"{db_name}.sql"       #6

#1 assert pgdump.dump(url) AssertionError: assert None
#2 AssertionError: Expected call: Popen(['pg_dump', 'postgres://mao@example.com:5432/db_one'], stdout=-1)
#3 PASS
#5 	OSError: not such file
#5 PASS reference test_pgdump.py

