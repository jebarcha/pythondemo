from PyPDF2 import PdfMerger, PdfReader, PdfWriter

# Combine 2 PDFs
# merger = PyPDF2.PdfMerger()
# file_names = ["file1.pdf", "file2.pdf"]

# for file_name in file_names:
#     merger.append(file_name)

# # Write out the combined PDF
# merger.write("combined.pdf")
# merger.close()


# example 2:
with open("file1.pdf", "rb") as file:
    reader = PdfReader(file)
    print(len(reader.pages))  # `numPages` is replaced with `len(reader.pages)`

    # Get the first page
    page = reader.pages[0]

    # Rotate the page
    page.rotate(90)

    # Create a PdfWriter object
    writer = PdfWriter()
    writer.add_page(page)

    # Write the rotated page to a new PDF
    with open("rotated.pdf", "wb") as output:
        writer.write(output)
