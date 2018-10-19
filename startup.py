# from robots import Robots
from sitereader import SiteReader
from sys import argv

if len(argv) != 2:
    print("Usage: python3 startup.py url")
    exit(0)

# # print(argv[1])
# robotHandler = Robots(argv[1])
# # print the list of disallowed pages from the site's robot.txt file
# robotHandler.print_disallowed()
#
# # Example checking whether we can view /file.php on the server
# if robotHandler.can_view('/'):
#     pass

site_reader = SiteReader(argv[1])
result = site_reader.read()
print(result.get_request())
print(result.get_links())
