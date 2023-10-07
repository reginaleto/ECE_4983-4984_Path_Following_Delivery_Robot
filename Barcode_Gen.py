import pyzbar
from barcode import EAN13
from barcode.writer import ImageWriter

def Main(self):
    # Barcode with ID Number associated with turning left
    turn_left = '' # ID number must be 12 digits
    barcode_left = EAN13(turn_left, writer=ImageWriter()) # generates barcode with specific ID number and converts to PNG


if __name__ == '__main__':
    Main()