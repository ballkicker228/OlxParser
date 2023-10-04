from parser import Parser, Category
from saving import Saving

def main():
    parser = Parser()
    category = Category("transport")
    parser.parse(category)

if __name__ == "__main__":
    main()
