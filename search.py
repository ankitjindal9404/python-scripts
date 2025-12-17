#searching and getting results from particular sites
import sys
import webbrowser

def google_search(query):
    search_query = f"{query} site:medium.com OR site:reddit.com OR site:quora.com"

    encoded_query = search_query.replace(" ", "+")

    url = f"https://www.google.com/search?q={encoded_query}"

    webbrowser.open(url)

if len(sys.argv) > 1:
    search_term = ' '.join(sys.argv[1:])
    google_search(search_term)
else:
    print("please provide search term")
