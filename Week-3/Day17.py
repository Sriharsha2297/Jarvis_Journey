# Decorators & Context Managers
# n What is a decorator?
# n Write your own: def timer(func):
# n Context managers (you've used with)
# n __enter__ / __exit__
# n Review and clean up Week 3
# n Decorators are everywhere in FastAPI, LangChain.

def timer(func):
    import time
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.4f} seconds")
        return result
    return wrapper

# *args, **kwargs is the fix. It means "accept whatever arguments come in, however many, named or not":
# pythondef wrapper(*args, **kwargs):    # accepts anything
#     result = func(*args, **kwargs)   # passes it all straight through
#     return result

# Two jobs happening here:

# def wrapper(*args, **kwargs) collects all incoming arguments into a tuple (args) and a dict (kwargs).
# func(*args, **kwargs) unpacks them back out and forwards them to the real function.


@timer
def example_function(n):
    total = 0
    for i in range(n):
        total += i
    return total    
if __name__ == "__main__":
    print(example_function(100))