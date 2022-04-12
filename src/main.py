from subprocess import getoutput
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-o', '--octal', type=int, default=777, required=False, help="Type your octal as an integer (Ex: 777)")
parser.add_argument('-f', '--file', default=False, required=False, help="Store the output in a file (Format: log_<OCTAL>.txt)", action="store_true")
parser.add_argument('-v', '--verbose', default=False, required=False, help="If outputting to a file, this flag will need to be triggered to also print to the console", action="store_true")
parser.add_argument('-c', '--color', default=False, required=False, help="Add some color! (True by default)", action="store_true")
args = parser.parse_args()

class Us3rUnl0ck3d:

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
            if args.color:
                return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

        whoami = getoutput("whoami")
        permissions = convert_permissions(args.octal)

        if args.color:
            print("[ {0}]  {1}   Entire Root System (Parameters: /*)"
                .format(color_scheme(0, 255, 0, "0"), color_scheme(0, 255, 0, "=>")))
            
            print("[ {0}]  {1}   Home Directory (Parameters: ~)"
                .format(color_scheme(0, 255, 0, "1"), color_scheme(0, 255, 0, "=>")))
            
            print("[ {0}]  {1}   Custom Directory (Ex: /etc)"
                .format(color_scheme(0, 255, 0, "2"), color_scheme(0, 255, 0, "=>")))
        else:
            print("[{0}]  {1}   Entire Root System (Parameters: /*)"
                .format("0", "=>"))
            
            print("[{0}]  {1}   Home Directory (Parameters: ~)"
                .format("1", "=>"))
            
            print("[{0}]  {1}   Custom Directory (Ex: /etc)"
                .format("2", "=>"))

        option = input("Choose Option: ")

        if option == '0':
            access_granted = getoutput(f"ls -la /* | grep '{whoami}' | grep '{permissions}'")
            print(f"\nSearching system for username: {whoami}")
            print(f"Permissions Set: {permissions}")
        elif option == '1':
            access_granted = getoutput(f"ls -la ~ | grep '{whoami}' | grep '{permissions}'")
            print(f"\nSearching system for username: {whoami}")
            print(f"Permissions Set: {permissions}")
        elif option == '2':
            dir_name = input("Directory to search: ")
            access_granted = getoutput(f"ls -la {dir_name} | grep '{whoami}' | grep '{permissions}'")
            print(f"\nSearching system for username: {whoami}")
            print(f"Permissions Set: {permissions}")
        else:
            if args.color:
                print("\n{0}\n".format(color_scheme(255, 0, 0, "Unable to search or access system")))
            else:
                print("\n{0}\n".format("Unable to search or access system"))
        
        try:
            if access_granted != None:

                if args.color:
                    print("\n=== {0} ===\n".format(color_scheme(0, 204, 0, "SEARCH INFO")))
                else:
                    print("\n=== {0} ===\n".format("SEARCH INFO"))

                print(f"The following files are accessible based your set parameters: {permissions}\n")

                if args.file and args.verbose:
                    print(access_granted)
                elif args.file and not args.verbose:
                    print("\nAll data is saved in the generated file")
                else:
                    print(access_granted)

                if args.file:
                    with open(f'log_{args.octal}.txt', 'w') as f:
                        f.write(access_granted)
            else:
                if args.color:
                    print("\n{0}\n".format(color_scheme(255, 0, 0, "No data was generated")))
                else:
                    print("No data was generated")
        except UnboundLocalError as e:
            if args.color:
                print("\n{0} {1}\n".format(color_scheme(255, 0, 0, "[ERROR] =>"), e))
            else:
                print("[ERROR] => {0}".format(e))
        

if __name__ == '__main__':
    U3 = Us3rUnl0ck3d()
    U3.main()