# Test file - NO IMPORTS NEEDED!
# Just write your code normally
# Errors will automatically trigger PHAA sound!

import sys
import winsound


def _phaa_excepthook(exc_type, exc_value, exc_traceback):
    winsound.Beep(1000, 1000)
    sys.__excepthook__(exc_type, exc_value, exc_traceback)


sys.excepthook = _phaa_excepthook

print("Starting test...")

# This will cause an error
result = 10 / 0  # Division by zero error
print(result)
