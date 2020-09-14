from email_extraction.DocumentContainingEmails import DocumentContainingEmails

if __name__ == "__main__":
    doc = DocumentContainingEmails("../res/sample.txt")
    entry_count_min = input("Display email domains that occur more than this number of times: ")
    doc.rank_and_remove(entry_count_min)
    print(doc.email_dictionary)
