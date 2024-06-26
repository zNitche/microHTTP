## microHTTP

minimal async HTTP client for micropython

### Local installation (for development)
```
python3 -m build --sdist
pip3 install dist/microhttp-[version].tar.gz
```

#### Microcontroller installation
##### As git submodule

In order to use `microHTTP` in your project without keeping whole 
codebase in repo, package should be added as `git submodule`.

In your project root directory add `microHTTP` as git submodule.
```
git submodule add --name microHTTP -b production https://github.com/zNitche/microHTTP ./microHTTP
```

Flash microcontroller and you are good to go.

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
