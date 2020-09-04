from routing import route
import views


def application(environ, start_response):

    url = environ.get('PATH_INFO')
    view_info = route(url)

    page_to_return = views.generate_view(view_info['path'])
    start_response(view_info['status'], view_info['headers'])
    return page_to_return
