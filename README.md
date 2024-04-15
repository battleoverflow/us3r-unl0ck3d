# Us3r Unl0ck3d
Us3r Unl0ck3d is a permissions scanner built to scan most Linux and Windows environments and return all accessible files by the currently logged-in user.

## Usage
```bash
python3 src/main.py
```

### Options
```
-h, --help          |   Displays help menu
-o, --octal         |   Type your octal as an integer to search for specific permissions (Ex: 777)
-f, --file          |   Store the output in a file (Format: log_<OCTAL>.txt)
-v, --verbose       |   If outputting to a file, this flag will need to be triggered to also print to the console
-c, --color         |   Add some color! (Off by default) | Linux Only
-r, --recursive     |   Recursively search the entire specified directory (May take a long time) | Windows Only
```

## Example(s)

### Linux
Displays all options with the 555 octal signature and pushes the data out to a file while printing the results to the terminal
```bash
$ python3 src/main.py -o 555 -vf
```

Prints data to a file, but does not print anything to the terminal. Uses the default octal, 777
```bash
$ python3 src/main.py -f
```

### Windows
Searches the entire home directory of the logged-in user recursively
```powershell
> py src/main.py -r
```

Searches the root system (`C:\`), exporting all data to a file and displaying the output to the terminal recursively
```powershell
> py src/main.py -rfv
```

## Helpful Octal(s)
Here I've compiled a list of common octal(s) you may need to search for on a system:

733 - Finds every option available to the owner + all writable and executable options for the public and group sections

If you still need help creating an octal combination, you can use this tool: https://chmod-calculator.com/
