from fo_lfp import *

# list, keys, hlist recursive definitions
Rlist = ["iff", ["list", ["x"]],
                ["or", ["==", ["x"], ["nil"]],
                       ["and", ["!=", ["x"], ["nil"]],
                               ["list", ["next", ["x"]]]]]]

Rhlist = ["==", ["hlist", ["x"]],
                ["ite", ["==", ["x"], ["nil"]],
                        ["\empty"],
                        ["union", ["singleton", ["x"]],
                                  ["hlist", ["next", ["x"]]]]]]

Rkeys = ["==", ["keys", ["x"]],
               ["ite", ["==", ["x"], ["nil"]], 
                       ["\empty"],
                       ["union", ["singleton", ["key", ["x"]]],
                                 ["keys", ["next", ["x"]]]]]]

# primed versions of list, keys, hlist
Rlist2 = ["iff", ["list2", ["x"]],
                 ["or", ["==", ["x"], ["nil"]],
                        ["and", ["!=", ["x"], ["nil"]],
                                ["list2", ["next2", ["x"]]]]]]

Rhlist2 = ["==", ["hlist2", ["x"]],
                 ["ite", ["==", ["x"], ["nil"]],
                         ["\empty"],
                         ["union", ["singleton", ["x"]],
                                   ["hlist2", ["next2", ["x"]]]]]]

Rkeys2 = ["==", ["keys2", ["x"]],
                ["ite", ["==", ["x"], ["nil"]],
                        ["\empty"],
                        ["union", ["singleton", ["key", ["x"]]],
                                  ["keys2", ["next2", ["x"]]]]]]

rec_defs = [Rlist, Rkeys, Rhlist, Rlist2, Rkeys2, Rhlist2]

## LOOP INVARIANT VC

# precondition
pre = ["and", ["list", ["orig"]],
              ["list", ["rev"]],
              ["==", ["intersect", ["hlist", ["orig"]], ["hlist", ["rev"]]], ["\empty"]],
              ["==", ["union", ["keys", ["orig"]], ["keys", ["rev"]]], ["$", "kk"]]]

# program transformation
code = ["and", ["==", ["tmp"], ["next", ["orig"]]],
               ["==", ["rev2"], ["orig"]],
               ["==", ["orig2"], ["tmp"]]]

# postcondition
post = ["and", ["list2", ["orig2"]],
               ["list2", ["rev2"]],
               ["==", ["intersect", ["hlist2", ["orig2"]], ["hlist2", ["rev2"]]], ["\empty"]],
               ["==", ["union", ["keys2", ["orig2"]], ["keys2", ["rev2"]]], ["$", "kk"]]]

# axiom for next2
axiom_next2 = ["==", ["$", "next2"],
                     ["store", ["$", "next"], ["orig"], ["rev"]]]

# frame rule
frame_result = ["and", ["==", ["list", ["x"]], ["list2", ["x"]]],
                       ["==", ["hlist", ["x"]], ["hlist2", ["x"]]],
                       ["==", ["keys", ["x"]], ["keys2", ["x"]]]]
frame_rule = ["implies", ["select", ["singleton", ["orig"]], ["x"]], frame_result]

# collect terms and instantiate recursive defs and frame rule with those terms
terms = collect_terms_formulas([pre, code, post, axiom_next2])
formulas = remove_duplicates(instantiate(terms, ["x"], rec_defs + [frame_rule]))

# repeat process using formulas from previous instantiation
new_terms = collect_terms_formulas(formulas)
print len(new_terms)

new_formulas = remove_duplicates(instantiate(new_terms, ["x"], rec_defs + [frame_rule]))
print len(new_formulas)
