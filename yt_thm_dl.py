import argparse
import shutil
from urllib.parse import parse_qs, urlparse

import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0'
}


def yt_thm_dl(vid: str, quality='HD'):
    """
    Youtube thumbnail downloader

    :param vid: Video id of youtube video
    :param quality: Quality of thumbnail
        HD     -> 1280x720 (default)
        SD     -> 640x480
        HQ     -> 480x360
        Player -> 480x360
        Start  -> 120x90
        Middle -> 120x90
        End    -> 120x90
    """
    q_dict = {
        'HD': 'maxresdefault',
        'SD': 'sddefault',
        'HQ': 'hqdefault',
        'Player': '0',
        'Start': '1',
        'Middle': '2',
        'End': '3'
    }
    url = f'https://img.youtube.com/vi/{vid}/{q_dict[quality]}.jpg'
    r = requests.get(url, headers=headers, stream=True)

    # Some video does NOT have HD thumbnail, using SD instead
    if r.status_code != 200:
        url_2 = f'https://img.youtube.com/vi/{vid}/{q_dict["SD"]}.jpg'
        r = requests.get(url_2, headers=headers, stream=True)
        print(f'VID=\"{vid}\" does NOT have HD quality, download SD quality.')

    if r.status_code == 200:
        r.raw.decode_content = True
        with open(f'{vid}.jpg', 'wb') as f:
            shutil.copyfileobj(r.raw, f)
        print(f'Thumbnail \"{vid}.jpg\" downloaded.')
    else:
        print(f'Can NOT download \"{vid}.jpg\".')


def get_yt_vid(url: str) -> (str | None):
    """
    Parse vid from any type of YouTube url

    :param url: YouTube video url
    :return: vid | None (when parse Fail)
    """
    p = urlparse(url)

    if p.hostname == 'youtu.be':
        return p.path[1:]
    elif p.hostname in ['www.youtube.com', 'music.youtube.com', 'youtube.com']:
        if p.path == '/watch':
            return parse_qs(p.query).get('v')[0]
        elif p.path[:3] == '/v/':
            return p.path[3:]
        elif p.path[:7] == '/embed/':
            return p.path[7:]
        elif p.path[:8] == '/shorts/':
            return p.path[8:]
        else:
            return None
    else:
        return None


def parse_args():
    parser = argparse.ArgumentParser(
        prog='yt_thm_dl', description='Youtube thumbnail downloader')
    parser.add_argument('vid', type=str,
                        help='Video id of youtube video')
    parser.add_argument('-q', dest='quality', type=str, default='HD',
                        help='Quality of thumbnail')
    return parser.parse_args()


def main():
    args = parse_args()
    vid = get_yt_vid(args.vid)
    if vid == None:
        vid = args.vid
    yt_thm_dl(vid, args.quality)


if __name__ == '__main__':
    main()
