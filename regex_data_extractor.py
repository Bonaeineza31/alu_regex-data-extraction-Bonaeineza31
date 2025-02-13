import re

def extract_emails(text):
    """
    This function extracts email addresses from the text.
    Example formats: user@example.com, firstname.lastname@company.co.uk
    """
    email_form = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(email_form, text)

def extract_phone_numbers(text):
    """
    This function extracts phone numbers from the text.
    Example formats: (123) 456-7890, 123-456-7890, 123.456.7890
    """
    phone_form = r'\(\d{3}\) \d{3}-\d{4}|\d{3}-\d{3}-\d{4}|\d{3}\.\d{3}\.\d{4}|\d{3} \d{3}-\d{4}'
    return re.findall(phone_form, text)

def extract_urls(text):
    """
    This function extracts URLs from the text.
    Example formats: https://example.com, http://sub.example.org/page
    """
    url_form = r'https?://[a-zA-Z0-9./-]+'
    return re.findall(url_form, text)

def extract_time(text):
    """
    This function extracts time values from the text.
    Example formats: 14:30 (24-hour format), 2:30 PM (12-hour format)
    """
    time_form = r'(?:1[0-9]|2[0-3]|0?[0-9]):[0-5][0-9](?:\s?(?:AM|PM))?'
    return re.findall(time_form, text)

def extract_creditcard(text):
    """
    This function extracts credit card numbers from the text.
    Example formats: 1234 5678 9012 3456, 1234-5678-9012-3456
    """
    creditcard_form = r'\d{4}[- ]\d{4}[- ]\d{4}[- ]\d{4}'
    return re.findall(creditcard_form, text)

def extract_currency(text):
    """
    This function extracts currency amounts from the text.
    Example formats: $19.99, $1,234.56
    """
    currency_form = r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?'
    return re.findall(currency_form, text)

# Sample text to test the functions
test_text = """
Contact us at user@example.com or firstname.lastname@company.co.uk.
For inquiries, call (123) 456-7890 or 123-456-7890 or 123.456.7890.
Visit our website at https://www.example.com or http://sub.example.org/page.
The price is $1,234.56 and on sale for $19.99!
Meeting times are 14:30 and 2:30 PM.
Credit card: 1234 5678 9012 3456 and 1234-5678-9012-3456
"""

# Running all functions and presenting the results
emails = extract_emails(test_text)
phone_numbers = extract_phone_numbers(test_text)
urls = extract_urls(test_text)
creditcards = extract_creditcard(test_text)
times = extract_time(test_text)
currencies = extract_currency(test_text)

# Display results in a clean, readable format
print("Hello Readers!!!! Here is my extraction results:\n")
print(f"Emails Found:\n- {', '.join(emails)}\n")
print(f"Phone Numbers Found:\n- {', '.join(phone_numbers)}\n")
print(f"URLs Found:\n- {', '.join(urls)}\n")
print(f"Credit Card Numbers Found:\n- {', '.join(creditcards)}\n")
print(f"Times Found:\n- {', '.join(times)}\n")
print(f"Currency Amounts Found:\n- {', '.join(currencies)}\n")




