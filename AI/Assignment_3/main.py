class BayesNet:
    def calc_prob(self, b, e, a, j, m):
        return (
            self.prob("B", b, None, None)
            * self.prob("E", e, None, None)
            * self.prob("A|B,E", a, b, e)
            * self.prob("J|A", j, a, None)
            * self.prob("M|A", m, a, None)
        )

    def prob(self, query, val1, val2, val3):
        if query == "B":
            return 0.001 if val1 else 0.999
        elif query == "E":
            return 0.002 if val1 else 0.998
        elif query == "A|B,E":
            temp = (
                0.95 if val2 and val3 else 0.94 if val2 else 0.29 if val3 else 0.001
            )
            return temp if val1 else 1 - temp
        elif query == "J|A":
            temp = 0.9 if val2 else 0.05
            return temp if val1 else 1 - temp
        elif query == "M|A":
            temp = 0.7 if val2 else 0.01
            return temp if val1 else 1 - temp

    def enumerate(self, variables):
        if None not in variables:
            b, e, a, j, m = variables
            return self.calc_prob(b, e, a, j, m)
        none_idx = variables.index(None)
        new_vars = list(variables)
        new_vars[none_idx] = True
        val1 = self.enumerate(new_vars)
        new_vars[none_idx] = False
        val2 = self.enumerate(new_vars)
        return val1 + val2

    def gen_values(self, variables):
        result = [None] * 5
        for i, var in enumerate(variables):
            if var == "Bt":
                result[0] = True
            elif var == "Bf":
                result[0] = False
            elif var == "Et":
                result[1] = True
            elif var == "Ef":
                result[1] = False
            elif var == "At":
                result[2] = True
            elif var == "Af":
                result[2] = False
            elif var == "Jt":
                result[3] = True
            elif var == "Jf":
                result[3] = False
            elif var == "Mt":
                result[4] = True
            elif var == "Mf":
                result[4] = False
        return result

import sys

given = False
observations = []
query = []

for arg in sys.argv[1:]:
    if arg == "given":
        given = True
        continue
    query.append(arg)
    if given:
        observations.append(arg)

bnet = BayesNet()

if query:
    num = bnet.enumerate(bnet.gen_values(query))
    if observations:
        den = bnet.enumerate(bnet.gen_values(observations))
    else:
        den = 1
    print(f"The probability is : {num / den:.9f}")
else:
    print("Invalid query string")