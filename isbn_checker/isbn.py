import requests

def get_book_details(isbn):
    url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        # Check if any books are found
        if "items" in data:
            book = data["items"][0]["volumeInfo"]
            
            # Extracting necessary details
            title = book.get("title", "N/A")
            authors = book.get("authors", ["N/A"])
            publisher = book.get("publisher", "N/A")
            published_date = book.get("publishedDate", "N/A")
            description = book.get("description", "N/A")

            book_details = {
                "Title": title,
                "Authors": ', '.join(authors),
                "Publisher": publisher,
                "Published Date": published_date
            }
            
            # Printing book details
            print(f"Title: {title}")
            print(f"Authors: {', '.join(authors)}")
            print(f"Publisher: {publisher}")
            print(f"Published Date: {published_date}")
            # print(f"Description: {description}")

            return book_details
        else:
            print("No book found with the given ISBN.")
    else:
        print("Failed to fetch data from Google Books API.")

# Replace with any ISBN number
isbn = "9781847941831"
get_book_details(isbn)
