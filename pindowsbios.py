import subprocess
import platform

def komut(c):
    try:
        return subprocess.check_output(c, shell=True, text=True, stderr=subprocess.DEVNULL)
    except:
        return "erişim yok"

def bios_bilgi():
    print("=== BIOS ===")
    print(komut("wmic bios get Manufacturer,Name,Version,ReleaseDate"))

def anakart_bilgi():
    print("=== ANAKART ===")
    print(komut("wmic baseboard get Manufacturer,Product,Version,SerialNumber"))

def cpu_bilgi():
    print("=== CPU ===")
    print(komut("wmic cpu get Name,NumberOfCores,NumberOfLogicalProcessors,MaxClockSpeed"))

def ram_bilgi():
    print("=== RAM ===")
    print(komut("wmic memorychip get Manufacturer,Capacity,Speed,PartNumber"))

def disk_bilgi():
    print("=== DISKLER ===")
    print(komut("wmic diskdrive get Model,Size,InterfaceType"))

def sistem():
    print("=== SISTEM ===")
    print("Sürüm:", platform.version())
    print("Sistem:", platform.system())
    print("Mimari:", platform.machine())

bios_bilgi()
anakart_bilgi()
cpu_bilgi()
ram_bilgi()
disk_bilgi()
sistem()
