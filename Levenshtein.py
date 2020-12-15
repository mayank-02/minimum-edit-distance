class Levenshtein:
    """
    The Levenshtein distance between two strings: source, target

    Methods:
       constructor(source, target, costs): initialises data attributes and calculates distances and backtrace
       distance(): returns the minimum edit distance for the two strings
       edit_ops(): returns a list of operations to perform on source to transform into target
       print_distance_matrix(): print out the distance matrix
       print_edit_ops(): print out the edit operations

    Data attributes:
       source: source string
       target: target string
       costs: a tuple or a list with three integers (i, d, s)
              where i defines the costs for a insertion
                    d defines the costs for a deletion
                    s defines the costs for a substitution
       D: distance matrix
       edits: operations to perform on source to transform into target

    Usage:
    >>> l = Levenshtein("hello", "world", costs=(2,2,1))
    >>> min_distance = l.distance()
    >>> operations = l.edit_ops()
    >>> print(l.print_distance_matrix())
     -  -  w  o  r  l  d
     -  0  2  4  6  8 10
     h  2  1  3  5  7  9
     e  4  3  2  4  6  8
     l  6  5  4  3  4  6
     l  8  7  6  5  3  5
     o 10  9  7  7  5  4
    >>> print(l.print_edit_ops())
    Type           i  j
    --------------------
    Substitution   0  0
    Substitution   1  1
    Substitution   2  2
    Match          3  3
    Substitution   4  4
    """

    def __init__(self, source, target, costs=(1, 1, 1)):
        self.source = source
        self.target = target
        self.costs = costs
        self.D = self.__edit_distance()
        self.edits = self.__backtrace()

    def __backtrace(self):
        """ Trace back through the cost matrix to generate the list of edits """
        # Find out indices of bottom-right most cell in matrix
        i, j = len(self.source), len(self.target)

        # Assign costs
        insertion_cost, deletion_cost, substitution_cost = self.costs

        # Distance matrix
        D = self.D

        # Declare list of edit operations
        edits = list()

        # While we don't reach the top-leftmost cell
        while not (i == 0 and j == 0):

            # Find out cost of current cell
            current_cost = D[i][j]

            if (i != 0 and j != 0) and current_cost == D[i - 1][j - 1]:
                # Same letter
                i, j = i - 1, j - 1
                edits.append({"type": "Match", "i": i, "j": j})

            elif (i != 0 and j != 0) and current_cost == D[i - 1][
                j - 1
            ] + substitution_cost:
                # Previous cell is diagonally opposite
                i, j = i - 1, j - 1
                edits.append({"type": "Substitution", "i": i, "j": j})

            elif i != 0 and current_cost == D[i - 1][j] + deletion_cost:
                # Previous cell is above current cell
                i, j = i - 1, j
                edits.append({"type": "Deletion", "i": i, "j": j})

            elif j != 0 and current_cost == D[i][j - 1] + insertion_cost:
                # Previous cell is on the left of current cell
                i, j = i, j - 1
                edits.append({"type": "Insertion", "i": i, "j": j})

        # Reverse the backtrace of operations
        edits.reverse()

        return edits

    def __edit_distance(self):
        """ Calculates every cell of distance matrix """

        # Calculate number of rows and columns in distance matrix
        rows = len(self.source) + 1
        cols = len(self.target) + 1

        # Assign costs
        insertion_cost, deletion_cost, substitution_cost = self.costs

        # Declaring distance matrix
        D = [[0 for i in range(cols)] for j in range(rows)]

        # Initialising first row
        for i in range(rows):
            D[i][0] = i * deletion_cost

        # Initialising first column
        for j in range(cols):
            D[0][j] = j * insertion_cost

        # Fill the rest of the matrix
        for i in range(1, rows):
            for j in range(1, cols):
                if self.source[i - 1] == self.target[j - 1]:
                    # Same character
                    D[i][j] = D[i - 1][j - 1]

                else:
                    # Different character

                    # Accounting for the cost of operation
                    insertion = D[i][j - 1] + insertion_cost
                    deletion = D[i - 1][j] + deletion_cost
                    substitution = D[i - 1][j - 1] + substitution_cost

                    # Choosing the best option and filling the cell
                    D[i][j] = min(insertion, deletion, substitution)

        # Return distance matrix
        return D

    def distance(self):
        """ Returns bottom-rightmost entry of distance matrix """

        return self.D[-1][-1]

    def edit_ops(self):
        """ Returns list of edit operations """

        return self.edits

    def print_distance_matrix(self):
        """ Pretty prints the distance matrix """

        rows = len(self.source) + 1
        cols = len(self.target) + 1

        first_row = "--" + self.target
        first_column = "-" + self.source

        for i in first_row:
            print("%2c " % i, end="")

        print()

        for i in range(0, rows):
            print("%2c " % (first_column[i]), end="")

            for j in range(0, cols):
                print("%2d " % (self.D[i][j]), end="")

            print()

    def print_edit_ops(self):
        """ Pretty prints the edit operations """

        print("%-13s %2s %2s" % ("Type", "i", "j"))
        print("-" * 20)

        for op in self.edits:
            print("%-13s %2d %2d\n" % (op["type"], op["i"], op["j"]), end="")