
from sys import maxsize


class Group:
    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    def __eq__(self, other):
        # in case when we come across empty "id"
        # we shouldn't take it into account
        return (self.id is None or other.id is None or self.id == other.id) and (self.name == other.name)

    def __repr__(self):
        return "%s:%s:%s:%s" % (self.id, self.name, self.header, self.footer)

    def id_or_maxval(self):
        """Method used to compare 2 instances by 'id'-parameter.
        In case when some instance have empty 'id', method
        returns 'maxsize' const."""
        if self.id:
            return int(self.id)
        else:
            return maxsize
