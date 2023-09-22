def fib(n):
    match n:
        case 1:
            return 1
        case 2:
            return 1
    return fib(n - 1) + fib(n - 2)
