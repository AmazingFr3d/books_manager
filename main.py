from barcode_scanner import BarcodeScanner
from isbn_checker import IsbnChecker

def main():
    scanner = BarcodeScanner()

    try:
        # Start barcode scanning
        scanner.start_scanning()
    except KeyboardInterrupt:
        print("Scanner stopped manually.")
    finally:
        # Ensure resources are released
        scanner.stop_scanning()

# isbn_check = IsbnChecker()
# isbn_check("9781847941831")

# if __name__ == '__main__':
#     main()