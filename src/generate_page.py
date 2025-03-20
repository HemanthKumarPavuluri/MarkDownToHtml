import os, shutil
from markdown_blocks import markdown_to_html_node

def generate_page(from_path, template_path, dest_path, base_path="/"):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    # read markdown content
    with open(from_path, "r", encoding="utf-8") as f:
        markdown_content = f.read()

    # read template content
    with open(template_path, "r", encoding="utf-8") as f:
        template_content = f.read()

    #convert markdown to html
    html_content = markdown_to_html_node(markdown_content).to_html()

    title = extract_title(markdown_content)

    final_html = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_content)
    final_html = final_html.replace('href="/', f'href="{base_path}')
    final_html = final_html.replace('src="/', f'src="{base_path}')


    final_html = final_html.replace('href="majesty"', 'href="./blog/majesty/"')


    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(final_html)



def extract_title(markdown):
    """
    Extracts the first H1 header from the markdown text.
    If no H1 header is found, raises an exception.
    """
    for line in markdown.split("\n"):
        if line.startswith("# "):  # Ensures it is an H1
            return line[2:].strip()  # Removes "# " and trims spaces
    raise ValueError("No H1 header found in markdown")


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, base_path="/"):
    dir_list = os.listdir(dir_path_content)

    for file in dir_list:
        from_path = os.path.join(dir_path_content, file)
        dest_path = os.path.join(dest_dir_path, file)

        if os.path.isdir(from_path):
            print(f"Processing directory: {from_path}")
            generate_pages_recursive(from_path, template_path, dest_path, base_path)

        elif from_path.endswith(".md"):
            os.makedirs(dest_dir_path, exist_ok=True)
            dest_file_path = dest_path.replace(".md", ".html")
            print(f"Generating page: {from_path} -> {dest_file_path}")
            generate_page(from_path, template_path, dest_file_path, base_path)





















