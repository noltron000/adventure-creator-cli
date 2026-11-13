import sys

from file_writter import *
from story import *

if sys.version_info < (3, 14):
	raise SystemExit('Python 3.14 or newer is required.')


if __name__ == '__main__':
	story = Story()
	story.write()
	file_writter = FileWritter(story)
	file_writter.main()
