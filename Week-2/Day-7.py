# File I/O
#  with open('log.txt','w') as f: f.write('hello')
#  Read: with open('log.txt','r') as f: print(f.read())
#  Append mode: open('log.txt','a')
#  f.readlines()
#  Save calculator history to file

# Character	Meaning
# 'r'	Open for reading (default)
# 'w'	Open for writing, truncating (overwriting) the file first
# 'rb' or 'wb'	Open in binary mode (read/write using byte data)

# with open('log.txt','w') as f:
#     f.write('hello\n')

# with open('log.txt','r') as f:
#     print(f.read()) 

# with open('log.txt','a') as f:
#     f.write('name: John Doe\n')
# with open('log.txt','r') as f:
#     lines = f.readlines()
#     for line in lines:
#         print(line.strip())

#  Save calculator history to file
import importlib
Day6 = importlib.import_module("Day-6")

def save_history(history, filename='calc_history.txt'):
    # with open(filename  ,'w') as f:
    with open(filename  ,'a') as f:
        for entry in history:
            f.write(entry + '\n') 
# Example usage
calculator = Day6.calculator
calculator()
save_history(Day6.History)  

# print the file contents
print("\n--- Calculation History ---")
with open('calc_history.txt', 'r') as f:
    print(f.read())

# calculator = Day6.calculator
# calculator()

# usefull cases for history 
# save_history  persist calculations
# load_history  remember previous sessions
# search        find a specific calculation
# len(history)  track usage stats