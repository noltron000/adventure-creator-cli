import sys

from file_writter import FileWritter
from story import Story

if sys.version_info < (3, 14):
	raise SystemExit('Python 3.14 or newer is required.')


if __name__ == '__main__':
	story: Story = Story()
	story.write()
	file_writter: FileWritter = FileWritter(story)
	file_writter.main()
