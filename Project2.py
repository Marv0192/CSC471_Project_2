

def main():
    cfg_dict = {}
    V = []
    check_list = []
    with open("Test_3.txt", "r") as file:
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


def elim_e_rules(cfg, V):
    #if V is empty then split the rules and update the dictionary
    #if not V:
       #for variable, rule in cfg.items():
            #new_rule = rule.split("|")
            #cfg[variable] = new_rule

    #if V is not empty then remove any letters in our rules that are in V, split the rules and update dictionary
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
        new_list_of_rules = []
        for item in list_of_rules:
            for letter in V:
                if letter in item:
                    new_rule = item.replace(letter, "")
                    if new_rule != "" and new_rule not in list_of_rules:
                        list_of_rules.append(new_rule)
                        new_list_of_rules.append(new_rule)
        for all_rules in new_list_of_rules:
            rule = rule + "|" + all_rules
            cfg[variable] = rule



    print("After further removing empty rules:")
    for variable, rule in cfg.items():
        print(variable + " -> ", rule)
    print(V)

    return cfg



main()

