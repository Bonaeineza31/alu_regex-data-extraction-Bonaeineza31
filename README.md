# The file name is called regex_data_extractor.py
I started by creating  a repository called alu_regex_data_extraction_ Bonaeineza31
Then initialized a Readme.md file as it would help me clone it in my jetbrain.Ide/pycharm
I did clone it, then created the file regex_data_extractor.py where i had to implement my codes
The features I wanted to display are as follow : Email address, URLs, Phonenumbers, Creditcards , Time and Currency Amount
I defined every feature through creating function for each. In these function i assigned them their regex and called them through what they have to return
for example def extract_currency(text):
    """
    This function extracts currency amounts from the text.
    Example formats: $19.99, $1,234.56
    """
    currency_form = r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?'
    return re.findall(currency_form, text)
    as you can see we defined the function then we aasigned currency_form to it's regex then later on called the function to print  the regex but in text form. 
    this was done for other features too.
    Aftr finishing it  we wrote a test_text which had this example as one of their lines 
    Meeting times are 14:30 and 2:30 PM. then the purpose of our it it;s that whatver we have we need to extract that time only 
    I then assigned name to function that would be printed i.e: times = extract_time(test_text)
    i would print them like print("0 Time:")
for time in times:
    print(f"  ○ {time}") to mean they would have to first print the word time then the under it wuld be nullet points of the extracted time
    this was done for all other features
After successfully implementing all the features, I committed and pushed my code to GitHub.
This ensures that my work is saved, version-controlled, and accessible for further improvements.

