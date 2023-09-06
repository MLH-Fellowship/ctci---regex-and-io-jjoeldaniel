# Write the solution for "New Emails".

import csv
import re
import os


def is_valid_email(s):
    reg = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"
    if re.match(reg, s):
        return True
    return False


def read_emails():
    with open("inputs/emails.csv", newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        emails = {}
        for row in reader:
            if is_valid_email(row[1]):
                emails[row[0]] = re.sub(r"(@.*)\.*$", "@mlh.io", row[1])
            else:
                emails[row[0]] = row[1]
        return emails


emails = read_emails()

file_path = "./outputs/emails.csv"
os.makedirs(os.path.dirname(file_path), exist_ok=True)

with open(file_path, "w") as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    for key, value in emails.items():
        writer.writerow([key, value])
