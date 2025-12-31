import subprocess
import platform
import os

def komut(c):
    try:
        return subprocess.check_output(c.split(), text=True, stderr=subprocess.DEVNULL)
    except:
        return "erişim yok"

def paket_kontrol():
    print("=== dmidecode kontrolü ===")
    kontrol = subprocess.call("which dmidecode", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if kontrol != 0:
        print("dmidecode bulunamadı. Yükleniyor...")
        try:
            subprocess.call("sudo apt update", shell=True)
            subprocess.call("sudo apt install -y dmidecode", shell=True)
            print("dmidecode yüklendi.")
        except:
            print("dmidecode yüklenemedi.")
    else:
        print("dmidecode zaten kurulu.")

def bios_bilgi():
    print("=== BIOS ===")
    print(komut("sudo dmidecode -t bios"))

def anakart_bilgi():
    print("=== ANAKART ===")
    print(komut("sudo dmidecode -t baseboard"))

def cpu_bilgi():
    print("=== CPU ===")
    print(komut("lscpu"))

def ram_bilgi():
    print("=== RAM ===")
    print(komut("sudo dmidecode -t memory"))

def disk_bilgi():
    print("=== DISKLER ===")
    print(komut("lsblk -o NAME,SIZE,MODEL"))

def sistem():
    print("=== SISTEM ===")
    print("Kernel:", platform.release())
    print("Mimari:", platform.machine())
    try:
        # modern distrolarda kaldırıldı, fallback yapıyoruz
        out = komut("uname -a")
        print("Sistem:", out)
    except:
        pass

def secureboot():
    yol = "/sys/firmware/efi/secureboot/enabled"
    if os.path.exists(yol):
        try:
            durum = open(yol).read().strip()
            print("SecureBoot:", durum)
        except:
            print("SecureBoot: okunamadı")
    else:
        print("SecureBoot: yok")

def efi_legacy():
    if os.path.exists("/sys/firmware/efi"):
        print("Boot Modu: UEFI")
    else:
        print("Boot Modu: Legacy")

paket_kontrol()
bios_bilgi()
anakart_bilgi()
cpu_bilgi()
ram_bilgi()
disk_bilgi()
sistem()
secureboot()
efi_legacy()
