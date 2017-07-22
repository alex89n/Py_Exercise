import subprocess

p = subprocess.Popen('dir', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

x = p.stdout.readlines()
#y = x.decode("utf-8")

for line in x:
    

    print line,
retval = p.wait()
