# Reading the unusual data into a list of lists
with open('unusual_data.txt') as f:
    unusual_data = [ ]
    for line in f: # going report by report
        if line.strip(): # skipping any blank reports in the data
            unusual_data.append(list(map(int, line.split()))) # appending each report to ful list