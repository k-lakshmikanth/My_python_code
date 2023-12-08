import os

print(__file__)
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
dir_path = os.path.dirname(os.path.abspath(__file__))

print(f"{dir_path}/../../conf")
