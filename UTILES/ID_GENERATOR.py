
# def create_ID():
#    if not books:
#       return "BK1001"

#    HIGHEST_ID = max(int (book["ID"][2:]) for book in books)
#    return f"BK{HIGHEST_ID + 1}"
def generate_book_id(records,prefix,start):
    if not records:
        return f"{prefix}{start:03d}"
    highest_id = max(int(record["ID"][len(prefix):]) for record in records)
    return f"{prefix}{highest_id + 1}"
