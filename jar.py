# Cookie Jar
# Problem Set 8

# 🍪

class Jar:
    def __init__(self, capacity=12):    # Initialize Jar with capacity of 12
        if capacity < 0:
            raise ValueError("Invalid capacity")
        self._capacity = capacity
        self._size = 0

    def __str__(self):                  # Returns str with n cookies
        return self.size * "🍪"

    def deposit(self, n):               # Adds n cookies to jar, unless n > 12, in which case ValueError
        if n > self.capacity or n + self.size > self.capacity:
            raise ValueError("Jar is full")
        self._size += n

    def withdraw(self, n):              # Removes n cookies from jar, unless n =< 0, in which case ValueError
        if n > self.size:
            raise ValueError("Jar is empty") 
        self._size -= n

    @property
    def capacity(self):                 # Returns capacity of Jar (12)
        return self._capacity

    @property
    def size(self):                     # Returns number of cookies actually in Jar; initially 0
        return self._size

"""
def main():
    jar = Jar(4)
    jar.deposit(2)
    jar.withdraw(1)
    print(jar.capacity)
    print(jar.size)


if __name__ == "__main__":
    main()
"""