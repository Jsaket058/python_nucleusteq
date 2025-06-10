# 4. Implement a script that appends user input to a file.

# script = input("Enter text: ")
# with open('file_handling/yo.txt', 'a') as f:
#     f.write( script + '\n')

def append_user_input(filename):
    try:
        with open(filename, 'a') as file:  
            print(f"Enter text to append to {filename} (blank line to finish):")
            while True:
                user_input = input()
                if not user_input:  
                    break
                file.write(user_input + '\n')  
        print("Content successfully appended.")
    except PermissionError:
        print(f"Error: No permission to write to {filename}")
    except Exception as e:
        print(f"Error: {str(e)}")

append_user_input('file_handling/yo.txt')