from fo_lfp import *

Rlist = ["iff", ["list", ["x"]],
                ["or", ["==", ["x"], ["nil"]],
                       ["and", ["!=", ["x"], ["nil"]],
                               ["list", ["next", ["x"]]]]]]

Rkeys = ["==", ["keys", ["x"]],
               ["ite", ["==", ["x"], ["nil"]], 
                       ["\empty"], 
                       ["union", ["singleton", ["key", ["x"]]],
                                 ["keys", ["next", ["x"]]]]]]

Rhlist = ["==", ["hlist", ["x"]],
               ["ite", ["==", ["x"], ["nil"]], 
                       ["\empty"], 
                       ["union", ["singleton", ["x"]],
                                 ["hlist", ["next", ["x"]]]]]]

Rlist2 = ["iff", ["list2", ["x"]],
                ["or", ["==", ["x"], ["nil"]],
                       ["and", ["!=", ["x"], ["nil"]],
                               ["list2", ["next2", ["x"]]]]]]

Rkeys2 = ["==", ["keys2", ["x"]],
               ["ite", ["==", ["x"], ["nil"]], 
                       ["\empty"], 
                       ["union", ["singleton", ["key", ["x"]]],
                                 ["keys2", ["next2", ["x"]]]]]]

Rhlist2 = ["==", ["hlist2", ["x"]],
               ["ite", ["==", ["x"], ["nil"]], 
                       ["\empty"], 
                       ["union", ["singleton", ["x"]],
                                 ["hlist2", ["next2", ["x"]]]]]]
