pattern = "^" + start_primer + "([A-Z]+)" + end_primer + "$" # start primer and end primer are sequences you are looking to match
regex = re.match(pattern, sequence) # sequence is the DNA sequence you are analyzing
print regex.group(1) # prints the sequence between the start and end primers