# Rembg-disk

This is a short and improved version of the library:
https://github.com/danielgatis/rembg

which in turn works on top of the library:
https://github.com/xuebinqin/U-2-Net

## Installation

```bash
git clone ...

cd rembg-disk

docker-compose up

curl -s -F file=@/path/to/input.jpg "http://localhost:7000/api/remove"  -o output.png
```