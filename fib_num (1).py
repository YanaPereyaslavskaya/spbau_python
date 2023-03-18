import itertools


class Fib:
    """По объектам этого класса можно итерироваться и получать 6 чисел Фибоначчи"""

    class _FibNum_iter:
        """Внутренний класс — итератор"""

        def __init__(self):
            self.i = 0
            self.fibs = [1, 1]  # они у нас выше были

        def __next__(self):
            self.i += 1
            x = self.fibs[0] + self.fibs[1]
            self.fibs.append(x)
            value = self.fibs[0]
            self.fibs.pop(0)
            return value

    def __iter__(self):
        """Создать и вернуть итератор"""
        return Fib._FibNum_iter()


Fibonacci = Fib()
N = 20
print(list(itertools.islice(Fibonacci, N)))
for i, f in zip(itertools.count(1), itertools.islice(Fibonacci, N)):
    print(f"{i}){f}")