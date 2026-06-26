import csv
with open(r"C:\Users\AnudipCOA\Downloads\python file handling\file_handling\new1.csv","w",newline='') as file :
    writer=csv.write(file)
    writer.write(["ink,25"])
    writer.writerow(["ballpen",10])

     