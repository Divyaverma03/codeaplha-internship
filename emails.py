
import re
import os

# Step 1: Define input and output files
input_file = "emails.txt"
output_file = "extracted_emails.txt"

# Step 2: Check whether input file exists
if os.path.exists(input_file):

    # Step 3: Read the text file
    with open(input_file, "r") as file:
        text = file.read()

    # Step 4: Find all email addresses using Regular Expression
    emails = re.findall(
        r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
        text
    )

    # Step 5: Remove duplicate email addresses
    emails = list(set(emails))

    # Step 6: Save emails into another file
    with open(output_file, "w") as file:

        for email in sorted(emails):
            file.write(email + "\n")

    # Step 7: Display results
    print("================================")
    print("       EMAIL EXTRACTOR")
    print("================================")

    print("\nEmails found:")

    for email in sorted(emails):
        print(email)

    print("\nTotal emails found:", len(emails))
    print("Emails saved successfully!")

else:
    print("Error: emails.txt file not found!")
