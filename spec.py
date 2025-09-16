
import platform

def get_system_info():
    system_info = platform.uname()
    print("--- System Information ---")
    print(f"System: {system_info.system}")
    print(f"Node Name: {system_info.node}")
    print(f"Release: {system_info.release}")
    print(f"Version: {system_info.version}")
    print(f"Machine: {system_info.machine}")
    print(f"Processor: {system_info.processor}")

get_system_info()
#shameless pull from the internet lol