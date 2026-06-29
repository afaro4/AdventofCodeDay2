# Reading the unusual data into a list of lists
with open('unusual_data.txt') as f:
    unusual_data = [ ]
    for line in f: # going report by report
        if line.strip(): # skipping any blank reports in the data
            unusual_data.append(list(map(int, line.split()))) # appending each report to ful list

# Checking each report safe or unsaf
num_safe_reports = 0 # initiating counter for number of safe reports
for report in unusual_data:
    for i in range(0, len(report)):
        if (i == len(report)-1): # if its at the last level then it is safe
            num_safe_reports += 1
        else: # if we are not at the last level of the report
            difference = report[i] - report[i+1]
            # check if numbers are increasing or decreasing
            if i == 0:
                if difference < 0:
                    direction = 1 # numbers increasing
                else:
                    direction = -1 # numbers decreasing
            else: # move to next report if the proceeding numbers are not following the same pattern
                if (direction == 1) & (difference > 0):
                    break
                if (direction == -1) & (difference < 0):
                    break

            # check if the differences are between 1 and 3
            if 0 < abs(difference) < 4: 
                continue
            else:
                break

# Printing answer
print("There are " + str(num_safe_reports) + " safe reports in the data.")