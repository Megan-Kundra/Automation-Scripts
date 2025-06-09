# import fitz  # PyMuPDF
# import re

# def extract_invoice_data(pdf_path):
#     doc = fitz.open(pdf_path)
#     full_text = ""
#     for page in doc:
#         full_text += page.get_text()

#     # Patterns to extract info
#     invoice_number = re.search(r"Invoice #:\s*(\S+)", full_text)
#     invoice_date = re.search(r"Date:\s*([\d-]+)", full_text)
#     due_date = re.search(r"Due Date:\s*([\d-]+)", full_text)
    
#     # Extract 'Billed To' section - assumes it's the text between 'Billed To:' and 'Vendor:'
#     billed_to_match = re.search(r"Billed To:\s*(.*?)\s*Vendor:", full_text, re.DOTALL)
#     billed_to = billed_to_match.group(1).strip() if billed_to_match else "Not found"

#     # Extract 'Vendor' section - assumes it's the text between 'Vendor:' and '----' line
#     vendor_match = re.search(r"Vendor:\s*(.*?)\s*-{5,}", full_text, re.DOTALL)
#     vendor = vendor_match.group(1).strip() if vendor_match else "Not found"

#     # Extract total amount due by looking for "Total Amount Due:" label and yen amount after it
#     total_amount_match = re.search(r"Total Amount Due:\s*¥?([\d,]+)", full_text)
#     total_amount = "¥" + total_amount_match.group(1) if total_amount_match else "Not found"

#     # Prepare extracted data dictionary
#     data = {
#         "Invoice Number": invoice_number.group(1) if invoice_number else "Not found",
#         "Invoice Date": invoice_date.group(1) if invoice_date else "Not found",
#         "Due Date": due_date.group(1) if due_date else "Not found",
#         "Billed To": billed_to,
#         "Vendor": vendor,
#         "Total Amount Due": total_amount
#     }

#     return data

# # Example usage:
# invoice_data = extract_invoice_data(r"C:\Users\Megan\Documents\Automation Projects\Invoice Parser\Invoice.pdf")  # Change to your actual file name
# for key, value in invoice_data.items():
#     print(f"{key}: {value}")








import fitz  # PyMuPDF
import re
import sys

def extract_invoice_data(pdf_path):
    try:
        doc = fitz.open(pdf_path)
    except Exception as e:
        print(f"Error opening file: {e}")
        return None

    full_text = ""
    for page in doc:
        full_text += page.get_text()

    # Patterns to extract info
    invoice_number = re.search(r"Invoice #:\s*(\S+)", full_text)
    invoice_date = re.search(r"Date:\s*([\d-]+)", full_text)
    due_date = re.search(r"Due Date:\s*([\d-]+)", full_text)
    
    # Extract 'Billed To' section - assumes it's the text between 'Billed To:' and 'Vendor:'
    billed_to_match = re.search(r"Billed To:\s*(.*?)\s*Vendor:", full_text, re.DOTALL)
    billed_to = billed_to_match.group(1).strip() if billed_to_match else "Not found"

    # Extract 'Vendor' section - assumes it's the text between 'Vendor:' and '----' line
    vendor_match = re.search(r"Vendor:\s*(.*?)\s*-{5,}", full_text, re.DOTALL)
    vendor = vendor_match.group(1).strip() if vendor_match else "Not found"

    # Extract total amount due by looking for "Total Amount Due:" label and yen amount after it
    total_amount_match = re.search(r"Total Amount Due:\s*¥?([\d,]+)", full_text)
    total_amount = "¥" + total_amount_match.group(1) if total_amount_match else "Not found"

    # Data dictionary
    data = {
        "Invoice Number": invoice_number.group(1) if invoice_number else "Not found",
        "Invoice Date": invoice_date.group(1) if invoice_date else "Not found",
        "Due Date": due_date.group(1) if due_date else "Not found",
        "Billed To": billed_to,
        "Vendor": vendor,
        "Total Amount Due": total_amount
    }

    return data

def main():
    while True:
        file_path = input("Enter PDF file path (or 'q' to quit): ").strip()
        if file_path.lower() == 'q':
            print("Exiting.")
            sys.exit()

        data = extract_invoice_data(file_path)
        if data:
            print("\nExtracted Invoice Data:")
            for key, value in data.items():
                print(f"{key}: {value}")
            break  # Exit after successful extraction
        else:
            print("Failed to extract data. Please check the file and try again.\n")

if __name__ == "__main__":
    main()

