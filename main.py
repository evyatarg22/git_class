print("Git practice")
print("Yossi Balabuski")

print("Hello World")

def is_prime(x):
    if x<=2:
        return True
    for i in range(2 , x):
        if x%i == 0:
            return False
    return True

print(is_prime(997))