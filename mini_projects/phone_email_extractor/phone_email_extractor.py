#!/usr/bin/python
import re

# phone_pattern = re.compile(r'\(?\d{3}\)?[.*-]\d{3}[.*-]\d{4}')
phone_pattern = re.compile(r'(?:\d{3}|\(\d{3}\))[.*-]\d{3}[.*-]\d{4}')

email_pattern = re.compile(r'''
    [a-z0-9._+-]+
    @
    [a-z0-9.-]+
    (?:\.[a-z]{2,4})
    (?:\.[a-z]{2,4})?
''', re.VERBOSE | re.I)


def get_phones(file):
    with open(file, 'r') as file:
        phone_matches = phone_pattern.findall(file.read())
        return phone_matches


def get_emails(file):
    with open(file, 'r') as file:
        email_matches = email_pattern.findall(file.read())
        return email_matches


def main():
    for index, phone in enumerate(get_phones('phone_email_book'), start=1):
        print(f'Phone number {index}: {phone}')
    for index, email in enumerate(get_emails('phone_email_book'), start=1):
        print(f'Email address {index}: {email}')


if __name__ == '__main__':
    main()
