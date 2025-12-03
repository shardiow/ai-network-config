 import yaml
from git import Repo
from network_runner import get_running_config, apply_config

REPO_PATH = "."  # local working directory of your repo

def main():
    print("[AI AGENT] Starting network automation engine...")

    repo = Repo(REPO_PATH)
    repo.remotes.origin.pull()

    with open("inventory/devices.yml") as f:
        inventory = yaml.safe_load(f)

    for device in inventory["devices"]:
        device_name = device["name"]
        vendor = device["vendor"]

        desired_file = f"desired-configs/{device_name}.cfg"

        try:
            with open(desired_file) as f:
                desired_config = f.read()
        except FileNotFoundError:
            print(f"[!] No desired config for {device_name}. Skipping.")
            continue

        print(f"\n[+] Checking device: {device_name}")

        running_config = get_running_config(device)

        if running_config.strip() != desired_config.strip():
            print(f"[!] Config drift detected on {device_name}")
            print(f"[+] Applying new configuration...")
            apply_config(device, desired_config)
        else:
            print(f"[✓] {device_name} is up-to-date.")

    repo.git.add(all=True)
    repo.index.commit("AI agent applied new network configs")
    repo.remotes.origin.push()

    print("\n[✓] Deployment complete.")

if __name__ == "__main__":
    main()
