from Database import Database

def main():
    d = Database()
    myList = d.read_per_quotes()
    print(myList)

def do_nothing():
    print("hi")
if __name__ == "__main__":
    main()