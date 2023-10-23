import pyzbar
from barcode import EAN13
from barcode.writer import ImageWriter

def Main():
    # Barcode with ID Number associated with turning left
    barcode_id = '666666666666666666' # ID number must be 12 digits
    barcode = EAN13(barcode_id, writer=ImageWriter()) # generates barcode with specific ID number and converts to PNG
    barcode.save('/Users/ginaleto/ECE_4983-4984_Path_Following_Delivery_Robot/Barcodes/Final_Barcodes/Instruction6_Loading_Station') # no need to specify file ending bc of above line

if __name__ == '__main__':
    Main()