# task2.py
def write_and_append_to_file(file_name):
    user_input = input("Enter data to write to the file: ")
    
    # Write user input to the file
    with open(file_name, 'w') as file:
        file.write(user_input + '\n')
    
    # Append additional data
    additional_data = input("Enter additional data to append to the file: ")
    with open(file_name, 'a') as file:
        file.write(additional_data + '\n')
    
    # Read and display the final content of the file
    print("\nFinal content of the file:")
    with open(file_name, 'r') as file:
        for line in file:
            print(line.strip())

if __name__ == "__main__":
    write_and_append_to_file('output.txt')
