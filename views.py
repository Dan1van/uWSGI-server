import os


def path_to_html(url, full_path=False):
    if full_path:
        return url

    return os.path.join(os.getcwd(), url)


def generate_view(path):
    with open(path) as f:
        html = f.read()

    return bytes(str(html), encoding='utf8')


def return_view(url, full_path=False):
    return generate_view(path_to_html(url, full_path))
