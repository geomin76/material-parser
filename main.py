import textract

def parse_doc(filename):
    text = textract.process('sample.DOCX')
    ls = []
    for i in text.split(b'\n'):
        if i:
            ls.append(i.decode("utf-8").strip())
    
    return ls

def looper(data):
    for i in range(len(data) - 10):
        # print(data[i])

        """
        if ls[0-5] is Item No., etc., then store all of those into list
        """
        get_item(data, i)
        
    
        """
        if ls[0] is "Qty" and ls[1] is "List of Materials", run list_of_materials until Qty column is not zero
        """
        list_of_materials(data, i)


def list_of_materials(data, pointer):
    if "Catalog No" not in data[pointer] and "Qty" in data[pointer + 1] and "List of Materials" in data[pointer + 2]:
        print("two column list of materials")

    elif "Catalog No" in data[pointer] and "Qty" in data[pointer + 1] and "List of Materials" in data[pointer + 2]:
        print("three column list of materials")

def get_item(data, pointer):
    if ("Item No." in data[pointer] and "Qty" in data[pointer + 1] 
        and "Product" in data[pointer + 2] and "Description" in data[pointer + 3]
        and "Unit  Quote Price" in data[pointer + 4] and "Extended Quote" in data[pointer + 5]):


        qty = data[pointer + 6]
        product = data[pointer + 7]
        description = data[pointer + 8]
        if "$" in description:
            description = ""
            unit_price = data[pointer + 8]
            extended_quote = data[pointer + 9]
        else:
            unit_price = data[pointer + 9]
            extended_quote = data[pointer + 10]

        print([qty, product, description, unit_price, extended_quote])


if __name__ == "__main__":
    print("hello world\n")
    # parse_pdf('')
    parsed_data = parse_doc('')
    looper(parsed_data)