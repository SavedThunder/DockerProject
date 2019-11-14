import os
import socket


def GetFiles(p):
    files = []
    for f in os.listdir(path):
        if f.endswith(".txt"):
            files.append(f)
    
    return files

def GetFilesWC(p, file_list):
    files_wc = []
    total_words = 0
    for f in file_list:
        command = "wc -w " + p + "/" + f
        out = os.popen(command).read()
        out = out.split()
        total_words += int(out[0])
        files_wc.append(int(out[0]))

    return files_wc, total_words

def GetMaxFile(p, file_list):
    max_file = ""
    max_wc = -1
    for f in files:
        command = "wc -w " + p + "/" + f
        out = os.popen(command).read()
        out = out.split()
        if(int(out[0]) > max_wc):
            max_file = f
            max_wc = int(out[0])
    
    return max_file

if __name__ == "__main__":
    path = "home/data"

    files = GetFiles(path)
    files_wc, total_words = GetFilesWC(path, files)
    max_file = GetMaxFile(path, files)
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    name = "Kyle O'Connor"


    # Appending to output file
    result_file = open("home/output/results.txt", "w+")
    count = 0
    for file in files:
        st = file + " wc: " + str(files_wc[count])
        result_file.write(st + "\n")
        count += 1

    result_file.write("Total # words: " + str(total_words) + "\n")
    result_file.write("Max WC File: " + max_file + "\n")
    result_file.write("IP Address: " + ip_address + "\n")
    result_file.write("My Name: " + name)
    result_file.close()
    result_file = open("home/output/results.txt", "r")
    print(result_file.read())