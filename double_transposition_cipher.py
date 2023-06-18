def remove_duplicates(key):
    return "".join(sorted(set(key), key=key.index))

def display_matrix(message, key):
    matrix = [list(message[i:i+len(key)]) for i in range(0, len(message), len(key))]
    for row in matrix:
        print(" ".join(row))
    print("\n")

def transpose(message, key):
    while len(message) % len(key) != 0:
        message += "X"
    matrix = [list(message[i:i+len(key)]) for i in range(0, len(message), len(key))]
    key_order = sorted([(char, i) for i, char in enumerate(key)], key=lambda x: x[0])
    
    print("Sorted Key Order: ", "".join([char for char, _ in key_order]))
    
    transposed = [[row[i] for _, i in key_order] for row in matrix]
    for row in transposed:
        print(" ".join(row))
    print("\n")
    
    return "".join(["".join(row) for row in transposed])

def double_transposition():
    message = input("Enter the message to be encrypted: ")
    key1 = input("Enter the first key: ")
    key2 = input("Enter the second key: ")

    message = message.upper().replace(" ", "").replace(".", "")
    key1 = remove_duplicates(key1.upper())
    key2 = remove_duplicates(key2.upper())
    
    print("Original Message: ", message)
    print("Key for first encryption: ", key1)
    print("Matrix for first encryption: ")
    display_matrix(message, key1)
    first_transposition = transpose(message, key1)
    print("Message after first encryption: ", first_transposition)

    print("Key for second encryption: ", key2)
    print("Matrix for second encryption: ")
    display_matrix(first_transposition, key2)
    second_transposition = transpose(first_transposition, key2)
    print("Message after second encryption: ", second_transposition)

if __name__ == "__main__":
    double_transposition()


