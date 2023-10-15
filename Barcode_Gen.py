import pyzbar
from barcode import EAN13
from barcode.writer import ImageWriter

def Main():
    # Barcode with ID Number associated with turning left
    barcode_id = '333333333333' # ID number must be 12 digits
    barcode = EAN13(barcode_id, writer=ImageWriter()) # generates barcode with specific ID number and converts to PNG
    barcode.save('/home/ginaleto/ECE_4983-4984_Path_Following_Delivery_Robot/Barcodes/Instruction3_Barcode_Test') # no need to specify file ending bc of above line

if __name__ == '__main__':
    Main()