from parser import Parser, Category
from saving import Saving

def main():
    parser = Parser()
    category = Category("uslugi")
    announcementslist = parser.parse(category)
    parser.close()

if __name__ == "__main__":
    main()
