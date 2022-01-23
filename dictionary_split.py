def split_dict(num, num_list):
    with open('output/dictionary_'+str(num)+'.txt', 'w', newline='') as f:
            f.write('\n'.join(num_list))
    
def run():
    
    with open("./input/dictionary.txt", "rt") as f:
        sol_raw = f.read().splitlines()
    
    sol = {}
    lengths = set()
    for word in sol_raw:
        lengths = lengths.union({len(word)})
        
    for num in lengths:
        sol[num] = list()
        
    for word in sol_raw:
        sol[len(word)].append(word)
        
    for num in sol:
        split_dict(num, sol[num])
        
    print (sol)

if __name__ == "__main__":
    run()
