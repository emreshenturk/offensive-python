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
print(sys.version)
```
output
```
3.13.3 (main, Jan  8 2026, 12:03:54) [GCC 14.2.0]
```
---
We can check the details in tuple format.
```python
print(sys.version_info)
```
output
```
sys.version_info(major=3, minor=13, micro=3, releaselevel='final', serial=0)
```
---
We can access these values by index or attribute.
```python
print(sys.version_info.major)
print(sys.version_info[0])
```
output
```
3
3
```
---
Maybe we want a version lower than 3.8.5 for our exploit to work.
```python
import sys

v = sys.version_info

if v.major == 3 and v.minor == 8 and v.micro < 5:
    print("Exploit can run")
else:
    print("Exploit can't run")
```
---
We can check which interpreter run out script.
```python
print(sys.executable)
```
output
```
/usr/bin/python3
```



