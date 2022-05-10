from Database import Database

def main():
    d = Database()
    myList = d.check_important_dates()
    print(myList)

def do_nothing():
    print("hi")
if __name__ == "__main__":
    main()