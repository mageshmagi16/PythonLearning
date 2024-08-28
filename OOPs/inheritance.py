class Hollywood:
    def __init__(self, moviename, year):
        self.moviename = moviename
        self.year = year

    def hitmovies(self):
        print(self.moviename, "is the first hit movie of Marvel which was released in", self.year)

class Director(Hollywood):
    pass
        
    def printeverything(self):
        print(self.moviename, "the movie of Marvel which was released in", self.year)


Marvel = Hollywood("Spiderman", 2002)
Marvel.hitmovies()


Director_1 = Director("Avengers", 2012)
Director_1.printeverything()