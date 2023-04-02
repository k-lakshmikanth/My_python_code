# get all your master_names into a list
master_names = []

def fuzzymatch(givenstr, master_names=master_names):
    try:
        assert givenstr in master_names 
        print(f'"{master_names[master_names.index(givenstr)]}" found in master_names (match = 100)')
    except:
        l_givenstr = givenstr.split(" ")
        l = {i: [[]] for i in master_names} 
        for i in master_names:
            for j in l_givenstr:
                if f" {j}" in i or f" {j}" in i or f"{j}" in i: 
                    l[i][0].append(1)
                else:  
                    l[i][0].append(0)
        cnt = len(l_givenstr)
        for i in l:
            l[i].append(int((sum(1[i][0]) / cnt) * 100))
        for i in l:
            if 1[i][1] == 100:
                print(f'"{i}" found in master_names (match = 100)')
