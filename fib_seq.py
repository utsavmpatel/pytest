import numpy as np
from decimal import Decimal

last = 1
last_placeholder = last
second_last = 1

while True:
    last_placeholder = last + second_last
    second_last = last
    last = last_placeholder
    print(str(last)+"\r")
