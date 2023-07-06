# yt-thm-to-cover

Youtube thumbnail to CD-like cover image converter

See [Examples](#examples)

## Usage

Download thumbnail and convert it to cover
```shell
python yttc.py video-id --clean
```
To download a mp3 file, add `--ytdlp` argument. (`yt-dlp` binary required) 

For more usage, type `-h` or  `--help` in argument.

If you just want to download thumbnail or convert to cover, both `yt_thm_dl.py` and `thm_to_cover.py` can be standalone executed.

```shell
python yt_thm_dl.py video-id
```

```shell
python thm_to_cover.py thm-filename
```

## Requirements
```shell
pip install -r requirments.txt
```
* [requests](https://github.com/psf/requests)
* [opencv-python](https://github.com/opencv/opencv-python)
* [optional] [yt-dlp](https://github.com/yt-dlp/yt-dlp)


## Examples
![example01](https://github.com/chu3an/yt-thm-to-cover/blob/main/images/example01.jpg?raw=true)
![example02](https://github.com/chu3an/yt-thm-to-cover/blob/main/images/example02.jpg?raw=true)
![example03](https://github.com/chu3an/yt-thm-to-cover/blob/main/images/example03.jpg?raw=true)
![example04](https://github.com/chu3an/yt-thm-to-cover/blob/main/images/example04.jpg?raw=true)


## License
This code is licensed under MIT license
