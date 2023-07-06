import argparse
import os
import subprocess

from thm_to_cover import thm_to_cover
from yt_thm_dl import yt_thm_dl


def parse_args():
    parser = argparse.ArgumentParser(
        prog='yt_thm_to_cover', description='Youtube thumbnail to cover')
    parser.add_argument('vid', type=str,
                        help='Video id of youtube video')
    parser.add_argument('-q', dest='quality', type=str, default='HD',
                        help='Quality of thumbnail')
    parser.add_argument('-c', '--clean', dest='clean', action='store_true',
                        help='Remove origin thumbnail file cover file')
    parser.add_argument('--ytdlp', dest='ytdlp', action='store_true',
                        help='Download mp3 file (yt-dlp binary required)')
    parser.add_argument('--ytdlp-path', dest='ytdlp_path', type=str, default='yt-dlp',
                        help='Location of the yt-dlp binary')
    return parser.parse_args()


def main():
    args = parse_args()
    
    yt_thm_dl(args.vid)
    thm_to_cover(f'{args.vid}.jpg')
    if args.clean:
        os.remove(f'{args.vid}.jpg')
        print(f'Thumbnail \"{args.vid}.jpg\" removed.')

    if not args.ytdlp:
        return 0
    # yt-dlp common command and argument 
    # Just for my convenience
    try:
        ytdlp_cmd = f'{args.ytdlp_path} '
        ytdlp_cmd += '-f bestaudio --extract-audio --audio-format mp3 --audio-quality 0 --add-metadata '
        ytdlp_cmd += f'-- \"{args.vid}\"'
        subprocess.call(ytdlp_cmd)
    except:
        print('[ERROR] yt-dlp is not install')
        exit(127)
    


if __name__ == '__main__':
    main()
