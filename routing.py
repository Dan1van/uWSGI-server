from yaml import load, FullLoader

url_dict = load(open('urls.yaml'), Loader=FullLoader)


def making_tuple_headers(url_to_transform):
    for header in url_to_transform['headers']:
        i = url_to_transform['headers'].index(header)
        url_to_transform['headers'][i] = tuple(header)

    return url_to_transform


def route(url, url_dict=url_dict):
    url_to_return = url_dict.get(url)

    if url_to_return is None:
        return making_tuple_headers(url_dict['404_error_page'])
    else:
        url_to_return = making_tuple_headers(url_to_return)

    return url_to_return
