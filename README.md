# screenshot-script
---
## Description

This script creates 3 screenshots from every 1/4 of the file (e.g. if file's length is 100 seconds, it creates screenshot at 25th, 50th and 75th second). It is set up to only work with ```.mkv``` files but you can easily edit the source to support others.

## Dependencies

- ```ffmpeg```
- ```ffprobe``` (which should be included in ```ffmpeg```)
- Python 2.7.13 or higher

## Usage

```
$ git clone https://github.com/effektsvk/screenshot-script
$ cd screenshot-script
$ chmod +x screenshotScript.py
$ ./screenshotScript.py
```

Then you insert your source folder and your screenshot output folder. That's it.

## TODO

- Implementation of arguments (-i for input, -o for output, maybe some new ones)
- Nicer folder creation
- Ability to easily use the script with one file only

## Issues

I haven't found any issues with this script yet.
