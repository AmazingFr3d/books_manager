import cv2
from pyzbar.pyzbar import decode
import time
import requests
import json


def scanner():
    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 660)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    while True:
        success, frame = cam.read()
        isbn = ""

        for code in decode(frame):
            isbn = code.data.decode('utf-8')
            print(isbn)
            time.sleep(2)
        if isbn != "":
            break

        cv2.imshow("ISBN Scanner", frame)
        cv2.waitKey(3)

    return isbn


def api_call(isbn):
    url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}"
    response = requests.get(url)

    result = json.loads(response.text)
    if result['totalItems'] >= 1:
        book = result['items'][0]
        # print(type(book))
        title = book['volumeInfo']['title']
        author = book['volumeInfo']['authors']
        pub_date = book['volumeInfo']['publishedDate']
        isbn_num = isbn

        print(f"\nTitle: {title}\n")
        print(f"Author: {author}\n")
        print(f"Publication Date: {pub_date}\n")
        print(f"ISBN Number: {isbn_num}")
    else:
        print(f"ISBN Number '{isbn}' is not valid")


api_call(scanner())
