import os
import sys
import sqlite3
import time
from datetime import datetime

def display_banner():
    banner_text = '''
     (                                                   
     )\ )                   )                         )  
    (()/(            )   ( /(   (        )         ( /(  
     /(_))   (    ( /(   )\())  )(    ( /(    (    )\()) 
    (_))_|   )\   )\()) (_))/  (()\   )(_))   )\  (_))/  
    | |_    ((_) ((_)\  | |_    ((_) ((_)_   ((_) | |_   
    | __|  / _ \ \ \ /  |  _|  | '_| / _` | / _|  |  _|  
    |_|    \___/ /_\_\   \__|  |_|   \__,_| \__|   \__|         
    
        Firefox Browser History Extraction Tool
    '''
    print(banner_text)

if len(sys.argv) < 2:
    display_banner()
    print("    Usage: Foxtract.exe -f <places.sqlite> [--format]")
    print("\n")
    sys.exit(1)

if sys.argv[1] != '-f':
    display_banner()
    print("Invalid argument: use -f to specify the path to the places.sqlite file")
    sys.exit(1)

if len(sys.argv) < 3:
    display_banner()
    print("Missing argument: specify the path to the places.sqlite file after -f")
    sys.exit(1)

db_path = sys.argv[2]

if not os.path.isfile(db_path):
    display_banner()
    print(f"Error: {db_path} is not a valid file path")
    sys.exit(1)

format_output = False
if len(sys.argv) >= 4 and sys.argv[3] == "--format":
    format_output = True

conn = sqlite3.connect(db_path)
cursor = conn.cursor()
cursor.execute('SELECT url, visit_count, last_visit_date FROM moz_places ORDER BY last_visit_date DESC')
results = cursor.fetchall()

if format_output:
    display_banner()
    for url, visit_count, last_visit_date in results:
        last_visit_date_str = "N/A"
        if last_visit_date:
            last_visit_date_epoch = int(last_visit_date) // 1000000
            last_visit_date_str = datetime.fromtimestamp(last_visit_date_epoch).strftime('%Y-%m-%d %H:%M:%S')
        filename = url.split("/")[-1]
        print(f'URL: {url}\nVisits: {visit_count}\nLast Visit: {last_visit_date_str}\n')
else:
    for url, visit_count, last_visit_date in results:
        last_visit_date_str = "N/A"
        if last_visit_date:
            last_visit_date_epoch = int(last_visit_date) // 1000000
            last_visit_date_str = datetime.fromtimestamp(last_visit_date_epoch).strftime('%Y-%m-%d %H:%M:%S')
        print(f'{url}: visits={visit_count}, last visit={last_visit_date_str}')
