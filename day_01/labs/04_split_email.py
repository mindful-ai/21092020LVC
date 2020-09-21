# Input a valid email ID and display the user name and domain separatly

# Example:
# Input < ram@oracle.com
# Output:
# USER   -> ram
# DOMAIN -> oracle.com


# input

email = input("Enter an email ID: ")

# process

'''
domain = email.split('@')[1]
user   = email.split('@')[0]
'''

ind = email.find('@')



# output

print("DOMAIN: ", email[:ind])
print("USER  : ", email[ind + 1:])

