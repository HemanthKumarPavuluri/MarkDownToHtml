
from generate_page import generate_page
from copystaticfile import delete_public_directory, copy_files_recursively

dir_path_static = "./static"
dir_path_public = "./public"


def main():
    
    delete_public_directory(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursively(dir_path_static, dir_path_public)
    generate_page("content/index.md", "template.html", "public/index.html")


if __name__ == '__main__':
    main()


