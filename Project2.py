

def main():
    cfg_dict = {}
    V = []
    check_list = []
    with open("Example.txt", "r") as file:
        for line in file:
            Variables = line.strip().split("-")
            Rules = Variables[1]
            for char in Rules:
                if char not in check_list and char.islower():
                    check_list.append(char)
            if Rules[0] == Rules[-1] and Rules[0] == "0":  # this if statement takes care of step 1
                V.append(Variables[0])  # of removing empty rules
                continue
            cfg_dict[Variables[0]] = Rules

    print("CFG after removing  -> empty")
    for variable, rule in cfg_dict.items():
        print(variable + " -> ", rule)

    print(V)
    print(check_list)

    cfg_dict = elim_e_rules(cfg_dict, V)
    elim_useless_rules(cfg_dict, check_list)


def elim_e_rules(cfg, V):

    # if V is not empty then remove any letters in our rules that are in V
    if V:
        for variable, rule in cfg.items():
            for letter in V:
                if letter in rule:
                    new_rule = rule.replace(letter, "")
                    cfg[variable] = new_rule

    # this for loop removes 0 from our rules then adds that variable to V
    for variable, rule in cfg.items():
        if "|0" in rule:
            new_rule = rule.replace("|0", "")
            cfg[variable] = new_rule
            V.append(variable)
        elif "0|" in rule:
            new_rule = rule.replace("0|", "")
            cfg[variable] = new_rule
            V.append(variable)

    # this for loop creates all possible combinations of the rules using the symbols in V
    # could be an easier/more efficient way to do this?
    for variable, rule in cfg.items():
        list_of_rules = rule.split("|")
        for item in list_of_rules:
            for letter in V:
                if letter in item:
                    new_rule = item.replace(letter, "")
                    if new_rule != "" and new_rule not in list_of_rules:
                        list_of_rules.append(new_rule)
        cfg[variable] = list_of_rules

    print("After further removing empty rules:")
    for variable, rule in cfg.items():
        print(variable + " -> ", end="")
        for item in rule:
            if rule[-1] == item:
                print(item)
                continue
            print(item + "|", end="")


    return cfg

def elim_useless_rules(cfg, check_list):
    x = []
    check = False
    to_be_removed = []

    for variable, rules_list in cfg.items():
        for rule in rules_list:
            for character in rule:
                if character not in check_list:
                    check = False
                    break
                check = True
            if check:
                x.append(variable)
                check_list.append(variable)
                break

    print(x)
    print(check_list)

    for variable in cfg.keys():
        if variable not in x:
            to_be_removed.append(variable)

    for item in to_be_removed:
        cfg.pop(item)

    print("After further removing useless rules:")
    for variable, rule in cfg.items():
        print(variable + " -> ", end="")
        for item in rule:
            if rule[-1] == item:
                print(item)
                continue
            print(item + "|", end="")






main()
