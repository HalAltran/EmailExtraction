class DocumentContainingEmails:
    def __init__(self, file_path):
        with open(file_path) as file:
            self.content = file.read()
            self.email_dictionary = {}
            self.create_email_dictionary()

    def get_words(self):
        return self.content.split(" ")

    def get_email_addresses(self):
        list_of_words = self.get_words()
        email_addresses = []
        for word in list_of_words:
            if word.__contains__("@"):
                email_addresses.append(word)
        return email_addresses

    def get_softwire_email_address_count(self):
        email_addresses = self.get_email_addresses()
        count = 0
        for email_address in email_addresses:
            if email_address.endswith("@softwire.com"):
                count += 1
        return count

    def create_email_dictionary(self):
        list_of_words = self.get_words()
        for word in list_of_words:
            if word.__contains__("@"):
                count = 1
                email_suffix = word.split("@")[1]
                email_suffix = email_suffix.split(".")[0]
                if email_suffix in self.email_dictionary:
                    count = self.email_dictionary[email_suffix] + 1
                self.email_dictionary[email_suffix] = count

    def sort_by_entry_count(self):
        self.email_dictionary = {address: count for address, count in sorted(self.email_dictionary.items(), key=lambda
            item: item[1])}
