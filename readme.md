# Introduction

This is the Week 11 RegEx + Input/Output Exercises for Production Engineering Fellows. Following the instructions in this document, solve the exercises and make a Pull Request with your solutions.

# Tasks

There are several tasks that you need to complete. For each task, there is an input file, an output file, and a Python script file all having the same name. For example, an input and output file with the name `email.csv` and an `email.py` script where you'll need to write the script.

**Note:** Please make sure to use Regular Expressions for any kind of string manipulation (search, replace, etc).

## Exercise 1: New Emails

_File: `emails.csv`_

Suddenly, MLH received a huge amount of funding and hired 100 employees at once. You can see the list of employees in [_/inputs/emails.csv_](./inputs/emails.csv). The problem is all of the MLH's employees have Gmail accounts. Nick Quinlin, the CTO at MLH, has made `@mlh.io` accounts for all the employees, but he needs your help to update the emails in the sheet. Using your technical skills, develop a Regular Express (RegEx) and write a Python script that updates all the Gmail accounts to `@mlh.io` email addresses and write these new emails to a new file. Some new hires gave invalid email addresses (e.g., user@gmailcom). You can ignore that and add them to the output file as it is.

For example:
`abhorrence@gmail.com` should be updated to `abhorrence@mlh.io.`


## Exercise 2: Longest Word

_File: `longest.txt`_

MLH found a new partner who is interested in sponsoring their Hackathons. MLH has written a proposal for them on how and where the sponsor's funding will be used. The sponsor wants the proposal to be straightforward. To solve this problem, MLH needs your help to look into the proposal, find the longest word, and make it bold for all occurances of words the same length (use Markdown formatting i.e. **Text**).


## Exercise 3: Filter Vowels

_File: `vowels.txt`_

MLH has a document from last year, and Jay Nappy, President of the MLH Fellowship, is interested to know the number of vowels in the document. To solve this problem, MLH needs your help to count all the vowels (letters “a,” “e”, “i”, “o”, and “u”) and append the total in the file name. The document contains only ASCII characters.

For example: If the document has a vowel total of 50, the output file should be named as `vowels-50.txt`.

## Exercise 4:  Split the files

_Folder: `split`_

MLH has some documentation, some of which is large (under 1MB). This makes an issue when someone with slow internet tries to open, send or download it. To solve this problem, MLH needs your help to look into the documents and split them into two files or more files if the file size is more than 500 bytes. You don’t necessarily need to break them into two equal sizes (e.g. 250 bytes each) but make sure that none of them is larger than 500 bytes.
The documents are text files, and there is no specific boundary where you have to split them. Splitting a paragraph or a sentence is acceptable, but please ensure you don’t split a word into two files.

For example:
If `meta.txt` has a file size of 600 bytes, split it into two parts, `meta-1.txt` and `meta-2.txt`, and save it in the `dist.`
The format is `[file-name]-1.txt` and `[file-name]-2.txt`.
