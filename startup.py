from robots import Robots
from sys import argv

if len(argv) != 2:
    print ("Usage: python3 startup.py url")
    exit(0)

# print(argv[1])

robotHandler = Robots(argv[1])
robotHandler.print_disallowed()

print(robotHandler.can_view('file.php'))