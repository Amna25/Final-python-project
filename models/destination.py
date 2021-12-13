class Destination:

    def __init__(self, name, city, visited, id=None):
        self.name= name
        self.city= city
        self.visited= visited
        self.id = id

    def places_to_vist(self):
        self.visited = True

    def still_to_visit(self):
        self.visited = False

  