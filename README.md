# Tempmail Python Wrapper

## Introduction

The Tempmail Python Wrapper allows you to interact with the Temp-mail API to create disposable email addresses and retrieve messages sent to those addresses.

## Installation

```bash
git clone https://github.com/lutherantz/tempmail
```

## Usage

### Importing the Library

```python
from tempmail import Tempmail
```

### Initializing Tempmail

```python
temp = Tempmail()
```

### Creating a Disposable Email

To create a disposable email address, use the createMail method. This method returns both the email address and a token.

```python
email, token = temp.createMail()
print(f"Email: {email}")
```

### Retrieving Messages

To retrieve messages sent to a disposable email address, use the getMail method, passing the email address as an argument. This method returns a JSON response containing the messages.

```python
email = "example@temp-mail.org"  # Replace with your actual email
messages = temp.getMail(email)

for email_data in messages:
    print("-" * 20)
    print(f"Author: {email_data['from']}")
    print(f"To: {email_data['to']}")
    print(f"Subject: {email_data['subject']}")
    print(f"Content: {email_data['body_text']}")
    print("-" * 20)
```

### Example

Here's an example of how to use the Tempmail library:

```python
from tempmail import Tempmail

temp = Tempmail()
email, token = temp.createMail()
print(f"Email: {email}")

while True:
    try:
        messages = temp.getMail(email)
        for email_data in messages:
            print("-" * 20)
            print(f"Author: {email_data['from']}")
            print(f"To: {email_data['to']}")
            print(f"Subject: {email_data['subject']}")
            print(f"Content: {email_data['body_text']}")
            print("-" * 20)
        time.sleep(2)
    except Exception as e:
        print(f"An error occurred: {e}")
        continue
```
