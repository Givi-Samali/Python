import subprocess
text = subprocess.check_output('ver', shell=True)
print(text.decode('cp866'))
