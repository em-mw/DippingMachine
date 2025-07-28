import psutil
import platform
import os

def find_pico_drive():
    for part in psutil.disk_partitions(all=False):
        try:
            if platform.system() == "Windows":
                volume_label = os.path.basename(part.mountpoint.rstrip("\\/"))
            else:
                # On Linux, check mount path directly
                volume_label = os.path.basename(part.mountpoint)
            
            if "RPI-RP2" in volume_label or "CIRCUITPY" in volume_label:
                return part.device, part.mountpoint
        except Exception:
            continue
    return None, None

device, mountpoint = find_pico_drive()
if mountpoint:
    print(f"Pico detected at: {mountpoint} ({device})")
else:
    print("Pico not found.")

