import os

print("__file__ :\n",__file__)
print("\nos.path.abspath(__file__) :\n",os.path.abspath(__file__))
print("\nos.path.dirname(os.path.abspath(__file__)) :\n",os.path.dirname(os.path.abspath(__file__)))
dir_path = os.path.dirname(os.path.abspath(__file__))

print(f"\ndir_path : \n{dir_path}\n\nconf_path : \n{dir_path}/conf")
