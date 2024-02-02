# Hasret Kevser KARAGÖL
# https://en.wikipedia.org/wiki/Free-space_path_loss
# Boş Uzay Alan Kayıpları

import math

# Işık hızı
c = 299792458  # metre/saniye

# Frekans
f = 920000000  # Hz

# Mesafe
d = 15000  # metre

# FREE SPACE PATH LOSS
FSPL = 10 * math.log10(((4 * math.pi * d * f) / c) ** 2)  # dB

print("Free Space Path Loss (dB):", FSPL)
