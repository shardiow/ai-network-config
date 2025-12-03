# agent/network_runner.py

from netmiko import ConnectHandler
import os # <--- ADD THIS

# ... (rest of the file remains the same)

def get_running_config(device):
   # Load credentials from Environment Variables if available, otherwise use inventory
   conn_info = device.copy()
   conn_info['username'] = os.environ.get('NETWORK_USERNAME', conn_info.get('username')) # <--- ADD/MODIFY
   conn_info['password'] = os.environ.get('NETWORK_PASSWORD', conn_info.get('password')) # <--- ADD/MODIFY
   
   conn = ConnectHandler(**conn_info) # <--- USE conn_info
   output = conn.send_command("show running-config")
   conn.disconnect()
   return output
 
def apply_config(device, config):
   # Load credentials from Environment Variables if available, otherwise use inventory
   conn_info = device.copy()
   conn_info['username'] = os.environ.get('NETWORK_USERNAME', conn_info.get('username')) # <--- ADD/MODIFY
   conn_info['password'] = os.environ.get('NETWORK_PASSWORD', conn_info.get('password')) # <--- ADD/MODIFY
 
   conn = ConnectHandler(**conn_info) # <--- USE conn_info
   print(f"[+] Sending config to {device['name']}...")
   conn.send_config_set(config.split("\n"))
   conn.save_config()
   conn.disconnect()
