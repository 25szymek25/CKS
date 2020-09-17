init python:

    class Place(object):
        def __init__(self, Name, ID, IsActive):
            self.Name = Name
            self.ID = ID
            self.IsActive = IsActive

        @property
        def Bg_Image(self):
            FilePath = "images/places/backgrounds/" + self.ID + ".jpg"
            return FilePath

        def Unlock(self):
            self.IsActive = True

        def Lock(self):
            self.IsActive = False

    Locations = []

    Locations.append(Place("My Bedroom", "mc_bedroom", False))
    Locations.append(Place("Kitchen", "mc_kitchen", False))
    Locations.append(Place("Bathroom", "mc_bathroom", False))
    Locations.append(Place("Mom Bedroom", "mc_mom_bedroom", False))

    class People(object):
        def __init__(self, FirstName, Surname, ID, Location, IsActive):
            self.FName = FirstName
            self.SName = Surname
            self.ID = ID
            self.Location = Location
            self.IsActive = IsActive

        @property
        def FullName(self):
            Output = self.FName + " " + self.SName
            return Output

        def Unlock(self):
            self.IsActive = True

        def Lock(self):
            self.IsActive = False

        @property
        def Avatar(self):
            global Location
            Output = "images/avatars/" + self.ID + "_" + CodeFriendlyLocationName() + ".png"

    Characters = []

    Characters.append(People("Jhon", "Jones", "jhon_jones", 0, True))
    Characters.append(People("milf", "Kuchnia", "milf_kuchnia", 1, True))
    Characters.append(People("milf", "Lazienka", "milf_lazienka", 2, True))
    Characters.append(People("My", "mother", "mom_bed", 3, True))

    def CodeFriendlyLocationName():
        global Location
        global Locations
        for q in Locations:
            if Location == q.Name:
                return q.ID
        return ""

    def CodeFriendlyLocationNumber():
        global Location
        global Locations
        for q, i in enumerate(Locations):
            if Location == q.Name:
                return i
        return -1
