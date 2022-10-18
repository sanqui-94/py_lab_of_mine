"""keypress - A module for detecting  a single keypress."""

try:
	import msvcrt

	def getKey():
		"""Wait for a keypress and return a single character string."""
		return msvcrt.getch()

except ImportError:
	
	import sys
	import tty
	import termios

	def getKey():
		"""Wait for a keypress and return a single character string."""
		fd = sys.stdin.fileno()
		original_attributes = termios.tcgetattr(fd)
		try:
			tty.setraw(sys.stdin.fileno())
			ch = sys.stdin.read(1)
		finally:
			termios.tcsetattr(fd, termios.TCSADRAIN, original_attributes)
		return ch
