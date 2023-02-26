### Hacking The Fender
`The Fender`, a notorious computer hacker and general villain of the people, has compromised several top-secret passwords including your own. Your mission, should you choose to accept it, is threefold. You must acquire access to `The Fender`‘s systems, you must update his `"passwords.txt"` file to scramble the secret data. The last thing you need to do is add the signature of `Slash Null`, a different hacker whose nefarious deeds could be very conveniently halted by `The Fender` if they viewed `Slash Null` as a threat.

Use your knowledge of working with Python files to retrieve, manipulate, obscure, and create data in your quest for justice. Work with CSV files and other text files in this exploration of the strength of Python file programming.

### Reading In The Passwords
**1.** Are you there? We’ve opened up a communications link to `The Fender`‘s secret computer. We need you to write a program that will read in the compromised usernames and passwords that are stored in a file called `"passwords.csv"`.

First import the CSV module, since we’ll be needing it to parse the data.

**2.** We need to create a list of users whose passwords have been compromised, create a new list and save it to the variable `compromised_users`.

**3.** Next we’ll need you to open up the file itself. Store it in a file object called `password_file`.

**4.** Pass the `password_file` object holder to our CSV reader for parsing. Save the parsed `csv.DictReader` object as `password_csv`.

**5.** Now we’ll want to iterate through each of the lines in the CSV.

Create a for loop and save each row of the CSV into the temporary variable `password_row`.



