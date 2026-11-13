import os


class FileWritter:
	def __init__(self, story):
		self.story = story
		self.dir = input('What folder-name do you want your output files to be in? ')
		if self.dir == '':
			self.dir = 'story'
		output_dir = f'./{self.dir}'
		if os.path.exists(output_dir):
			raise FileExistsError('This folder already exists! Please try again.')

		else:
			os.mkdir(output_dir)
			os.mkdir(f'{output_dir}/pages')

	def main(self):
		story = self.story
		self.write_cover()
		self.write_event(story.root)

	def write_cover(self):
		story = self.story
		markdown = (
			f'{story.title.title()}\n'
			f'{len(story.title) * "="}\n\n'
			f'{story.subtitle.title()}\n'
			f'{len(story.subtitle) * "-"}\n\n'
			f'> {story.synopsis}\n\n'
			'---\n\n'
			'### [*click here to start reading*]'
			f'(./pages/{id(story.root)}.md)\n'
		)

		# Then, create the file.
		with open(f'./{self.dir}/START.md', 'w+') as file:
			file.write(markdown)

	def write_event(self, event):
		# Compile the event path.
		event_path = f'./{self.dir}/pages/{id(event)}.md'
		# Check if the compiled Markdown file exists.
		if os.path.isfile(event_path):
			return

		# First, create the list of options.
		option_list = ''
		for index, choice in enumerate(event.choices):
			outcome = event.outcomes[index]
			# Compile the event path.
			outcome_path = f'./{id(outcome)}.md'
			option_list += f'1. [{choice}]({outcome_path})\n'

		if option_list != '':
			option_list = '\n---\n\n' + option_list

		# Next, compile the Markdown.
		markdown = (
			f'{event.content}\n'
			f'{option_list}'
		)

		# Then, create the file.
		with open(event_path, 'w+') as file:
			file.write(markdown)

		# Finally, repeat for child events.
		for outcome in event.outcomes:
			self.write_event(outcome)
