from module import myFunc

if __name__ == "__main__":
    # if this code is diorectly executed bhy running th efile its present it 
    print("We are directly running this code") 


# __name__’ evaluates to the name of the module 
# in python from where the program is
# ran.
# If the module is being run 
# directly from the command line, 
# the ‘ __name__’ is set to
# string “__main__”. Thus, 
# this behaviour is used to check whether 
# the module is run
# directly or imported to another file.