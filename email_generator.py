####################################################################################################################
# A simple python script that will generate email ids based on combination of name and date of birth (dob)
# various combinations are used and dob is split to include in combinations
# USECASE : social engineering, phishing attack or brute forcing. This script will generate ~220 id's
# Author : Shuvro Basu, 2023.
# WARNING : IT IS ILLEGAL TO TRY TO GAIN ACCESS TO AN EMAIL ID WHICH DOES NOT BELONG TO YOU. DO NOT USE THIS PROGRAM
#           FOR ANY ILLEGAL OR NON-ETHICAL PUPOSES UNLESS YOU HAVE EXPLICIT PERMISSION FROM THE OWNER OF THE EMAIL ID
# RELEASE : AS FREE CODE UNDER GPL.
# NOTE : In some cases the ANSI Color codes may not work on Windows. In that case replace the statements with normal print()
####################################################################################################################

#standard imports required
import re
import sys
import os
import csv

#Few text formatting functions:
def color_for_windows():
    if os.name == 'nt':  # Only if we are running on Windows
        from ctypes import windll
        k = windll.kernel32
        k.SetConsoleMode(k.GetStdHandle(-11), 7)

def print_highlight(text):
    """
    Print text in a highlighted format.
    """
    os.system("")
    print("\033[97m" + text + "\033[m")

def print_red(text):
    """
    Print text in red.
    """
    os.system("")
    print("\033[91m" + text + "\033[m")

def print_green(text):
    """
    Print text in green.
    """
    os.system("")
    print("\033[92m" + text + "\033[m")

def print_yellow(text):
    """
    Print text in yellow.
    """
    os.system("")
    print("\033[93m" + text + "\033[m")

def print_blue(text):
    """
    Print text in blue.
    """
    os.system("")
    print("\033[94m" + text + "\033[m")

def print_purple(text):
    """
    Print text in purple.
    """
    os.system("")
    print("\033[95m" + text + "\033[m")

def print_cyan(text):
    """
    Print text in cyan.
    """
    os.system("")
    print("\033[96m" + text + "\033[m")


#Clear screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

#Check if date is valid
def is_valid_date(dob):
    # Split date of birth into year, month, and day
    try:
        year, month, day = dob.split("-")
    except ValueError:
        print_red("[!!]-Invalid date.\nDate should be in YYYY-MM-DD format only including dashes.")
        return False

    try:
        year = int(year)
        month = int(month)
        day = int(day)

        # Check if year, month, and day are within valid ranges
        if (year < 1900 or year > 2100) or (month < 1 or month > 12) or (day < 1 or day > 31):
            print_red("[!!]-Invalid date.\nDate should be in YYYY-MM-DD format only including dashes.")
            return False
        else:
            return True
    except ValueError:
        return False

#Default email domains
email_domains = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "aol.com", "icloud.com"]

#Main code to generate email id's
def generate_email_ids(first_name, last_name, dob, custom_domains=None):

    # Add custom domains if provided by the user
    if custom_domains:
        email_domains.extend(custom_domains)

    email_ids = set()  # Using a set to ensure unique email IDs

    # Check if first_name is empty
    if not first_name:
        print_red("[!]-First name cannot be empty. Exiting program.")

    # Remove any special characters from first and last names
    first_name = re.sub(r'[^a-zA-Z0-9]', '', first_name)
    last_name = re.sub(r'[^a-zA-Z0-9]', '', last_name)

    # Validate date of birth
    if not is_valid_date(dob):
        print("Invalid date of birth. Please enter a valid date (yyyy-mm-dd).")
        return email_ids

    # Split date of birth into year, month, and day
    year, month, day = dob.split("-")

    # Generate combinations
    combinations = [
         f"{first_name[:3]}{last_name[:3]}{day}",
         f"{first_name[:3]}{last_name[:3]}{day}{month}",
         f"{first_name[:3]}{last_name[:3]}{month}",
         f"{first_name[:3]}{last_name[:3]}{month}{day}",
         f"{first_name[:3]}{last_name}",
         f"{first_name[:3]}{last_name}{year}",
         f"{first_name[:3]}{year}{last_name}",
         f"{first_name[:4]}{last_name[:4]}{day}",
         f"{first_name[:4]}{last_name[:4]}{month}",
         f"{first_name[:4]}{last_name}",
         f"{first_name[:4]}{last_name}{year}",
         f"{first_name[:4]}{year}{last_name}",
         f"{first_name}{last_name}{month}{day}",
         f"{first_name}{last_name}{year}",
         f"{first_name}{year}",
         f"{last_name[:3]}{first_name[:3]}{day}",
         f"{last_name[:3]}{first_name[:3]}{month}",
         f"{last_name[:3]}{first_name[:3]}{month}{day}",
         f"{last_name[:3]}{first_name}",
         f"{last_name[:3]}{first_name}{day}",
         f"{last_name[:3]}{first_name}{month}",
         f"{last_name[:3]}{first_name}{month}{day}",
         f"{last_name[:3]}{first_name}{year}",
         f"{last_name[:3]}{year}{first_name}",
         f"{last_name[:4]}{first_name}",
         f"{last_name[:4]}{first_name}{day}",
         f"{last_name[:4]}{first_name}{day}{month}",
         f"{last_name[:4]}{first_name}{month}",
         f"{last_name[:4]}{first_name}{month}{day}",
         f"{last_name[:4]}{first_name}{year}",
         f"{last_name[:4]}{year}{first_name}",
         f"{first_name}{last_name}",
         f"{first_name[:1]}.{last_name}",
         f"{last_name[:1]}.{first_name}",
         f"{first_name}.{last_name}",
         f"{last_name}.{first_name}",
         f"{first_name}.{last_name[:1]}",
    ]

    # Repeat the combinations for each domain
    for domain in email_domains:
        for _ in range(6):  # Repeat 6 times for each domain
            for combination in combinations:
                email_ids.add(f"{combination}@{domain}")

    # Iterate through combinations for each domain
    for domain in email_domains:
        for combination in combinations:
            email_ids.add(f"{combination}@{domain}")

    return email_ids
