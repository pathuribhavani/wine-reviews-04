s = open("02.txt","r")
r = open("03.txt", "w")

thisKey = ""
thisValue = 0.0

for line in s:
  data = line.strip().split('\t')
  country, price = data

  if country != thisKey:
    if thisKey:
      # output the last key value pair result
      r.write(thisKey + '\t' + str(thisValue)+'\n')

    # start over when changing keys
    thisKey = country 
    thisValue = 0.0
  
  # apply the aggregation function
  thisValue += float(price)

# output the final entry when done
r.write(thisKey + '\t' + str(thisValue)+'\n')
s.close()
r.close()
