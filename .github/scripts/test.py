import os

print("__file__ :\n",__file__)
print("os.path.abspath(__file__) :\n",os.path.abspath(__file__))
print("os.path.dirname(os.path.abspath(__file__)) :\n",os.path.dirname(os.path.abspath(__file__)))
dir_path = os.path.dirname(os.path.abspath(__file__))

print(f"dir_path : \n{dir_path}/../../conf")
