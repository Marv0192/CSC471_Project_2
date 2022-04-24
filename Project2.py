from itertools import combinations


def main():
    cfg_dict = {}
    V = []
    terminals = []
    with open("Test_1.txt", "r") as file:
        for line in file:
            Variables = line.strip().split("-")
            Rules = Variables[1].split("|")
            if Rules[0] == Rules[-1] and Rules[0] == "0":  # this if statement takes care of step 1
                V.append(Variables[0])                     # of removing empty rules
                continue
            cfg_dict[Variables[0]] = Rules

    print("Initial CFG")
    for variable, rule in cfg_dict.items():
        print(variable + " ->", end=" ")
        for item in rule:
            if item == rule[-1]:
                print(item, end=" ")
                continue
            print(item + "|", end="")
        print()
    print(V)

    elim_e_rules(cfg_dict, V)


def elim_e_rules(cfg, V):
    #this for loop removes 0 from our rules then adds that variable to V
    for variable, rule in cfg.items():
        for item in rule:
            if item == "0":
                rule.remove(item)
                V.append(variable)

    #this for loop creates all possible combinations of the rules using the symbols in V
    #could be an easier/more efficient way to do this?
    for rule in cfg.values():
        for item in rule:
            for letter in V:
                if letter in item:
                    new_rule = item.replace(letter, "")
                    if new_rule not in rule:
                        rule.append(new_rule)

    print("After removing empty rules:")
    for variable, rule in cfg.items():
        print(variable + " ->", end=" ")
        for item in rule:
            if item == rule[-1]:
                print(item, end=" ")
                continue
            print(item + "|", end="")
        print()
    print(V)


main()
