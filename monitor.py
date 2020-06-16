import os
import psutil
print("RAM ", dict(psutil.virtual_memory()._asdict()))
print("CPU ", (os.popen(
    '''grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage }' ''').readline()))
