a = 44              # Valid
b = "aditya"        # Valid
aditya = 33         # Valid
_aditya = 34        # Valid

@aditya = 23534     # Invalid due to symbol
_@sfgsdf = 4364y    # Invalid due to symbol and invalid value

# example 

name = "Aditya"       # right
name123 = "Aditya"    # right
_aditya = 34          # right
aditya_name = "Adi"   # right

123name = "Adi"       # error due to starting with a number
aditya-name = "Adi"   # error due to symbol
@aditya = 33          # error due to symbol