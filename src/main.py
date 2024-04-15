from subprocess import getoutput
import argparse, platform

###############################################
#                                             #
#   Us3r Unl0ck3d                             #
#   Author: battleoverflow                    #
#   GitHub: https://github.com/battleoverflow #
#                                             #
###############################################

parser = argparse.ArgumentParser()
parser.add_argument('-o', '--octal', type=int, default=777, required=False, help="Type your octal as an integer (Ex: 777)")
parser.add_argument('-f', '--file', default=False, required=False, help="Store the output in a file (Format: log_<OCTAL>.txt)", action="store_true")
parser.add_argument('-v', '--verbose', default=False, required=False, help="If outputting to a file, this flag will need to be triggered to also print to the console", action="store_true")
parser.add_argument('-c', '--color', default=False, required=False, help="Add some color! (True by default) | Linux Only", action="store_true")
parser.add_argument('-r', '--recursive', default=False, required=False, help="Recursively search the entire specified directory (May take a long time) | Windows Only", action="store_true")
args = parser.parse_args()

version = "0.2.11"

class Us3rUnl0ck3d:

    def author(self):
        print(f"""
        #################################################################
        #                                                               #
        #   Us3r Unl0ck3d                                               #
        #   Author: battleoverflow                                      #
        #   GitHub: https://github.com/battleoverflow                   #
        #   Repository: https://github.com/battleoverflow/us3r-unl0ck3d #
        #                                                               #
        #################################################################
        v{version}
        """)

    def main(self):

        def convert_permissions(oct):
            int_to_str_conversion = ""
            perm_values = [(4,"r"),(2,"w"),(1,"x")]
            
            for int_octal in [int(o) for o in str(oct)]:
                for x, str_octal in perm_values:
                    if int_octal >= x:
                        int_to_str_conversion += str_octal
                        int_octal -= x
                    else:
                        int_to_str_conversion += '-'
                    
            return int_to_str_conversion
        
        def color_scheme(r, g, b, text):
            if args.color and platform.system() != 'Windows':
                return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

        whoami = getoutput("whoami")
        whoami_win = getoutput("powershell -Command  (Get-WMIObject -ClassName Win32_ComputerSystem).Username")
        permissions = convert_permissions(args.octal)

        if args.color and platform.system() != 'Windows':
            print("[ {0}]  {1}   Entire Root System (Parameters: /*)"
                .format(color_scheme(0, 255, 0, "0"), color_scheme(0, 255, 0, "=>")))
            
            print("[ {0}]  {1}   Home Directory (Parameters: ~)"
                .format(color_scheme(0, 255, 0, "1"), color_scheme(0, 255, 0, "=>")))
            
            print("[ {0}]  {1}   Custom Directory (Ex: /etc)"
                .format(color_scheme(0, 255, 0, "2"), color_scheme(0, 255, 0, "=>")))
        elif platform.system() == 'Windows':
            print("[{0}]  {1}   Entire Root System (Parameters: C:\*)"
                .format("0", "=>"))
            
            print("[{0}]  {1}   Home Directory (Parameters: ~)"
                .format("1", "=>"))
            
            print("[{0}]  {1}   Custom Directory (Ex: \Program Files)"
                .format("2", "=>"))
        else:
            print("[{0}]  {1}   Entire Root System (Parameters: /*)"
                .format("0", "=>"))
            
            print("[{0}]  {1}   Home Directory (Parameters: ~)"
                .format("1", "=>"))
            
            print("[{0}]  {1}   Custom Directory (Ex: /etc)"
                .format("2", "=>"))

        option = input("Choose Option: ")

        if option == '0':
            if platform.system() == 'Windows':
                if args.recursive:
                    print("This might take awhile...")
                    access_granted = getoutput(f"powershell -Command Get-ChildItem -Recurse C:\* | powershell -Command Get-Acl C:\* | powershell -Command findstr '{whoami_win}'")
                else:
                    access_granted = getoutput(f"powershell -Command Get-ChildItem C:\* | powershell -Command Get-Acl C:\* | powershell -Command findstr '{whoami_win}'")
                
                print(f"\nSearching system for username: {whoami_win}")
            else:
                access_granted = getoutput(f"ls -la /* | grep '{whoami}' | grep '{permissions}'")
                
                print(f"\nSearching system for username: {whoami}")
                print(f"Permissions Set: {permissions}")
        elif option == '1':
            if platform.system() == 'Windows':
                if args.recursive:
                    print("This might take awhile...")
                    access_granted = getoutput(f"powershell -Command Get-ChildItem -Recurse ~ | powershell -Command Get-Acl ~ | powershell -Command findstr '{whoami_win}'")
                else:
                    access_granted = getoutput(f"powershell -Command Get-ChildItem ~ | powershell -Command Get-Acl ~ | powershell -Command findstr '{whoami_win}'")
                
                print(f"\nSearching system for username: {whoami_win}")
            else:
                access_granted = getoutput(f"ls -la ~ | grep '{whoami}' | grep '{permissions}'")
           
                print(f"\nSearching system for username: {whoami}")
                print(f"Permissions Set: {permissions}")
        elif option == '2':
            dir_name = input("Directory to search: ")

            if platform.system() == 'Windows':
                if args.recursive:
                    print("This might take awhile...")
                    access_granted = getoutput(f"powershell -Command Get-ChildItem -Recurse '{dir_name}' | powershell -Command Get-Acl '{dir_name}' | powershell -Command findstr '{whoami_win}'")
                else:
                    access_granted = getoutput(f"powershell -Command Get-ChildItem '{dir_name}' | powershell -Command Get-Acl '{dir_name}' | powershell -Command findstr '{whoami_win}'")
                
                print(f"\nSearching system for username: {whoami_win}")
            else:
                access_granted = getoutput(f"ls -la '{dir_name}' | grep '{whoami}' | grep '{permissions}'")
            
                print(f"\nSearching system for username: {whoami}")
                print(f"Permissions Set: {permissions}")
        else:
            if args.color and platform.system() != 'Windows':
                print("\n{0}\n".format(color_scheme(255, 0, 0, "Unable to search or access system")))
            else:
                print("\n{0}\n".format("Unable to search or access system"))
        
        try:
            if access_granted != None:

                if args.color and platform.system() != 'Windows':
                    print("\n=== {0} ===\n".format(color_scheme(0, 204, 0, "SEARCH INFO")))
                else:
                    print("\n=== {0} ===\n".format("SEARCH INFO"))
                
                if platform.system() == 'Windows':
                    print(f"The following files are accessible based the set parameters: {whoami_win}\n")
                else:
                    print(f"The following files are accessible based the set parameters: {permissions}\n")

                if args.file and args.verbose:
                    if platform.system() == 'Windows':
                        print("Path     Owner       Access")
                        print("-" * 50)
                        print(access_granted)
                    else:
                        print(access_granted)
                elif args.file and not args.verbose:
                    print("\nAll data is saved in the generated file")
                else:
                    if platform.system() == 'Windows':
                        print("Path     Owner               Access")
                        print("-" * 50)
                        print(access_granted)
                    else:
                        print(access_granted)

                if args.file:
                    if platform.system() == 'Windows':
                        with open(f'log_{whoami_win}.txt', 'w') as f:
                            f.write("Path     Owner       Access")
                            f.write("-" * 50)
                            f.write(access_granted)
                    else:
                        with open(f'log_{args.octal}.txt', 'w') as f:
                            f.write(access_granted)
            else:
                if args.color and platform.system() != 'Windows':
                    print("\n{0}\n".format(color_scheme(255, 0, 0, "No data was generated")))
                else:
                    print("No data was generated")
        except UnboundLocalError as e:
            if args.color and platform.system() != 'Windows':
                print("\n{0} {1}\n".format(color_scheme(255, 0, 0, "[ERROR] =>"), e))
            else:
                print("[ERROR] => {0}".format(e))
        

if __name__ == '__main__':
    U3 = Us3rUnl0ck3d()
    U3.author()
    U3.main()
