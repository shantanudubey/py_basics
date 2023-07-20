# Helper file for functions


def displayModuleName():
    print("Module Name :", __name__)

def show():
    print("Pizza is a pie chart of how much pizza is left.")

def display():
    print("Internet connects people at a long distance.")
    print("Internet disconnects people at a short distance.")

def main():
    print("Executing main() ...")
    print("If you break your own record, you win as well as lose.")
    display()


# Executes only if this is run as an independent program
if __name__ == "__main__":
    print('-'*79)
    main()
    print('-'*79)


