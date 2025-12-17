#checking percentage of used disk
import shutil
BYTES_PER_GB = 1024**3
Total = shutil.disk_usage("/").total
Used = shutil.disk_usage("/").used
# print("Used:", (shutil.disk_usage("/")).used / BYTES_PER_GB)
# print("Free:", (shutil.disk_usage("/")).free / BYTES_PER_GB)

print(Total)
print(Used)

Percentage_use = (Used * 100) / Total

print(Percentage_use)
