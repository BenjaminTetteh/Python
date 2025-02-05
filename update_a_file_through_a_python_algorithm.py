# You are required to regularly update a file that identifies the employees who can access restricted content. 
# The contents of the file are based on who is working with personal patient records. 
# Employees are restricted access based on their IP address. There is an allow list for IP addresses permitted to sign into the restricted subnetwork. 
# There's also a remove list that identifies which employees you must remove from this allow list.
# Your task is to create an algorithm that uses Python code to check whether the allow list contains any IP addresses identified on the remove list. 
# If so, you should remove those IP addresses from the file containing the allow list.


# Create a variable 'import file' and assign it to the name of the file.
import_file = "/users/tetteh/allow_list.txt"

# A list of IP addresses that are no longer allowed to access restricted information.
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

# Build 'with' statement to read in the initial contents of the file
with open(import_file, "r") as file:

    # Use '.read()' function to read the imported file and store it in a variable named 'ip_addresses'
    ip_addresses = file.read()

print(ip_addresses)

# Use '.split()' to convert 'ip_addresses' from a string to a list
ip_addresses = ip_addresses.split()

# Display 'ip_addresses'
print(ip_addresses)

# Build iterative statement
# Name loop variable 'element'
# Loop through 'remove_list'

for element in remove_list:
    # Create a conditional statement to evaluate if 'element' is in 'ip_addresses'
    if element in ip_addresses:
        # use the '.remove()' method to remove elements from 'ip_addresses'
        ip_addresses.remove(element)

# Display 'ip_addresses'
print(ip_addresses)

# Convert 'ip_addresses' back to a string so that it can be written to a file
ip_addresses = "\n".join(ip_addresses)

print(ip_addresses)

# Build 'with' statement to rewrite the original file
with open(import_file, "w") as file:

    # Rewrite the file, replacing its contents with 'ip_addresses'
    file.write(ip_addresses)

# End
