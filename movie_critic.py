recent_movies = [('Iron Man 3', 78),
                 ('The Great Gatsby', 48),
                 ('Star Trek Into Darkness', 90),
                 ('Oblivion', 56)]
movie_stars = [('Leonardo DiCaprio', 'The Great Gatsby'),
               ('Tom Cruise', 'Oblivion'),
               ('Robert Downey Jr.', 'Iron Man 3'),
               (None, 'Star Trek Into Darkness')]
#####################################                 
def likes_movie():
    print "\n" 
    print "I watched {} the other day.".format(movie)
    print "This movie is awesome!"
    print "Rotten Tomatoes agrees: they gave {} a score of {} out of 100".format(movie,rating)
    
def dislikes_movie():
    print "\n" 
    print "I watched {} the other day.".format(movie)
    print "This movie sucked!"
    print "Rotten Tomatoes agrees: they gave {} a score of {} out of 100".format(movie,rating)   
def average_movie():
    print "\n" 
    print "I watched {} the other day.".format(movie)
    print "It was okay!"
    print "Rotten Tomatoes agrees: they gave {} a score of {} out of 100".format(movie,rating)    
   ########################### 


for movie, rating in recent_movies:
    if rating > 75:
        likes_movie()
        for actor, movie1 in movie_stars:
            if movie == movie1:
                print "{} was pretty good in it, though".format(actor)
    elif rating < 50:
        dislikes_movie()
        for actor, movie1 in movie_stars:
            if movie == movie1:
                print "{} was pretty good in it, though".format(actor)
    else:
        average_movie()
        for actor, movie1 in movie_stars:
            if movie == movie1:
                print "{} was pretty good in it, though".format(actor)
     
 