class Event:
	'''
	An event can be thought of as a discrete chunk
	of script from the story, like a short act in a play.

	An event usually has a choice at the end,
	as is common in choose-your-own-adventure stories.

	The choices are visible to the reader,
	but their outcomes are not.
	Their outcomes, however,
	take the form of another event.
	'''

	def __init__(self):
		# The content is long-form, unformatted text.
		# It is the main information presented to the user.
		self.content: str = ''

		# Different choices lead to different outcomes.
		# Their array indices correspond to one another.
		self.choices: list[str] = []  # This remains empty if there are no choices.
		self.outcomes: list[Event] = []  # This is empty if the event is terminal.
		# ==NOTE==
		# I was unsure which data structure to use here
		# because each choice and outcome must remain
		# in a specific order set by the writer.

	def __repr__(self) -> str:
		'''
		Represents what is seen by the user.
		Specifically, this method outputs a string
		containing the event content and a numbered
		list of available choices.
		'''
		option_list = ''
		for index, choice in enumerate(self.choices):
			option_list += f'{index + 1}. {choice}\n'

		return (
			f'{self.content}\n'
			f'{option_list}'
		)

	def add_content(
		self,
		parent: 'Event | None' = None,
		choice_index: int | None = None,
	):
		'''
		This method asks the user to
		add string content to the event.

		Call this method without parameters
		exactly once from Story.write().
		Otherwise, provide the parameters to give
		the user context for what they are writing.
		'''
		# ==READ==
		# The user should know this function's
		# context as soon as it is called.
		# Otherwise, they may be asked for
		# input without knowing what it is for.
		print(
			f'\n{"-" * 47}\n'
		)

		if parent is None:
			if choice_index is not None:
				raise ValueError(
					'A parent event and choice ' +
					'index must be provided together.'
				)
		else:
			if choice_index is None:
				raise ValueError(
					'A parent event and choice ' +
					'index must be provided together.'
				)
			# Both the choice and choice
			# index are needed to provide context.
			choice = parent.choices[choice_index]

			# ==READ==
			# The user needs to see what they are adding to.
			# They are adding event content
			# in response to an earlier choice.
			# Show them exactly which choice that is.
			# This event may be revisited later
			# and may have choices of its own.
			print(
				f'{parent}\n'
				f'({choice_index + 1}. {choice})'
			)

		# ==WRITE==
		# Once the user knows the context,
		# ask them to add a section to the story.
		self.content = input(
			'Please input the event\'s content:\t'
		)

	def add_choices(self):
		'''
		This method asks the user
		to add string choices to the event.
		The choices should be based on the event's content.
		'''
		# ==READ==
		# The user should know this function's
		# context as soon as it is called.
		# Otherwise, they may be asked for
		# input without knowing what it is for.
		print(
			f'\n{"-" * 47}\n'
		)

		# The choice variable starts the loop
		# and is later overwritten by a string.
		# An empty string is false; a nonempty
		# string is true because the user entered data.
		choice = True
		# A loop is needed because an
		# event can have many choices.
		while choice:
			# ==READ==
			# The user will be asked whether they want
			# to add another choice to the event.
			# Because this question is repeated,
			# describe the context each time so
			# the user does not forget what they are doing.
			print(self)

			# ==WRITE==
			# Once the user knows the context,
			# ask them to add a choice.
			choice = input(
				'Create a new choice for this event\n'
				'(you can leave this blank to skip):\t'
			)

			# Check whether the user left the choice blank.
			if choice:
				self.choices.append(choice)

		# Once the loop finishes, self.choices is populated.
		# If it is empty, the event is terminal.
		# The for loop ends immediately in this case.
		for choice_index, choice in enumerate(self.choices):
			# Create a new outcome event for each choice.
			event = Event()
			# Add content to the outcome event.
			# Its content branches off
			# from the choices added here.
			event.add_content(self, choice_index)
			# The outcome event proceeds from this event.
			self.outcomes.append(event)

		# Once each event is created,
		# it can have choices of its own.
		# This recursively creates more choices and,
		# with them, more events.
		for event in self.outcomes:
			event.add_choices()

	def is_terminal(self) -> bool:
		'''
		Checks whether the node is a leaf, or an ending.
		There are no more choices
		to be made, so this is the end.

		Was it happy? Was it sad?
		That's for you to decide!
		'''
		return self.outcomes == []
