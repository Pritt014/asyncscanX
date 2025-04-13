Here's the updated README.md for your project with the new details:
# asyncscanX

A fast and efficient port scanner built with `asyncio` in Python, designed to scan all ports from 0 to 65535 and report open ports with labels (e.g., HTTP, HTTPS, SSH). This scanner works asynchronously to maximize speed and minimize waiting times.

## Features
- Asynchronous scanning using `asyncio` for faster execution.
- Labels known ports with human-readable names (e.g., HTTP, SSH, SMTP).
- Reports only **open** ports, keeping the output clean and readable.
- Semaphore to limit concurrency (default: 100 threads)
- Easy-to-use command-line interface (CLI).

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/Pritt014/asyncscanX.git
   ```
2.	Navigate into the project directory:
3.	cd asyncscanX
4.	No additional dependencies are needed; the script uses built-in Python libraries (asyncio, socket).

## Usage
Run the script with Python 3:
```bash
python3 async.py
```
You will be prompted to enter the host or IP address you wish to scan.
Example:
Enter host for scanning: example.com or IP
The script will display the open ports along with their labels, such as:
Port 22 (SSH): OPEN
Port 80 (HTTP): OPEN
Port 443 (HTTPS): OPEN
Port 587 (SMTP (secure)): OPEN

## Supported Ports
The script labels well-known ports like:
•	22 – SSH
•	80 – HTTP
•	443 – HTTPS
•	21 – FTP
•	25 – SMTP
•	53 – DNS
•	110 – POP3
•	143 – IMAP
•	465 – SMTPS
•	587 – SMTP (secure)
•	993 – IMAPS
•	995 – POP3S
•	3306 – MySQL
•	5432 – PostgreSQL
If the port is not labeled in the dictionary, it will show up as "Unknown Port."

## Example Output
Port 22 (SSH): OPEN
Port 80 (HTTP): OPEN
Port 443 (HTTPS): OPEN
Port 587 (SMTP (secure)): OPEN

## Contributing
Feel free to fork this project and contribute. If you find any bugs or have ideas for improvements, create an issue or submit a pull request.

## License
This project is licensed under the MIT License 


