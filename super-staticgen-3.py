# Super Staticgen 3
# This isn't even my final form!
# Michael Rudden 2019

import os

if __name__ == "__main__":
    print("Compiling site from \"build_files\" into \"public\" folder")

    build_path = 'build_files/'
    
    for filename in os.listdir(build_path):
        print(filename)