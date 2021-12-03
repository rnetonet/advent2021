data = list(map(int, open("input.txt", "r").read().splitlines()))

counter = 0

previous_measurement = data[counter]
next_measurement = data[counter + 1]

increases = 0
while counter < len(data) - 1:
    counter += 1
    next_measurement = data[counter]

    if previous_measurement < next_measurement:
        increases += 1
    
    previous_measurement = next_measurement

print(increases)