import glob

# Find all .txt files in the current directory
txt_files = glob.glob(r'C:\Users\jinda\Downloads\Devops\final_practicing\*.txt')
print(f"Text files: {txt_files}")
count = 0

for i in txt_files:
    count += 1
print(count)

with open("counting.txt", "w") as file:
    file.write(str(count))
