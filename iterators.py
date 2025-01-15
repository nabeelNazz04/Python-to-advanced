class RemoteControl:
    """
    A simple iterator class to cycle through a list of TV channels.
    """

    def __init__(self):
        """
        Initialize the RemoteControl with a predefined list of channels and an index.
        """
        self.channels = ['hbo', 'cnn', 'discovery', 'safari']
        self.index = -1

    def __iter__(self):
        """
        Return the iterator object itself.
        """
        return self

    def __next__(self):
        """
        Return the next channel in the list.
        Raise StopIteration when the list ends.
        """
        self.index += 1
        if self.index == len(self.channels):
            raise StopIteration
        return self.channels[self.index]


if __name__ == "__main__":
    r = RemoteControl()  # Create an instance of RemoteControl
    itr = iter(r)        # Get an iterator from the RemoteControl object
    print(next(itr))     # Fetch and print the first channel
    print(next(itr))     # Fetch and print the second channel
    print(next(itr))     # Fetch and print the third channel
    print(next(itr))     # Fetch and print the fourth channel
