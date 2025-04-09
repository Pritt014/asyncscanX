#!/bin/python3

import asyncio
import time
from socket import gethostbyname
from asyncio import Lock

start_time = time.time()
print_lock = Lock()

# Dictionary to label well-known ports
PORT_LABELS = {
    22: "SSH",
    21: "FTP",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    443: "HTTPS",
    110: "POP3",
    143: "IMAP",
    465: "SMTPS",
    587: "SMTP (secure)",
    993: "IMAPS",
    995: "POP3S",
    3306: "MySQL",
    8080: "HTTP Proxy",
    5432: "PostgreSQL"
}

async def scan_port(target, port):
    """Function to scan a single port asynchronously and label it"""
    try:
        # Create a non-blocking socket connection
        reader, writer = await asyncio.open_connection(target, port)
        port_name = PORT_LABELS.get(port, "Unknown Port")  # Get label for the port
        async with print_lock:  # Prevent print collisions in async tasks
            print(f'Port {port} ({port_name}): OPEN')
        writer.close()
        await writer.wait_closed()
    except Exception:
        pass  # Do nothing if the port is closed

async def scan_ports(target):
    """Function to scan ports concurrently using asyncio"""
    t_IP = gethostbyname(target)  # Resolve the target to an IP address
    print('Starting scanning on host:', t_IP)
    
    # Create a list of tasks for scanning each port
    tasks = []
    for port in range(0, 65535):
        task = asyncio.create_task(scan_port(t_IP, port))
        tasks.append(task)
        
        # Delay every 100 ports to slow things down a bit (to see progress)
        if port % 100 == 0:
            await asyncio.sleep(0.1)  # Adding a small delay for visibility
    
    # Wait for all tasks to complete
    await asyncio.gather(*tasks)

def main():
    target = input('Enter host for scanning: ')
    asyncio.run(scan_ports(target))
    print('Time taken:', time.time() - start_time)

if __name__ == '__main__':
    main()
