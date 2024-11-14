from barcode_scanner import BarcodeScanner

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

if __name__ == '__main__':
    main()