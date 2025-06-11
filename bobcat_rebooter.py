import requests
import argparse
import time
from re import search

# Parsing rules
parser = argparse.ArgumentParser(description='Setup information for script')
parser.add_argument('--ip',type=str,required=True,help="Enter IP address. Ex. 192.168.x.x")
parser.add_argument('--sleep',type=int,required=True,help="Enter time to sleep in seconds.")
args = parser.parse_args()

# Global URL variables
status_url = 'http://{}/miner.json'.format(args.ip)
reboot_url = 'http://{}/admin/reboot'.format(args.ip)

status_good = "none"
nat_type_num = 5

while True:
    try:
        r = requests.get(status_url)
        data = r.json()
        status = data['p2p_status'][nat_type_num]
        if search(status_good,status):
            print("[STATUS] Miner is good")
        else:
            print("[ERROR] Miner nat_type is bad... \nGoing to reboot")
            r = requests.post(reboot_url,auth=('bobcat','miner'))
            time.sleep(120)
    except:
        print('[ERROR] Check IP address or bobcat miner power.')
    time.sleep(args.sleep)
