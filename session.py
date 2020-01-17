import requests


def get_session():
    jar = requests.cookies.RequestsCookieJar()
    session = requests.Session()

    jar.set('LWSSO_COOKIE_KEY', '123e1ehdiwgdhai23t4823r2tvds')

    post_args = {
        'cookies': jar
    }
    ses = session.get(
        'https://jsonplaceholder.typicode.com/todos', **post_args)
    print(ses.cookies.get_dict())
    return ses


if __name__ == '__main__':
    get_session()
