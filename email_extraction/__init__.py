from email_extraction.DocumentContainingEmails import DocumentContainingEmails

if __name__ == "__main__":
    # web_url = "http://free-email-database.blogspot.com/2008/12/welcome-to-free-e-mail-database.html"
    web_url = input("Enter url of web page to extract emails from: ")
    doc = DocumentContainingEmails(web_url)
    entry_count_min = input("Display email domains that occur more than this number of times: ")
    doc.rank_and_remove(entry_count_min)
    print(doc.email_dictionary)
