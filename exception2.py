# Example of Raising Predefined Exception
try:
    raise MemoryError('memory error')
except MemoryError as e:
    print(e)

# User-Defined Exception Class
class Accident(Exception):
    def __init__(self, msg):
        self.msg = msg

    def print_exception(self):
        print("User defined exception: ", self.msg)
    def handle(self):
        print("Take a detour")

# Demonstrating User-Defined Exception
if __name__ == "__main__":
    try:
        raise Accident("Crash between two cars")
    except Accident as e:
        e.print_exception()
        e.handle()
    finally:
        print("This execute if the exception is handled or not")
