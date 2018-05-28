# Check if formulas added to solver are satisfiable. Return model or None if unsat
def check_sat(solver):
    is_sat = solver.check()
    print is_sat

    if (is_sat == sat):
        return solver.model()
    return None

# Replace var in rec def with term
def replace(in_list, var, term):
    if in_list == []:
        return []

    if in_list[0] == [var]:
        return [term] + replace(in_list[1:], var, term)

    if type(in_list[0]) != list:
        return [in_list[0]] + replace(in_list[1:], var, term)

    if type(in_list[0]) == list:
        return [replace(in_list[0], var, term)] + replace(in_list[1:], var, term)

# Instantiate one rec_def with all terms found so far
def instantiate_one(terms, variables, rec_def):
    if variables == []:
        return [rec_def]

    partial_rec_defs = []
    for term in terms:
        partial_rec_defs += replace(rec_def, variables[0], term)
    
    return instantiate_many(terms, variables[1:], partial_rec_defs) 

# Instantiate all rec_defs with all terms found so far
def instantiate_many(terms, variables, rec_defs):
    inst = []
    for rec_def in rec_defs:
        inst += instantiate_one(terms, variables, rec_def)

    return inst

# Helper for instantiating
# TODO: make sure correct with many variables
def instantiate(terms, variables, rec_defs):
    out = []
    for term in terms:
        out += [instantiate_many([term], variables, rec_defs)]
    return out

# Collect ground terms from formula
def collect_terms_formula(formula):
    constants = ["True", "False"]
    formulas = ["not", "and", "or", "iff", "==", "!="]
    rec_defs = ["list"]
    unwanted = constants + formulas + rec_defs
    
    terms = ["next"]
    all_connectors = unwanted + terms

    if formula == []:
        return []

    elif formula[0] in unwanted:
        return collect_terms_formulas(formula[1:])

    # TODO: may not need this case
    elif not(formula[0].lstrip("-").isdigit()) and formula[0] not in all_connectors:
        # TODO: make sure there is nothing else in the list
        return [[formula[0]]]

    elif formula[0] in terms:
        return [formula] + collect_terms_formulas(formula[1:])
    
    else:
        # throw error correctly
        print "ERROR"

# Collect ground terms from formulas
def collect_terms_formulas(formulas):

    out = []

    for formula in formulas:
        out += collect_terms_formula(formula)

    return remove_duplicates(out)

# TODO: remove duplicate items in list of terms
def remove_duplicates(init_list):
    final_list = []
    for item in init_list:
        if item not in final_list:
            final_list += [item]
    return final_list

