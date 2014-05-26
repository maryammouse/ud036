import movie
import fresh_tomatoes

toy_story = movie.Movie("Toy Story",
                        "A tale about a boy and his toys that come to life.",
                        "http://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc&feature=kp")

avatar = movie.Movie("Avatar",
                     "A marine makes friends with aliens on another world",
                     "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "http://www.youtube.com/watch?v=cRdxXPV9GNQ")

tangled = movie.Movie("Tangled", "Fun retelling of a classic tale!",
                      "http://images4.fanpop.com/image/photos/18600000/Tangled-Poster-disney-18638629-1012-1500.jpg",
                      "https://www.youtube.com/watch?v=ycoY201RTRo")

frozen = movie.Movie("Frozen", "Retelling of 'The Snow Queen'",
                   "http://filmtrailer.hu/wp-content/uploads/Jegvarazs_poszter_3.jpg",
                   "https://www.youtube.com/watch?v=FLzfXQSPBOg")

#print(toy_story.storyline)

#avatar.show_trailer()

movies = [toy_story, avatar, tangled, frozen]

fresh_tomatoes.open_movies_page(movies)

