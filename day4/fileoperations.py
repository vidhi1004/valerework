import csv
import json
#txt file read and write 
with open ("name.txt","w") as f:
    f.write("hello world")
    
with open("name.txt","r") as f:
    data = f.readline(5)
    print(data)
    
with open("name.txt","r") as f:
    data = f.read()
    print(data)
    
f = open("name.txt","r")
data = f.read()
print(data)


#csv file write  
with open ("practice.csv","w") as f:
    write= csv.writer(f)
    write.writerow(['Order,ID,Date,Customer Name,Product Name,Category,Quantity,Unit Price,Total Sales,Discount,Profit,Region'])
    data=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    write.writerows(data)
    
#writing file using dictwriter

with open("b.csv","w") as f :
    fieldnames=["name","age"]
    write=csv.DictWriter(f,fieldnames=fieldnames)
    write.writerow({"name":"vidhi","age":20})
    
#csv file read 
with open ("SalesData.csv","r") as f:
    data = csv.reader(f)
    for row in data:
        print(row[0]) 


with open ("SalesData.csv","r") as f:
    data = csv.reader(f)
    for row in data:
        print(row) 

#json file write 

mydict={
    "name":"xyz",
    "age":20,
    "number":23456786
}

data = json.dumps(mydict)
print(data)

# json file read
with open ("file.json","r") as f :
    data=json.load(f)
    
    print(data)

        
