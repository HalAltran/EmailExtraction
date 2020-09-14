from email_extraction.DocumentContainingEmails import DocumentContainingEmails

if __name__ == "__main__":
    doc = DocumentContainingEmails("../res/sample.txt")
    doc.sort_by_entry_count()
    print(doc.email_dictionary)
