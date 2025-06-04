import csv
with open ("b.csv","w") as f:
    write=csv.writer(f)
    data=([1,2,3,4],[5,6,7,8])
    write.writerows(data)
    