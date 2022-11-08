from datetime import datetime
import math


def check_prime(number):
    sqrt_number = math.sqrt(number)
    for i in range(2, int(sqrt_number) + 1):
        if (number / i).is_integer():
            return False
        return True


start = datetime.now()
print(f"check_prime(10,000,000) = {check_prime(10_000_000)}")
end = datetime.now()
print(end - start)
