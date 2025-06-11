# Bobcat Miner Auto-Rebooter

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.7+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/license-MIT-green.svg" alt="License">
</p>

A simple yet effective Python script to monitor the health of your Bobcat Helium Miner and automatically reboot it if the NAT status becomes unfavorable. Keep your miner online and syncing without manual intervention.

---

## ⚠️ Disclaimer

This script interacts with your miner's local administrative functions. The default username and password (`bobcat`, `miner`) are used for authentication. Use this script at your own risk. The author is not responsible for any issues that may arise from its use.

---

## ✨ Features

-   **Automatic Status Monitoring**: Periodically checks the miner's status via its local API.
-   **Smart Reboot**: Triggers a reboot only when the `nat_type` is not `none`.
-   **Customizable Interval**: Set the time (in seconds) between status checks.
-   **Command-Line Interface**: Easy to run with simple command-line arguments.
-   **Lightweight**: Minimal dependencies, requiring only the `requests` library.

---

## 🚀 Getting Started

### Prerequisites

-   Python 3.7 or newer.
-   Your Bobcat miner must be on the same local network as the machine running the script.
-   You need to know your miner's local IP address.

### Installation

1.  **Clone the repository** or download the `bobcat_rebooter.py` script.
    ```sh
    git clone https://github.com/tberndt5/bobcat-miner-autoreloader.git
    ```

2.  **Install the required Python library**:
    ```sh
    pip install requests
    ```

---

## ⚙️ Usage

Run the script from your terminal, providing the miner's IP address and a sleep interval in seconds.

**Example**: To check the miner at `192.168.1.55` every hour (3600 seconds):

```sh
python bobcat_rebooter.py --ip 192.168.1.55 --sleep 3600
```

### Command-Line Arguments

-   `--ip` (Required): The local IP address of your Bobcat miner.
-   `--sleep` (Required): The time in seconds to wait between each status check.

---

## 🔧 How It Works

The script operates in an infinite loop with the following logic:

1.  **Fetch Status**: It sends a `GET` request to `http://<MINER_IP>/miner.json` to retrieve the miner's current status.
2.  **Check NAT Type**: It parses the JSON response and specifically checks the value of `p2p_status` which contains the `nat_type`. The script considers `none` as the healthy state.
3.  **Evaluate and Act**:
    -   If the `nat_type` is `none`, it prints a "good" status message and waits for the next cycle.
    -   If the `nat_type` is anything else (e.g., `symmetric`, `restricted`), it prints an error, then sends an authenticated `POST` request to `http://<MINER_IP>/admin/reboot` to restart the miner.
4.  **Wait**: The script then sleeps for the user-defined interval before starting the process again.

---

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for details.
