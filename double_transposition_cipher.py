# Function to remove duplicates and spaces from keys
def remove_duplicates(key):
    result = []
    for char in key:
        if char not in result and char != ' ':
            result.append(char)
    return ''.join(result)

# Function to display encryption matrices for visual understanding
def display_matrix(message, key):
    # Break message into chunks of the size of the key
    matrix = [list(message[i:i+len(key)]) for i in range(0, len(message), len(key))]
    # Print each row of the matrix
    for row in matrix:
        print(" ".join(row))
    print("\n")

# Function to perform transposition encryption on the message
def transpose(message, key):
    # Append 'X's to the message until it is a multiple of key length
    while len(message) % len(key) != 0:
        message += "X"
    # Create a matrix similar to display_matrix function
    matrix = [list(message[i:i+len(key)]) for i in range(0, len(message), len(key))]
    # Sort the key and create an order of columns
    key_order = sorted([(char, i) for i, char in enumerate(key)], key=lambda x: x[0])
    
    print("Sorted Key Order: ", "".join([char for char, _ in key_order]))
    
    # Transpose the columns of the matrix based on sorted key order
    transposed = [[row[i] for _, i in key_order] for row in matrix]
    for row in transposed:
        print(" ".join(row))
    print("\n")
    
    # Combine the transposed message into a single string
    return "".join(["".join(row) for row in transposed])

# Main function to perform double transposition encryption
def double_transposition():
    # Input plaintext and two keys from the user
    message = input("Enter the message to be encrypted: ")
    key1 = input("Enter the first key: ")
    key2 = input("Enter the second key: ")

    # Preprocess the message and keys
    message = message.upper().replace(" ", "").replace(".", "")
    key1 = remove_duplicates(key1.upper())
    key2 = remove_duplicates(key2.upper())
    
    print("Original Message: ", message)
    print("Key for first encryption: ", key1)
    print("Matrix for first encryption: ")
    display_matrix(message, key1)
    # Perform the first transposition encryption
    first_transposition = transpose(message, key1)
    print("Message after first encryption: ", first_transposition)

    print("Key for second encryption: ", key2)
    print("Matrix for second encryption: ")
    display_matrix(first_transposition, key2)
    # Perform the second transposition encryption
    second_transposition = transpose(first_transposition, key2)
    print("Message after second encryption: ", second_transposition)

if __name__ == "__main__":
    # Start the double transposition encryption process
    double_transposition()