from copyall import copy_all
from generate_page import generate_page_recursive


def main():
    copy_all()
    generate_page_recursive("content","template.html","public")

main()
