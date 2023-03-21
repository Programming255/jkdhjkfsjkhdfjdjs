import subprocess

# list of scripts to run
scripts = ["gen.py","runenvdeb.py", "del.py"]

# run each script
for i in range(1000000):
    for script in scripts:
        subprocess.run(["python", script])
