import PyPDF4

def add_margin(input_pdf, output_pdf, margin):
    # Open the PDF
    with open(input_pdf, 'rb') as file:
        reader = PyPDF4.PdfFileReader(file)
        writer = PyPDF4.PdfFileWriter()

        # Iterate through each page
        for page_num in range(reader.numPages):
            page = reader.getPage(page_num)
            media_box = page.mediaBox
            media_box.upperRight = (
                media_box.getUpperRight_x() - margin,
                media_box.getUpperRight_y() - margin
            )
            media_box.lowerLeft = (
                media_box.getLowerLeft_x() + margin,
                media_box.getLowerLeft_y() + margin
            )
            writer.addPage(page)

        # Write the modified PDF to a new file
        with open(output_pdf, 'wb') as output_file:
            writer.write(output_file)

# Usage example
add_margin('Hangooksa_06_origin.pdf', 'Hangooksa_06_with_margin.pdf', 50)  # Adjust 50 to the desired margin size
