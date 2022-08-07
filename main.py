#AWS DynamoDB RCUs Calculation (for both Reads & Writes)

import math

#Calculating RCUs: Strongly consistent reads

scr = int(input("Enter the strongly consistent read: "))
size_per_item = int(input("Enter the size of item/data: "))

if size_per_item % 4 != 0: 
    size_per_item = 4 * (size_per_item//4 +1)

rcu = scr * size_per_item / 4

print(f"RCU: {rcu}")

#Calculating RCUs: Eventually consistent reads

ecr = int(input("Enter the eventually consistent read: "))
size_per_item = int(input("Enter the size of item/data: "))

if size_per_item % 4 != 0:
    size_per_item = 4 * (size_per_item//4 +1)

rcu = ecr * size_per_item / 4 / 2

if rcu == float(rcu):
    rcu = math.ceil(rcu)

print(f"RCU: {rcu}")

#Calculating WCUs: Standard writes

sr = int(input("Enter the standard write: "))
size_per_item = float(input("Enter the size of item/data: "))

if size_per_item == float(size_per_item):
    size_per_item = math.ceil(size_per_item)

wcu = sr * size_per_item

print(f"WCU: {wcu}")

#Calculating WCUs: Transactional writes

tr = int(input("Enter the transactional write: "))
size_per_item = float(input("Enter the size of item/data: "))

if size_per_item == float(size_per_item):
    size_per_item = math.ceil(size_per_item)

wcu = tr * size_per_item * 2

print(f"WCU: {wcu}")

