#write functions here, don't add input('') statements here!
#Q4

def reverse_string(string1):
    rev_str = ""
    count = len(string1)

    while count > 0:
        rev_str += string1[count - 1]
        count = count -1
    return rev_str
