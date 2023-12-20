import time
import socket
while true
text = """
__     ___    _  _____     _    _ _    _ ____  
\ \   / / |  | |/ ____|   | |  | | |  | |  _ \ 
 \ \_/ /| |__| | |  __    | |__| | :  | | |_) |
  \   / |  __  | | |_ |   |  __  | |  | |  _ < 
   | |  | |  | | |__| |   | |  | | |__| | |_) |
   |_|  |_|  |_|\_____|   |_|  |_|\____/|____/ 
"""

print(text)

startti = input("for testing, Welcome\n\n")

if startti.lower() == "tester":
    print("\n\nLoading")
    time.sleep(3)
    
    kysy = input("Open tester program? (y/n): ")

    if kysy.lower() == "y":
        def check_open_ports(target_host, target_ports):
            try:
                for port in target_ports:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(1)
                    result = sock.connect_ex((target_host, port))
                    if result == 0:
                        print(f"Port {port} is open")
                    else:
                        print(f"Port {port} is closed")

                    sock.close()

            except socket.error as e:
                print(f"Error: {e}")

        target_host = input("Enter the target host: ")
        target_ports = [int(port) for port in input("Enter the target ports (comma-separated): ").split(",")]

        check_open_ports(target_host, target_ports)




if startti.lower() == "passwd":
    print("\n\nLoading")
    time.sleep(3)
    
    kysy = input("Open passwd program? (y/n): ")

    if kysy.lower() == "y":
    	import re

def check_password_strength(password):
    # Minimum length check
    if len(password) < 8:
        return "Weak: Password should be at least 8 characters long."

    # Uppercase letter check
    if not any(char.isupper() for char in password):
        return "Weak: Password should contain at least one uppercase letter."

    # Lowercase letter check
    if not any(char.islower() for char in password):
        return "Weak: Password should contain at least one lowercase letter."

    # Number check
    if not any(char.isdigit() for char in password):
        return "Weak: Password should contain at least one number."

    # Special character check
    special_characters = re.compile("[@#$%^&+=]")
    if not special_characters.search(password):
        return "Weak: Password should contain at least one special character (@#$%^&+=)."

    return "Strong: Password meets the minimum requirements."

if __name__ == "__main__":
    user_password = input("Enter your password: ")
    result = check_password_strength(user_password)
    print(result)
      break
