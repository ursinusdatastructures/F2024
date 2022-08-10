import subprocess

fin = open(".gitmodules")
lines = fin.readlines()
for line in lines:
    if "path" in line:
        s = line.split("path = ")[-1].rstrip()
        subprocess.call(["git", "rm", s])
fin.close()
