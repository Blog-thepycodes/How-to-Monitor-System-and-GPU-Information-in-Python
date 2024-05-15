import tkinter as tk
from tkinter import scrolledtext
import psutil
import GPUtil
 
 
def get_hardware_info():
   hardware_info.delete(1.0, tk.END)  # Clear previous info
 
 
   # Disk Drives
   hardware_info.insert(tk.END, "Disk Drives:\n")
   for partition in psutil.disk_partitions():
       hardware_info.insert(tk.END, f"Mountpoint: {partition.mountpoint}\n")
       try:
           usage = psutil.disk_usage(partition.mountpoint)
           hardware_info.insert(tk.END, f"Total Size: {usage.total / (1024 ** 3):.2f} GB\n")
           hardware_info.insert(tk.END, f"Used: {usage.used / (1024 ** 3):.2f} GB\n")
           hardware_info.insert(tk.END, f"Free: {usage.free / (1024 ** 3):.2f} GB\n")
           hardware_info.insert(tk.END, f"Percentage: {usage.percent}%\n\n")
       except PermissionError:
           hardware_info.insert(tk.END, "Access denied\n\n")
 
 
   # Network Adapters
   hardware_info.insert(tk.END, "Network Adapters:\n")
   for interface, addrs in psutil.net_if_addrs().items():
       hardware_info.insert(tk.END, f"Interface: {interface}\n")
       for addr in addrs:
           hardware_info.insert(tk.END, f"  Address Family: {addr.family}\n")
           hardware_info.insert(tk.END, f"  Address: {addr.address}\n")
           if addr.netmask:
               hardware_info.insert(tk.END, f"  Netmask: {addr.netmask}\n")
           if addr.broadcast:
               hardware_info.insert(tk.END, f"  Broadcast IP: {addr.broadcast}\n")
           if addr.ptp:
               hardware_info.insert(tk.END, f"  MAC Address: {addr.ptp}\n")
           hardware_info.insert(tk.END, "\n")
 
 
   # Graphics Processing Units (GPUs)
   hardware_info.insert(tk.END, "Graphics Processing Units (GPUs):\n")
   gpus = GPUtil.getGPUs()
   if gpus:
       for gpu in gpus:
           hardware_info.insert(tk.END, f"Name: {gpu.name}\n")
           hardware_info.insert(tk.END, f"GPU ID: {gpu.id}\n")
           hardware_info.insert(tk.END, f"Load: {gpu.load * 100:.1f}%\n")
           hardware_info.insert(tk.END, f"Memory Total: {gpu.memoryTotal} MB\n")
           hardware_info.insert(tk.END, f"Memory Used: {gpu.memoryUsed} MB\n")
           hardware_info.insert(tk.END, f"Memory Free: {gpu.memoryFree} MB\n")
           hardware_info.insert(tk.END, f"Memory Utilization: {gpu.memoryUtil * 100:.1f}%\n")
           hardware_info.insert(tk.END, f"Temperature: {gpu.temperature} °C\n\n")
   else:
       hardware_info.insert(tk.END, "No compatible GPU found.\n")
 
 
 
# Create the main application window
root = tk.Tk()
root.title("Hardware Information - The Pycodes")
 
 
# Create a scrolled text widget to display hardware info
hardware_info = scrolledtext.ScrolledText(root, width=80, height=30, wrap=tk.WORD)
hardware_info.pack(expand=True, fill="both", padx=10, pady=10)
 
 
# Create a button to fetch hardware info
fetch_button = tk.Button(root, text="Fetch Hardware Info", command=get_hardware_info)
fetch_button.pack(pady=10)
 
 
# Run the Tkinter event loop
root.mainloop()
