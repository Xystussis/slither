from robots import Robots
from sys import argv

if len(argv) != 2:
    print("Usage: python3 startup.py url")
    exit(0)

# print(argv[1])
robotHandler = Robots(argv[1])
# print the list of disallowed pages from the site's robot.txt file
robotHandler.print_disallowed()

# Example checking whether we can view /file.php on the server
print(robotHandler.can_view('/file.php'))
