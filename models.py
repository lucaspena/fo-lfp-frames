# Generate all true models
def generate_models(bound, theory):
    models = []
    for i in range(0, bound+1):
        models += generate_models_size(i, theory)
    for model in models:
        print model

# Generate true models of a particular size
def generate_models_size(size, theory):
    d = {}
    model = ''
    for i in range(0, size):
        xi = 'x' + str(i)
        d[xi] = None
    for i in theory['unary-symbols']:
        model += '(and\n'
        for j in d.keys():
            model += '  (or\n'
            for k in d.keys():
                model += '    (= ' + '(' + i + ' ' + j + ') ' + k + ')\n'
            model += '  )\n'
        model += ')\n'
    return [model]

nextf = ['next', ['x']]
listf = ["iff", ["list", ["x"]],
                ["ite", ["==", ["x"], ["nil"]],
                        ["true"],
                        ["list", ["next", ["x"]]]]]
listlen = ["iff", ["listlen", ["x"], ["y"]],
                  ["ite", ["==", ["x"], ["nil"]],
                          ["==", ["y"], ["0"]],
                          ["and", [">", ["y"], ["0"]],
                                  ["listlen", ["next", ["x"]], ["-", ["y"], ["1"]]]]]]

print generate_models_size(4, { 'unary-symbols': ['next'],
                                'constants': ['-1'],
                                'axioms': [listf, listlen] })[0]
