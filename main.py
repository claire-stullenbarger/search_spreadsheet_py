import openpyxl


def search_user(filename, search_term):
    wb = openpyxl.load_workbook(filename)

    sheet = wb.active

    for row in sheet.iter_rows(values_only=True):
        #this code uses the second colum as a search term and retrieves info in the first colum. Modify as needed
        user_id, user_info = row[0], row[1]

        if search_term.lower() in str(user_info).lower():
            return user_id

    return None

#replace below with the path to your file. Make sure it is in the same directory as your code
filename = 'C:/Users/put/path/here'
#replace below with your search term
search_term = 'term'

result = search_user(filename, search_term)

if result:
    print(f"User ID found: {result}")
else:
    print("User not found.")

