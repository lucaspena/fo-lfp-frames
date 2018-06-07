# Check if formulas added to solver are satisfiable. Return model or None if unsat
#def check_sat(solver):
#    is_sat = solver.check()
#    print is_sat
#
#    if (is_sat == sat):
#        return solver.model()
#    return None

# Replace var in rec def with term
#def replace(in_list, var, term):
#    if in_list == []:
#        return []
#
#    if in_list[0] == [var]:
#        return [term] + replace(in_list[1:], var, term)
#
#    if type(in_list[0]) != list:
#        return [in_list[0]] + replace(in_list[1:], var, term)
#
#    if type(in_list[0]) == list:
#        return [replace(in_list[0], var, term)] + replace(in_list[1:], var, term)

# same function as replace, just defined recursively
def replace_rec(in_list, var, term):
    if type(in_list) !=list:
        return in_list
    elif in_list == [var]:
        return term
    else:
        out = []
        for elts in in_list:
            out += [replace_rec(elts, var, term)] 
            
        return out

# Instantiate one rec_def with all terms found so far
def instantiate_one(terms, variables, rec_def):
    if variables == []:
        return [rec_def]

    partial_rec_defs = []
    for term in terms:
        #instantiate first variable with all possible terms, creating several partially instantiated terms
        partial_rec_defs += [replace_rec(rec_def, variables[0], term)]
    
    #recursively instantiate the other variables in all partial instantiations
    return instantiate(terms, variables[1:], partial_rec_defs) 

# Instantiate all rec_defs with all terms found so far
#def instantiate_many(terms, variables, rec_defs):
def instantiate(terms, variables, rec_defs):
    inst = []
    for rec_def in rec_defs:
        inst += instantiate_one(terms, variables, rec_def)

    return inst
            
# Helper for instantiating
# TODO: make sure correct with many variables
#def instantiate(terms, variables, rec_defs):
#    out = []
#    for term in terms:
#        out += [instantiate_many([term], variables, rec_defs)]
#    return out

#Collect foreground terms from each formula/term/subformula given. 
#Input is one level of [], such as ["iff", ...]
def collect_terms(things):
    constants = ["True", "False"]
    bool_constructors = ["not", "and", "or", "iff", "==", "!="]
    predicates = ["list"]
    skip_symbols = ["$"]
    skip_indicator = constants + bool_constructors + predicates + skip_symbols
    
    out = []
    if type(things) != list:
        return []
    
    if len(things) == 0:
        print("ERROR\n\n\n\n")
    if things[0] not in skip_indicator:
        out += [things]
    if len(things) > 1:
        for thing in things:
            out += collect_terms(thing)
    
    return remove_duplicates(out)

#Collect foreground terms on each given formula.
#Input is level 2 list, i.e [[]], such as [formula_1, formula_2, ...] where formula_i is a level 1 list []
#NOTE: It is not clear this function will be useful, since we are always dealing 
#   with one formula (the VC) at any stage
def collect_terms_formulas(formulas):
    out = []
    for formula in formulas:
        out += collect_terms(formula)
    
    return remove_duplicates(out)

# Collect ground terms from formula
#def collect_terms_formula(formula):
#    constants = ["True", "False"]
#    formulas = ["not", "and", "or", "iff", "==", "!="]
#    rec_defs = ["list"]
#    unwanted = constants + formulas + rec_defs
#    
#    terms = ["next"]
#    all_connectors = unwanted + terms
#
#    if formula == []:
#        return []
#
#    elif formula[0] in unwanted:
#        return collect_terms_formulas(formula[1:])
#
#    # TODO: may not need this case
#    elif not(formula[0].lstrip("-").isdigit()) and formula[0] not in all_connectors:
#        # TODO: make sure there is nothing else in the list
#        return [[formula[0]]]
#
#    elif formula[0] in terms:
#        return [formula] + collect_terms_formulas(formula[1:])
#    
#    else:
#        # throw error correctly
#        print("ERROR")
#
## Collect ground terms from formulas
#def collect_terms_formulas(formulas):
#    out = []
#
#    for formula in formulas:
#        out += collect_terms_formula(formula)
#
#    return remove_duplicates(out)

# TODO: remove duplicate items in list of terms
def remove_duplicates(init_list):
    final_list = []
    for item in init_list:
        if item not in final_list:
            final_list += [item]
    return final_list

