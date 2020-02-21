s = open("02.txt","r")
r = open("03.txt", "w")
count = 1
thisKey = ""
thisValue = 0.0

for line in s:
  data = line.strip().split('\t')
  country, amount = data

  if country != thisKey:
    if thisKey:
      # output the last key value pair result
      r.write(thisKey + '\t' + str(thisValue/count)+'\n')

    # start over when changing keys
    thisKey = country
    thisValue = 0.0
    count=1
  
  # apply the aggregation function
  thisValue += float(amount)
  count += 1

# output the final entry when done
r.write(thisKey + '\t' + str(thisValue/count)+'\n')

s.close()
r.close()