################ end of main code

iserror = False #variable to check if there was any error in writing files
#fix ansi color issue in Windows (may work or not!!!)
color_for_windows()

#Show small banner
clear_screen() #clear the console/screen
print_highlight("~"*120)
print_cyan("EMAIL ID GENERATOR v.1.0")
print_purple("(c) Shuvro Basu, 2023.")
print_red("[!!]-Remember email IDs are CASE SENSITIVE. So, make sure you use the correct case.")
print_highlight("_"*120)

# Input from the user
first_name = input("Enter your first name (blank to exit): ")

if len(first_name) == 0:
    print_red("[!]-First name is blank. Exiting..")
    sys.exit(1)

last_name = input("Enter your last name: ")
dob = input("Enter your date of birth (yyyy-mm-dd including the dashes/hyphens) : ")

if not is_valid_date(dob):
    print_red("[!]-Invalid date of birth. Exiting..")
    sys.exit(1)

custom_domains = []
while True:
    add_custom_domain = input("Do you want to add a custom email domain? (Y/N): ").lower()
    if add_custom_domain == 'n':
        break
    elif add_custom_domain == 'y':
        print_yellow("Default domains : [gmail.com, yahoo.com, hotmail.com, outlook.com, aol.com, icloud.com]")
        custom_domain = input("Enter the custom email domain (e.g., example.com): ")
        custom_domains.append(custom_domain)
    else:
        print_red("[!]-Invalid input. Please enter 'y' or 'n'.")


# ask user if they want to see email on screen
show = input("Show email ids on screen? (Y/N)? : ").strip().lower()

# # Generate and display email IDs
# email_ids = generate_email_ids(first_name, last_name, dob)

# Generate and display email IDs with custom domains
email_ids = generate_email_ids(first_name, last_name, dob, custom_domains)

#sort output ask user
sort = input("Do you want to sort the email ids (Y/N)? : ").strip().lower()

if sort == "yes" or sort == "y":
    sorted_email_ids = sorted(email_ids)

#work with the generated email ids
if email_ids:

    print_green(f"[+]Generated Email IDs (total {len(email_ids)} combinations):")
    #check for sorting before showing
    if sort == "yes" or sort == "y":
        for email_id in sorted_email_ids:
            #if user wanted to see, then show, else move on
            if show  == "yes" or show  == "y":
                print(email_id)
    else:
        for email_id in email_ids:
            # if user wanted to see, then show, else move on
            if show == "yes" or show == "y":
                print(email_id)

    # Ask if the user wants to save email IDs in a CSV file
    save_csv = input("Do you want to save these email IDs in a CSV file? (yes/no): ").strip().lower()
    if save_csv == "yes" or save_csv == "y":
        try:
            csv_filename = f"{first_name}_{last_name}_email_ids.csv"
            with open(csv_filename, mode='w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(["Email ID"])
                if sort == "yes" or sort == "y":
                    for email_id in sorted_email_ids:
                        csv_writer.writerow([email_id])
                else:
                    for email_id in email_ids:
                        csv_writer.writerow([email_id])

                print_yellow(f"[+]Email IDs saved in {csv_filename}.")

        except OSError as err: #generate an error if file cannot be written and make the ierror variable true
            iserror = True
            print_red("[!!]-Unable to write to file...\n[!!]Please check file/folder permissions or if file is open.\n" + str(err))
            sys.exit(1)

#Finishing message
if iserror:
    print_highlight("=" * 120)
    print_red("[!!]-Errors were detected. Fix and Rerun.")
    print_highlight("="*120)
    sys.exit(1)

else:
    print_highlight("=" * 120)
    print_green("[+]-Email id generation complete.")
    print_red("[!!]-WARNING !!! WARNING !!! WARNING !!! WARNING !!! WARNING !!!\n[!!]Use this information only for legitimate purposes. Author shall not be responsible for any illegal use.")
    print_highlight("="*120)
