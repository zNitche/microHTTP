## microHTTP

minimal async HTTP client for micropython

### Local installation (for development)
```
python3 -m build --sdist
pip3 install dist/microhttp-<VERSION>.tar.gz
```

#### Microcontroller installation
#### Get package from GitHub release

1. Get `.zip` package (replace `<VERSION>` with release number, for instance `v1.0.1`)
```
wget -O microHTTP.zip https://github.com/zNitche/microHTTP/releases/download/<VERSION>/microHTTP-<VERSION>.zip
```

2. Unpack archive and add its content to your project (don't forget to include it in `.gitignore`)
```
unzip microHTTP.zip
cp -r microHTTP <PROJECT_PATH>/microHTTP
```

3. Flash microcontroller and you are good to go.

##### As a MicroPython frozen module
See Micropython [docs](https://docs.micropython.org/en/latest/reference/manifest.html#manifest).

in short copy `microHTTP` package to `[micropython_src_dir]/ports/rp2/modules` and run
```
make -C ports/rp2 BOARD=RPI_PICO_W
```

### Development
packages in `requirements.txt` are used for development / build

```
pip3 install -r requirements.txt
```

#### Remote Shell
for flashing pico you can use `rshell`
```
pip3 install rshell==0.0.32
```

enter REPL
```
rshell 
repl
```

flash
```
rshell -f commands/flash
```

clear all files
```
rshell -f commands/wipe
```
