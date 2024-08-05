import csv
import sys

def main():
    # Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        sys.exit(1)

    # Read database file into a variable
    with open(sys.argv[1], newline='') as csvfile:
        reader = csv.reader(csvfile)
        database = list(reader)

    # Read DNA sequence file into a variable
    with open(sys.argv[2], 'r') as file:
        sequence = file.read()

    # Find longest match of each STR in DNA sequence
    STRs = database[0][1:]  # get the list of STRs
    longest_matches = [longest_match(sequence, STR) for STR in STRs]

    # Check database for matching profiles
    profiles = database[1:]
    for profile in profiles:
        # convert the profile STR counts to integers
        profile_STR_counts = list(map(int, profile[1:]))
        if longest_matches == profile_STR_counts:
            print(profile[0])  # print the name of the matching profile
            return
    print("No match")

def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):
        count = 0
        while True:
            start = i + count * subsequence_length
            end = start + subsequence_length
            if sequence[start:end] == subsequence:
                count += 1
            else:
                break
        longest_run = max(longest_run, count)
    return longest_run

if __name__ == "__main__":
    main()
