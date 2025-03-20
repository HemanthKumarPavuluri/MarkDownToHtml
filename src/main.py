
import sys
from generate_page import generate_pages_recursive
from copystaticfile import delete_public_directory, copy_files_recursively

dir_path_static = "./static"
dir_path_docs = "./docs" 


def main():

    base_path = sys.argv[1] if len(sys.argv) > 1 else "/"
    
    delete_public_directory(dir_path_docs)

    print("Copying static files to public directory...")
    copy_files_recursively(dir_path_static, dir_path_docs)
    generate_pages_recursive("content", "template.html", dir_path_docs, base_path)


if __name__ == '__main__':
    main()


