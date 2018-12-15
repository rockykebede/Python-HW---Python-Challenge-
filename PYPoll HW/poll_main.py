# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 21:18:49 2018

@author: Haile
"""

# Dependencies- modules to read csv and create file paths
import csv
import os

# Loading election data csv and path for the result file
csvpath_elec = os.path.join("Resources", "election_data.csv")
csvpath_elec_result_output = os.path.join("analysis", "election_result.txt")

# Total Votes
total_votes = 0

# Candidate Options and Vote Counters
candidate_list = []
candidate_vote_count = {}

# Winning Candidate and Winning Count Tracker
winner_candidate = ""
winner_vote_count = 0

# Read the csv and convert it into a list of dictionaries
with open(csvpath_elec) as election_data:
    reader = csv.reader(election_data)

    # defining the header
    header = next(reader)

    # For each row...
    for row in reader:

        # Run and print the loader animation
        print("- ", end=""),

        # Total vote count
        total_votes = total_votes + 1

        # Extract the candidate name from each row
        candidate_name = row[2]

        # If the candidatename is not in the candidate list, add it to the list
        # and count the votes for that candidate
        
        if candidate_name not in candidate_list:

            # Add it to the list of candidates in the running
            candidate_list.append(candidate_name)

            # And begin tracking that candidate's voter count
            candidate_vote_count[candidate_name] = 0

        # Then add a vote to that candidate's count
        candidate_vote_count[candidate_name] = candidate_vote_count[candidate_name] + 1

# Print the results and export the data to our text file
with open(csvpath_elec_result_output, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    print(election_results, end="")

    # Save the final vote count to the text file
    txt_file.write(election_results)

    # Determine the winner by looping through the counts
    for candidate in candidate_vote_count:

        # Retrieve vote count and percentage
        votes = candidate_vote_count.get(candidate)
        vote_per = float(votes) / float(total_votes) * 100

        # Determine winning vote count and candidate
        if (votes > winner_vote_count):
            winner_vote_count = votes
            winner_candidate = candidate

        # Print each candidate's voter count and percentage (to terminal)
        candidate_vote_sum = f"{candidate}: {vote_per:.3f}% ({votes})\n"
        print(candidate_vote_sum , end="")

        # Save each candidate's voter count and percentage to text file
        txt_file.write(candidate_vote_sum )

    # Print the winning candidate (to terminal)
    winner_candidate_sum = (
        f"-------------------------\n"
        f"Winner: {winner_candidate}\n"
        f"-------------------------\n")
    print(winner_candidate_sum)

    # Save the winning candidate's name to the text file
    txt_file.write(winner_candidate_sum)
