import os

def bad_function():
    password = "12345"  # Hardcoded password – Sonar should flag this
    print("Bad function:", password)
