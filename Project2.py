
cfg_dict = {}
V = []

with open("Example.txt", "r") as file:
    for line in file:
        Variable = line.strip().split("-")
        Rule = Variable[1].split("|")
        if Rule[0] == Rule[-1] and Rule[0] == "0":  #this if statement takes care of step 1
            V.append(Variable[0])                   #of removing empty rules
            continue
        cfg_dict[Variable[0]] = Rule

for variable, rule in cfg_dict.items():
    print(variable + " ->", *rule)
print(V)
