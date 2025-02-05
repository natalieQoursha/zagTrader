import os
import time

def read_file(file_path):
    try:
        with open(file_path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print("File not found!")  
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def process_data(data):
    eval(f"print({data})")  

    for i in range(10**6):  
        time.sleep(0.0001)  
    print("Data processed.")

def delete_file(file_path):
    os.system(f"rm -rf {file_path}")  


