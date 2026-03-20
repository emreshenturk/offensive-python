# sys

We can get and use arguments from the terminal.
```python
import sys

script_name = sys.argv[0]
first_number = sys.argv[1]
second_number = sys.argv[2]

print(int(first_number) + int(second_number))
```
bash
```bash
python3 file.py 10 15
```
output
```
25
```

---

We can catch this if an argument is missing.

```python
import sys

script_name = sys.argv[0]

if len(sys.argv) != 3:
    print(f"{script_name} needs 3 arguments.")
    sys.exit(1)

first_number = sys.argv[1]
second_number = sys.argv[2]

print(int(first_number) + int(second_number))
```
bash
```bash
python3 file.py 10
```
output
```
file.py needs 3 arguments.
```
---

We can print which platform we are on.

```python
import sys

print(sys.platform)
```
output
```
linux
```

| `sys.platform` output | Operating system |
| --- | --- |
| `win32` | Windows (32-bit and 64-bit) |
| `linux` | Linux (Kali, Ubuntu, Debian, etc.) |
| `darwin` | macOS |
| `android` | Android |
| `freebsd` | FreeBSD |
| `cygwin` | Windows / Cygwin |
| `aix` | AIX |
---
We can check the version.
```python
import sys

print(sys.version)
```
output
```
3.13.3 (main, Jan  8 2026, 12:03:54) [GCC 14.2.0]
```



