import urllib.request as urllib
import re


def get_web_content(url: str):
    content = ""
    try:
        web_page = urllib.urlopen(url)
        content = web_page.read()
    except:
        print("An error occurred reading the web page %s" % web_page)
    return str(content)


class DocumentContainingEmails:
    def __init__(self, file_path):
        self.email_dictionary = {}
        self.content = get_web_content(file_path)
        self.create_email_dictionary()

    def create_email_dictionary(self):
        list_of_emails = re.findall(r"\S+@\S+", self.content)
        for email in list_of_emails:
            email_suffix_list = re.findall(r"@\w+.", email)
            if len(email_suffix_list) > 0:
                count = 1
                email_suffix = email_suffix_list[0]
                if email_suffix in self.email_dictionary:
                    count = self.email_dictionary[email_suffix] + 1
                self.email_dictionary[email_suffix] = count

    def sort_by_entry_count(self):
        self.email_dictionary = {address: count for address, count in sorted(self.email_dictionary.items(), key=lambda
            item: item[1], reverse=True)}

    def rank_and_remove(self, no_fewer_than):
        self.sort_by_entry_count()
        self.email_dictionary = {key: val for key, val in self.email_dictionary.items() if val > int(no_fewer_than)}
