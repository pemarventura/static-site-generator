import os
from markdown_blocks import markdown_to_html_node, extract_title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page {from_path} to {dest_path} using {template_path}")

    with open(from_path) as f:
        from_md = f.read()
    
    with open(template_path) as f:
        template_html = f.read()

    from_html_string = markdown_to_html_node(from_md).to_html()

    template_html = template_html.replace("{{ Title }}", extract_title(from_md))
    template_html = template_html.replace("{{ Content }}", from_html_string)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    filename = os.path.basename(from_path)
    name, _ = os.path.splitext(filename)
    output_filename = name + ".html"

    with open(os.path.join(os.path.dirname(dest_path), output_filename), "w") as f:
        f.write(template_html)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):

    contents = os.listdir(dir_path_content)

    for content in contents:

        from_content_path = os.path.join(dir_path_content, content)

        if os.path.isfile(from_content_path):
            generate_page(from_path=from_content_path, template_path=template_path, dest_path=os.path.join(dest_dir_path, content))
            continue
        
        generate_pages_recursive(from_content_path, template_path, os.path.join(dest_dir_path, content))


