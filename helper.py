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
        """
        if ls[0-5] is Item No., etc., then store all of those into list
        """
        get_item(data, i)

        """
        Get catalog no + designation if designation exists
        """
        catalog_no(data, i)
        
    
        """
        if ls[0] is "Qty" and ls[1] is "List of Materials", run list_of_materials until Qty column is not zero
        """
        list_of_materials(data, i)


def list_of_materials(data, pointer):
    if "Catalog No" not in data[pointer] and "Qty" in data[pointer + 1] and "List of Materials" in data[pointer + 2]:
        temp_pt = pointer + 2
        qty = data[temp_pt + 1]
        while qty.isnumeric():
            qty = data[temp_pt + 1]
            material = data[temp_pt + 2]
            if material.isnumeric():
                material = ""
                print([qty, material])
                temp_pt += 1
                continue
            print([qty, material]) 
            temp_pt += 2

    elif "Catalog No" in data[pointer] and "Qty" in data[pointer + 1] and "List of Materials" in data[pointer + 2]:
        temp_pt = pointer + 2
        qty = data[temp_pt + 2]
        while qty.isnumeric():
            catalog = data[temp_pt + 1]
            qty = data[temp_pt + 2]
            if not qty.isnumeric():
                continue
            material = data[temp_pt + 3]
            print([catalog, qty, material])
            temp_pt += 3

def catalog_no(data, pointer):
    if data[pointer] == "Catalog No" and data[pointer + 2] == "Designation":
        catalog = data[pointer + 1]
        designation = data[pointer + 3]
        print([catalog, designation])
    elif data[pointer] == "Catalog No" and (data[pointer + 2] != "Designation" and data[pointer + 2] != 'List of Materials'):
        catalog = data[pointer + 1]
        print([catalog])


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
        
        if description:
            description_ls = [x.strip() for x in description.split(",")]
            print([qty, product, description_ls, unit_price, extended_quote])
        else:
            print([qty, product, description, unit_price, extended_quote])