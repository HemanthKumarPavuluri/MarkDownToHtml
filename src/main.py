
from generate_page import generate_pages_recursive
from copystaticfile import delete_public_directory, copy_files_recursively

dir_path_static = "./static"
dir_path_public = "./public"


def main():
    
    delete_public_directory(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursively(dir_path_static, dir_path_public)
    generate_pages_recursive("content", "template.html", "public")


if __name__ == '__main__':
    main()


