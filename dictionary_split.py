def output_csv(ids):
    with open('output/output_url.csv', 'w', newline='') as csvfile:
        output = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in ids:
            output.writerow(row)
            print(row)
    
def run():
    
    with open("./input/dictionary.txt", "rt") as f:
        sol_raw = f.read().splitlines()
    
    sol = {}
    for word in sol_raw:
        len(word) == length

if __name__ == "__main__":
    run()
