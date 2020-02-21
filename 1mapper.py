input = open("wine-data.txt", "r")
output = open("01.txt", "w")

for line in input:
    datalist = line.strip().split("\t")
    
    sno, country , point, price, province = datalist
    
    if len(price)!=0 :
        if len(country)!=0 :
            output.write(country + "\t" + price + "\n")

input.close()
output.close()