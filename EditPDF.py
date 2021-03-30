import PyPDF2
from pdf2image import convert_from_path
import os
import time
from PIL import Image
import pytesseract
from fpdf import FPDF


class Dir:
    png_dir = "images/"
    cropped_png_dir = "images/cropped/"
    address_page_dir = "address/"


start_time = time.time()


def convert_pfd_to_pngs(pdf):
    try:
        clear_folder(Dir.png_dir, '.png')
        pages = convert_from_path(pdf, 400, thread_count=4, paths_only=True, poppler_path='poppler-0.68.0/bin')
        counter = 1
        for page in pages:
            myfile = Dir.png_dir + 'output' + str(counter) + '.png'
            page.save(myfile, "PNG")
            print("Page " + str(counter) + " converted to PNG")
            counter += 1
        crop_pn_gs_to_addresses(pdf)
    except:
        print("convert_pfd_to_pngs failed")


def crop_pn_gs_to_addresses(pdf):
    try:
        clear_folder(Dir.cropped_png_dir, '.png')
        counter = 1
        print("\n")
        for file in os.listdir(Dir.png_dir):
            if file.endswith('.png'):
                im = Image.open(Dir.png_dir + file)
                im_crop = im.crop((305, 285, 3065, 850))
                im_crop.save(Dir.png_dir + "cropped/" + file, quality=100)
                print("Page " + str(counter) + " cropped")
                counter += 1
        get_text_from_cropped_png(pdf, counter)
        print("--- %s seconds ---" % (time.time() - start_time))
    except:
        print("crop_pn_gs_to_addresses failed")


def get_text_from_cropped_png(pdf, amount_of_pages):
    try:
        print("\n")
        clear_folder(Dir.address_page_dir, '.pdf')
        counter = 1
        pdf_writer = FPDF()
        for file in os.listdir(Dir.cropped_png_dir):
            if file.endswith('.png'):
                pytesseract.pytesseract.tesseract_cmd = r'Tesseract-OCR\tesseract.exe'
                customer_address = pytesseract.image_to_string(Image.open(Dir.cropped_png_dir + file))
                customer_address = os.linesep.join([s for s in customer_address.splitlines() if s])
                add_to_page(pdf_writer, customer_address, counter, amount_of_pages)
                counter += 1
        # add_to_pdf(pdf)
    except:
        print("get_text_from_cropped_png failed")


def add_to_page(pdf_writer, customer_address, counter, amount_of_pages):
    try:
        pdf_writer.add_page()
        pdf_writer.image(Dir.png_dir + "output" + str(counter) + ".png", 0, 0, w=210, h=297, type='PNG')
        pdf_writer.add_page()
        pdf_writer.set_font("Arial", size=12)
        pdf_writer.multi_cell(200, 10, txt=customer_address, align='L')
        print("Page " + str(counter) + " with address created")
        if counter == amount_of_pages - 1:
            pdf_writer.output(Dir.address_page_dir + "Addresses" + ".pdf")
            print("success")
    except:
        print("add_to_page failed")


def add_to_pdf(order_pdf):
    pdf_document = order_pdf
    pdf = PyPDF2.PdfFileReader(pdf_document)
    # Output files for new PDFs
    output_filename_odd = Dir.address_page_dir + "Addresses.pdf"
    pdf_writer_odd = PyPDF2.PdfFileWriter()
    # Get reach page and add it to corresponding
    # output file based on page number
    for page in range(pdf.getNumPages()):
        current_page = pdf.getPage(page)
        if page % 2 == 0:
            pdf_writer_odd.addPage(current_page)

    # Write the data to disk
    with open(output_filename_odd, "wb") as out:
        pdf_writer_odd.write(out)
        print("created", output_filename_odd)


def clear_folder(path, file_type):
    if not os.path.exists(path):
        os.makedirs(path)
    for file in os.listdir(path):
        if file.endswith(file_type):
            os.remove(path + file)
    print("Folder " + path + " cleared")
