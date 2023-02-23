# Simple redirect check

## install
```bash
ln -s $PWD/redirect-trace.py /home/$USER/.local/bin/redirect-trace
```

## usage
```bash
redirect-trace http://httpstat.us/301 
```

```
http://httpstat.us/301 301
https://httpstat.us 200
---
```
---
```bash
redirect-trace http://httpstat.us/301 http://httpstat.us/302
```

```
http://httpstat.us/301 301
https://httpstat.us 200
---
http://httpstat.us/302 302
https://httpstat.us 200
---
```