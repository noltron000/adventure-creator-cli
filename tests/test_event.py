import pytest
from event import Event


def test_repr_includes_numbered_choices():
	event = Event()
	event.content = 'Choose a path.'
	event.choices = ['Take the forest path', 'Enter the cave']

	assert repr(event) == (
		'Choose a path.\n'
		'1. Take the forest path\n'
		'2. Enter the cave\n'
	)


def test_is_terminal_reflects_outcomes():
	event = Event()
	assert event.is_terminal()

	event.outcomes.append(Event())
	assert not event.is_terminal()


def test_add_content_requires_parent_and_choice_index_together():
	message = 'parent event and choice index must be provided together'

	with pytest.raises(ValueError, match=message):
		Event().add_content(choice_index=0)

	with pytest.raises(ValueError, match=message):
		Event().add_content(parent=Event())
