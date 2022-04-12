# Us3r Unl0ck3d
Us3r Unl0ck3d is a permissions scanner built to scan any Linux environment and return all accessible files by the currently logged-in user.

## Usage
```bash
$ python3 src/main.py
```

### Options
```bash
-h, --help      |   Displays help menu
-o, --octal     |   Type your octal as an integer to search for specific permissions (Ex: 777)
-f, --file      |   Store the output in a file (Format: log_<OCTAL>.txt)
-v, --verbose   |   If outputting to a file, this flag will need to be triggered to also print to the console
-c, --color     |   Add some color! (Off by default)
```

## Example(s)
Displays all options with the 555 octal signature and pushes the data out to a file while printing the results to the terminal
```bash
$ python3 src/main.py -o 555 -v -f
```

Prints data to a file, but does not print anything to the terminal. Uses the default octal, 777.
```bash
$ python3 src/main.py -f
```

## Helpful Octal(s)
Here I've compiled a list of common octals you need to search for on a system.

733 - Finds every option available to the owner + all writable and executable options for the public and group sections

If you still need help creating an octal combination, you can use this tool: https://chmod-calculator.com/