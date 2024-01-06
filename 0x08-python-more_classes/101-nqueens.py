#!/usr/bin/python3
"""
nqueens backtracking program to print the coordinates of n queens
on an nxn grid such that they are all in non-attacking positions
"""


from sys import argv

if __name__ == "__main__":
    a = []
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
    n = int(argv[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)

    # initialize the answer list
    for k in range(n):
        a.append([k, None])

    def already_exists(y):
        """check that a queen does not already exist in that y value"""
        for l in range(n):
            if y == a[l][1]:
                return True
        return False

    def reject(l, y):
        """determines whether or not to reject the solution"""
        if (already_exists(y)):
            return False
        k = 0
        while(k < l):
            if abs(a[k][1] - y) == abs(k - l):
                return False
            k += 1
        return True

    def clear_a(l):
        """clears the answers from the point of failure on"""
        for k in range(l, n):
            a[k][1] = None

    def nqueens(l):
        """recursive backtracking function to find the solution"""
        for y in range(n):
            clear_a(l)
            if reject(l, y):
                a[l][1] = y
                if (l == n - 1):  # accepts the solution
                    print(a)
                else:
                    nqueens(l + 1)  # moves on to next x value to continue

    # start the recursive process at l = 0
    nqueens(0)
