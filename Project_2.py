def read_file():
    cfg_dict = {}
    V = []
    check_list = []
    try:
        with open("Test_3.txt", "r") as file:
            for line in file:
                Variables = line.strip().split("-")
                Rules = Variables[1]
                for char in Rules:
                    if char not in check_list and char.islower():
                        check_list.append(char)
                # this if statement takes care of step 1 of removing empty rules
                if Rules[0] == Rules[-1] and Rules[0] == "0":
                    V.append(Variables[0])
                    continue
                cfg_dict[Variables[0]] = Rules
    finally:
        file.close()

    print("CFG after removing  -> empty")
    for variable, rule in cfg_dict.items():
        print(variable + " ->", rule)

    cfg_dict = elim_e_rule(cfg_dict, V)
    print()
    print("After eliminating empty rules")
    print_cfg(cfg_dict)

    cfg_dict = elim_useless_rules(cfg_dict, check_list)
    print()
    print("After eliminating useless rules")
    print_cfg(cfg_dict)


#method used to eliminate empty rules
def elim_e_rule(cfg, V):
    #eliminates all 0 from the cfg and adds that variable with 0 to V
    for variable, rule in cfg.items():
        if "|0" in rule:
            new_rule = rule.replace("|0", "")
            cfg[variable] = new_rule
            V.append(variable)
        elif "0|" in rule:
            new_rule = rule.replace("0|", "")
            cfg[variable] = new_rule
            V.append(variable)

    #checks if all the characters in a rule are in V, if so add variable to V
    for variable, rule in cfg.items():
        list_of_rules = rule.split("|")
        for item in list_of_rules:
            flag = False
            for character in item:
                if character in V:
                    flag = True
                    continue
                else:
                    flag = False
                    break
            if flag:
                V.append(variable)

    #recursive solution for finding all possible combinations using the items in V
    for nonterminal, rule in cfg.items():
        list_of_rules = rule.split("|")
        new_rules = []
        for item in list_of_rules:
            if item.islower():
                continue
            x = cfg_pSet(item, V, 0)
            if "|" in x:
                x = x.split("|")
                for i in x:
                    new_rules.append(i)
            else:
                new_rules.append(x)
            cfg[nonterminal] = new_rules

    return cfg


#recursive method used to find all possible combinations for a given rule
def cfg_pSet(rule, V, i):
    if len(V) == i:
        return rule
    elif V[i] in rule:
        if rule[0] == rule[-1] and rule[0].isupper() and len(rule) > 1:
            new_rule = rule.lstrip(rule[0]) + "|" + rule.rstrip(rule[-1])
            rule += "|" + new_rule
            return cfg_pSet(rule, V, i+1)

        new_rule = rule.replace(V[i], "")
        if new_rule == "":
            return cfg_pSet(rule, V, i+1)

        rule +=  "|" + new_rule
        return cfg_pSet(rule, V, i+1)
    else:
        return cfg_pSet(rule, V, i+1)


#method used to eliminate all useless rules
def elim_useless_rules(cfg, check_list):
    x = []
    check = False
    to_be_removed = []

    # checks if all current letters in check_list are in a rule and adds it to x
    for variable, rules_list in cfg.items():
        for rule in rules_list:
            if "|" in rule:
                rule = rule.split("|")
            for character in rule:
                if character not in check_list:
                    check = False
                    break
                check = True
            if check:
                x.append(variable)
                check_list.append(variable)
                break

    #if a non-terminal is not in x then add it to to_be_removed
    for variable in cfg.keys():
        if variable not in x:
            to_be_removed.append(variable)

    #if there are items that need to be removed then remove them from the dictionary
    if to_be_removed:
        for item in to_be_removed:
            cfg.pop(item)
            for list_of_rules in cfg.values():
                for rule in list_of_rules:
                    if item in rule:
                        list_of_rules.remove(rule)

    return cfg


#method used to print the cfg
def print_cfg(cfg):
    for nonterminal, rules in cfg.items():
        print(nonterminal + "->", end="")
        for rule in rules:
            if rules[-1] == rule:
                print(rule)
                continue
            print(rule + "|", end="")


if __name__ == "__main__":
    read_file()
