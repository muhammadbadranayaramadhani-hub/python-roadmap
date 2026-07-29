"""
================
OPERATOR IDENTITY
================
"""

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print (a is b)  # True, karena b adalah referensi ke a
print (a is c)  # False, karena c adalah objek baru dengan nilai yang sama
print (a == c)  # True, karena nilai dari a dan c sama