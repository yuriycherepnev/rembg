# Rembg-disk

This is a short and improved version of the library:
https://github.com/danielgatis/rembg

which in turn works on the AI ​​model:
https://github.com/xuebinqin/U-2-Net

## Installation

```bash
git clone ...

cd rembg-disk

set the ip, protocol, host and port settings in the renbg/config.py

docker-compose up --build
```
## Test

```bash
curl -s -F file=@/path/to/input.jpg "http://localhost:7000/api/remove"  -o output.png
```