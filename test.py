import subprocess
import re

def check_bios():
    try:
        bios_info = subprocess.check_output('dmidecode -t system', shell=True).decode()
        indicators = ['VMware', 'VirtualBox', 'QEMU', 'Xen', 'Hyper-V']
        if any(indicator in bios_info for indicator in indicators):
            return True
    except subprocess.CalledProcessError:
        return False
    return False

def check_devices():
    device_info = subprocess.check_output('lspci', shell=True).decode()
    indicators = ['VMware', 'VirtualBox', 'QEMU', 'Xen', 'Hyper-V']
    if any(indicator in device_info for indicator in indicators):
        return True
    return False

def check_processes():
    process_info = subprocess.check_output('ps aux', shell=True).decode()
    indicators = ['vmtoolsd', 'VBoxService']
    if any(indicator in process_info for indicator in indicators):
        return True
    return False

def is_virtual_machine():
    if check_bios():
        return "VM Detected: BIOS information suggests a virtual environment."
    elif check_devices():
        return "VM Detected: Virtual devices found."
    elif check_processes():
        return "VM Detected: Virtual machine processes are running."
    else:
        return "No VM indicators found. Likely a physical machine."

if __name__ == "__main__":
    print(is_virtual_machine())