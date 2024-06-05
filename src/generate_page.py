from markdown_blocks import markdown_to_html_node
import os


def generate_page(from_path: str, template_path: str, dest_path: str):
    with open(template_path) as t:
        template = t.read()
    with open(from_path) as m:
        markdown = m.read()
    content = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    print(content)
    template = template.replace("{{ Title }}", title).replace("{{ Content }}", content)
    paths = dest_path.split("/")
    path_actual = "./" + paths[0]
    if not os.path.exists(path_actual):
        os.mkdir(path_actual)

    for path in paths[1:-1]:
        path_actual += "/" + path
        if os.path.exists(path_actual):
            continue
        os.mkdir(path_actual)
    with open(dest_path, "w") as f:
        f.write(template)


def extract_title(markdown: str) -> str:
    for line in markdown.splitlines():
        if line.startswith("# "):
            return line[2:]
    raise "error doesn't have a title in the markdownn"

def generate_page_recursive(dir_path_content:str, template_path:str, dest_dir_path:str):
    if not os.path.exists(dir_path_content):
        return
    for item in os.listdir(dir_path_content):
        dir_path_content_now = dir_path_content+"/"+item
        dest_dir_path_now = dest_dir_path+'/'+item
        if os.path.isfile(dir_path_content_now):
            generate_page(dir_path_content_now,template_path,dest_dir_path_now.split(".")[0]+".html")
        else:
            generate_page_recursive(dir_path_content_now,template_path,dest_dir_path_now)
    