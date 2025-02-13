import os, shutil



def delete_public_directory(path):
    """ Deletes public directory recursively"""
    print("Deleting public directory...")
    if os.path.exists(path):
        shutil.rmtree(path)

def copy_files_recursively(source_path, dest_path):
    if not os.path.exists(dest_path):
        os.mkdir(dest_path)

    for filename in os.listdir(source_path):
        from_path = os.path.join(source_path, filename)
        to_path = os.path.join(dest_path, filename)
        print(f" * {from_path} -> {to_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_files_recursively(from_path, to_path)
    










