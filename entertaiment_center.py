import fresh_tomatoes
import media

amelie = media.Movie("Amelie",
												"A story of a girl and her naighbor in Montmartre, Paris",
												"https://upload.wikimedia.org/wikipedia/en/thumb/5/53/Amelie_poster.jpg/220px-Amelie_poster.jpg",
												"https://www.youtube.com/watch?v=sECzJY07oK4")

he_is_not_that_into_you = media.Movie("He Is Not That Into You",
										 "A story about the complexities of modern relationships",
										 "https://upload.wikimedia.org/wikipedia/en/thumb/2/2e/Notintoyouposter.jpg/220px-Notintoyouposter.jpg",
										 "https://www.youtube.com/watch?v=3_DHhPckJNo")


love_actually = media.Movie("Love Actually",
										 "A story of verious coupples in christmas season.",
										 "https://upload.wikimedia.org/wikipedia/en/thumb/e/eb/Love_Actually_movie.jpg/220px-Love_Actually_movie.jpg",
										 "https://www.youtube.com/watch?v=KdzH6a-XEGM")


sister_act = media.Movie("Sister Act",
										 "A singer went to a church, and started to lead a gospel choir",
										 "https://upload.wikimedia.org/wikipedia/en/thumb/4/46/Sister_Act_2_Back_in_the_Habit_film_poster.jpg/220px-Sister_Act_2_Back_in_the_Habit_film_poster.jpg",
										 "https://www.youtube.com/watch?v=dfo4r-VNCOA")

midnight_in_paris = media.Movie("Midnight In Paris",
										 "An american men goes to paris and find himseld ",
										 "https://upload.wikimedia.org/wikipedia/en/thumb/9/9f/Midnight_in_Paris_Poster.jpg/215px-Midnight_in_Paris_Poster.jpg",
										 "https://www.youtube.com/watch?v=-NoGpkSTK8k")

barcelona = media.Movie("Vicky Cristina Barcelona",
										 "A story of two american girls spend a summer holiday in Barcelona",
										 "https://upload.wikimedia.org/wikipedia/en/thumb/2/28/Vicky_cristina_barcelona.jpg/220px-Vicky_cristina_barcelona.jpg",
										 "https://www.youtube.com/watch?v=x4VuLUKbnW8")

movies = [amelie, he_is_not_that_into_you, love_actually, sister_act, midnight_in_paris, barcelona]
fresh_tomatoes.open_movies_page(movies)
