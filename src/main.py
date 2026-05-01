import os
import shutil
import sys

from copystatic import copy_files_recursive
from generate_page import generate_pages_recursive


dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"

def main():

    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"

    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    open(os.path.join(dir_path_public, ".nojekyll"), "w").close()

    generate_pages_recursive(dir_path_content, "./template.html", dir_path_public, basepath)


main()
