# The data that we need to retrieve for the election results
# 1. The total number of votes cast
# 2. A complete list of condidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular votes


# Add dependencies.


import csv
import os



#Assign a variable for the file to load and the path.

file_to_load= os.path.join("resources","election_results.csv")

# Assign a variable to save the file to a path.

file_to_save= os.path.join("analysis","election_analysis.txt")

# 1. Create a variable for counting total number of votes and initialize to Zero.

total_votes = 0

# Create variable for candidate names.

candidate_options = []

# Create a dictionary for candidate votes and declare empty.


candidate_votes = {}

winning_candidate = ""

winning_count = 0

winning_percentage= 0



# open the election results and read the file

with open (file_to_load) as election_data:

# To do: read and analyze the data here.
   
    file_reader=csv.reader(election_data)

# Read the header row.

    headers=next(file_reader)


# Print each row in the CSV file.

    for row in file_reader:
    

    # 2. Add to total vote count(iterating through rows by + 1)

        total_votes += 1

    # Print the candidate name from each row

        candidate_name = row[2]

    # If candidate does not match aby existing candidate...

        if candidate_name not in candidate_options:


        # ...Then Add the candidate name to the candidate list.

            candidate_options.append(candidate_name)

            # Begin tracking candidate's vote count.

            candidate_votes[candidate_name] = 0 

            # Add vote to the candidates count.

        candidate_votes[candidate_name] += 1

    # Save the results to our text file.

with open (file_to_save,"w") as txt_file:

    # Print the final vote count to the terminal.

    election_results = (

        f"\nElection Results\n"

        f"-------------------------\n"

        f"Total Votes: {total_votes:,}\n"

        f"-------------------------\n")


    print(election_results, end="")

    # Save the final vote count to the text file.

    txt_file.write(election_results)


    # # Determine the percent of votes for each candidate by looping through the counts.
    # # 1. Iterate through the candidate list.

    for candidate_name in candidate_votes:


        # 2. Retrieve vote count of a candidate.

        votes = candidate_votes[candidate_name]

        # 3. Calculate the percentage of votes.

        vote_percentage = float(votes) / float(total_votes)*100


    # To do: print out each candidate's name, vote count, and percentage of

    # votes to the terminal.

        # print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        candidate_results= (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate, their voter count, and percentage to the terminal.

        print(candidate_results)

#  Save the candidate results to our text file.

        txt_file.write(candidate_results)


            
        if(votes > winning_count) and (vote_percentage > winning_percentage):

    

            # if true then set winning count= votes, and winning_percent = vote_percent.

            winning_count=votes

            winning_percentage = vote_percentage

            # set the winning_candidate equal to the candidates name.

            winning_candidate = candidate_name


    winning_candidate_summary = (

        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    print(winning_candidate_summary)   

    # Save the winning candidate's name to the text file.

    txt_file.write(winning_candidate_summary)








  












