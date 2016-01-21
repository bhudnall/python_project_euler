"""through_ten = {"1": 3,"2": 3,"3": 5,"4": 4,"5": 4,"6": 3,"7": 5,"8": 5,"9": 4,}
teens = {"11": 6,"12": 6,"13": 8,"14": 8,"15": 7,"16": 7,"17": 9,"18": 8,"19": 8,}
tens = {"20": 6,"30": 6,"40": 5,"50": 5,"60": 5,"70": 7,"80": 6,"90": 6}
hundred_and = {} ## value 10

ten = 3

thru_ten_sorted = sorted(through_ten.iteritems())
teens_sorted = sorted(teens.iteritems())
tens_sorted = sorted(tens.iteritems())

sum = 0
for key, value in sorted(through_ten.iteritems())[0:5]:
    sum += value

print sum

##sum = ten * 9
for key, value in thru_ten_sorted:
    print key
    ##sum += value

for key, value in teens_sorted:
    print key
    ##sum += value

for key, value in tens_sorted:
    print key
    ##sum += value

for ten_key, ten_val in tens_sorted:
    for key, value in thru_ten_sorted:
        print ten_key, key
        ##sum += ten_val + value

##print sum"""

## only need one dict

def convert(num):
    convert_dict = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
          10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen",
          17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty",
          60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety", 100: "hundred"}
    return convert_dict[num]


sum = 0
for i in range(1, 30 + 1):
    if i < 20:
        sum += len(convert(i))
    elif i < 100:
        print convert(i/10)
        ##sum += len(convert)


print "sum", sum


## remember to divide by 10, 100, and 1000
## get:
## come up with logic send josh pseudocode
