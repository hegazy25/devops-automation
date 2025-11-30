#for loop 
servers = ["web01", "web02", "db01", "db02"]
for server in servers:
    print(server)

for i in range(5):
    print("Iteration:", i)

for i in range(1, 6):
    print("Iteration:", i)

for i in range(1, 13, 3):
    print("Iteration:", i)

#while loop
count = 0
while count < 5:
    print("Count:", count)
    count += 1