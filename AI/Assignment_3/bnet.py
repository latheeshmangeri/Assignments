from sys import argv

class BayesianNetwork(object):
    def compute_probability(self, values):
        return (
            self.get_probability("B", values[0]) *
            self.get_probability("E", values[1]) *
            self.get_probability("A|B,E", values[2], values[0], values[1]) *
            self.get_probability("J|A", values[3], values[2]) *
            self.get_probability("M|A", values[4], values[2])
        )

    def get_probability(self, check, value, *conditions):
        if check == "B":
            return 0.001 if value else 0.999
        elif check == "E":
            return 0.002 if value else 0.998
        elif check == "A|B,E":
            p_2 = (
                0.95 if conditions[0] and conditions[1] else
                0.94 if conditions[0] and not conditions[1] else
                0.29 if not conditions[0] and conditions[1] else
                0.001
            )
            return p_2 if value else (1 - p_2)
        elif check == "J|A":
            p_2 = 0.9 if conditions[0] else 0.05
            return p_2 if value else (1 - p_2)
        elif check == "M|A":
            p_2 = 0.7 if conditions[0] else 0.01
            return p_2 if value else (1 - p_2)

    def check(self, values):
        if None not in values:
            return self.compute_probability(values)
        else:
            i = values.index(None)
            next_items = list(values)
            next_items[i] = True
            val_1 = self.check(next_items)
            next_items[i] = False
            val_2 = self.check(next_items)
            return val_1 + val_2

    def get_values(self, values):
        result = []
        for var in ["B", "E", "A", "J", "M"]:
            if f"{var}t" in values:
                result.append(True)
            elif f"{var}f" in values:
                result.append(False)
            else:
                result.append(None)
        return result

given = False
observations = []
query = []

for _arg in argv:
    if _arg == "given":
        given = True
    query.append(_arg)
    if given:
        observations.append(_arg)


bnet = BayesianNetwork()

if query:
    x = bnet.check(bnet.get_values(query))
    if observations:
        y = bnet.check(bnet.get_values(observations))
    else:
        y = 1
    print("The probability is : %.9f" % (x/y))
else:
    print("Invalid query string")
