input = open("cost.txt", "r")
output = open("01.txt", "w")

for line in input:
    datalist = line.strip().split("    ")
    country, price, province, nameType = datalist
    output.write(nameType + "\t" + price + "\n")

input.close()
output.close()