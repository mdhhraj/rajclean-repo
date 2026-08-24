#!/usr/bin/env python3
import os, shutil, hashlib, time
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor

INTERNAL = "/storage/emulated/0"
EXTERNAL = "/storage/5F34-6C6B"
TRASH = ".rajclean_trash"

EXTRA_PATHS = [
    "/storage/emulated/0/Android/data",
    "/storage/emulated/0/Android/obb",
    "/storage/5F34-6C6B"
]

C = {
    "LG":"\033[92m",
    "Y":"\033[93m",
    "V":"\033[95m",
    "C":"\033[96m",
    "X":"\033[0m"
}

def clear():
    os.system("clear")

def w():
    try:
        return os.get_terminal_size().columns
    except:
        return 40

def center(t):
    return t.center(w())

def scan(path):
    files=[]
    for r,_,fs in os.walk(path):
        for f in fs:
            files.append(os.path.join(r,f))
    return files

def scan_worker(paths):
    print("Scanning...")

    files=[]
    total=len(paths)

    for i,p in enumerate(paths,1):
        if os.path.exists(p):
            files += scan(p)

        bar="█"*(int(i/total*30))+"-"*(30-int(i/total*30))
        print(f"\r[{bar}] {int((i/total)*100)}%", end="")
        time.sleep(0.02)

    print()
    return files

def hash_file(p):
    try:
        h=hashlib.md5()
        with open(p,"rb") as f:
            for c in iter(lambda:f.read(65536),b""):
                h.update(c)
        return h.hexdigest()
    except:
        return None

def find_duplicates(files):
    size_map=defaultdict(list)

    for f in files:
        try:
            size_map[os.path.getsize(f)].append(f)
        except:
            pass

    candidates=[f for g in size_map.values() if len(g)>1 for f in g]

    hash_map=defaultdict(list)

    def worker(f):
        return f, hash_file(f)

    with ThreadPoolExecutor(max_workers=8) as ex:
        for f,h in ex.map(worker, candidates):
            if h:
                hash_map[h].append(f)

    dup=[]
    for g in hash_map.values():
        if len(g)>1:
            g.sort(key=os.path.getmtime)
            dup += g[1:]

    return dup

def find_junk(files):
    keys=["cache","temp","thumb",".log",".tmp"]
    return [f for f in files if any(k in f.lower() for k in keys)]

def move(files):
    trash=os.path.join(INTERNAL,TRASH)
    os.makedirs(trash,exist_ok=True)

    total=len(files)

    for i,f in enumerate(files,1):
        try:
            shutil.move(f,os.path.join(trash,os.path.basename(f)))
        except:
            pass

        bar="█"*(int(i/total*30))+"-"*(30-int(i/total*30))
        print(f"\rCleaning [{bar}] {int((i/total)*100)}%", end="")

    print()

def clean():
    while True:
        clear()

        # CENTERED HEADER ONLY
        print(center("🅁🄰🄹🄲🄻🄴🄰🄽 🅃🅄🅁🄱🄾 🄿🅁🄾"))
        print(center("🅰🅿🅿 🆅🅴🆁🆂🅸🅾🅽 8.1"))
        print(center("🄳🄴🅅🄴🄻🄾🄿🄴🄳 🄱🅈: 🄷🄰🅂🄸🄱🅄🄻 🄷🄰🅂🄰🄽 🅁🄰🄹🄸🄱"))
        print()

        print(C["Y"] + "Select 1 to 3 to clean, and 4 for exit the tool." + C["X"])
        print()

        print(C["LG"] + "1 Internal Scan")
        print("2 External Scan")
        print("3 Both Scan")
        print("4 Exit" + C["X"])
        print()

        choice=input("Select: ").strip()

        if choice=="4":
            clear()
            print("👋 Thank you for using RajClean")
            print("👨‍🏫 Hasibul Hasan Rajib")
            print("🌐 github.com/mdhhraj")
            return

        paths=[INTERNAL] if choice=="1" else [EXTERNAL] if choice=="2" else EXTRA_PATHS

        files=scan_worker(paths)

        dup=find_duplicates(files)
        junk=find_junk(files)

        print("\nPreview")
        print("Duplicates:",len(dup))
        print("Junk:",len(junk))

        print("\n1 Preview sample")
        print("2 Clean now")
        print("3 Back")

        c=input("Select: ").strip()

        if c=="1":
            for f in (dup+junk)[:10]:
                print(" -",f)
            input("\nEnter...")
        elif c=="2":
            move(dup+junk)
            print("\nDone ✔")
            input("Enter...")
        else:
            continue

if __name__ == "__main__":
    import sys

    if "--version" in sys.argv or "-v" in sys.argv:
        print("RajClean Turbo Pro 8.2")
        sys.exit(0)

    if "--help" in sys.argv or "-h" in sys.argv:
        print("""
RajClean Turbo Pro 8.2

Usage:
  rajclean              Open interactive cleaner
  rajclean --help       Show this help
  rajclean --version    Show version

Options:
  -h, --help            Show help information
  -v, --version         Show application version
""".strip())
        sys.exit(0)

    clean()
