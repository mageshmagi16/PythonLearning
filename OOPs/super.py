class Hollywood:
    def __init__(self, moviename, year):
        self.moviename = moviename
        self.year = year

    def hitmovies(self):
        print(self.moviename, "is the first hit movie of Marvel which was released in", self.year)

class Director(Hollywood):
    def __init__(self, moviename, year, directorname):
        super().__init__(moviename, year)
        self.directorname = directorname
        
    def printeverything(self):
        print(self.directorname, "directed", self.moviename, "the first hit movie of Marvel which was released in", self.year)


Marvel = Hollywood("Spiderman", 2002)
Marvel.hitmovies()


Director_1 = Director("Spiderman", 2002, "Sam Raimi")
Director_1.printeverything()