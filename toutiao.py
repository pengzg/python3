import requests
from urllib.parse import urlencode




def get_one_page(offset):
    params = {
        'offset':offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '1'
    }
    url = 'http://www.toutiao.com/search_content/?'+urlencode(params)
    try:
        response = requests.get(url)
        if response.status_code ==200:
            return response.json()
    except requests.ConnectionError:
        return 'Error'

def get_images(json):
    if json.get('data'):
        for item in json.get('data'):
            title = item.get('title')
            images = item.get('image_detail')
            for image in images:
                print(image)
                yield {
                    'image':image.get('url'),
                    'title': title
                }


def main(offset):
    json = get_one_page(offset)
    print(json)
    imgs = get_images(json)

    print(imgs)


main(1)