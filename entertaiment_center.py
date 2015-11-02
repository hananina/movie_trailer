import fresh_tomatoes
import media

toy_story = media.Movie("toy story",
												"a story of a boy and his toys that come to life",
												"https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
												"https://www.youtube.com/watch?v=QpL9hkXBqk8")
# print(toy_story.story_line)

avatar = media.Movie("Avatar",
										 "a marine on an alian planet",
										 "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
										 "https://www.youtube.com/watch?v=5PSNL1qE6VY")

# print(avatar.story_line)
# avatar.show_trailer()

sisters_act = media.Movie("sister's act",
										 "a singer went to a church, and started to lead a gospel choir",
										 "https://upload.wikimedia.org/wikipedia/en/thumb/4/46/Sister_Act_2_Back_in_the_Habit_film_poster.jpg/220px-Sister_Act_2_Back_in_the_Habit_film_poster.jpg",
										 "https://www.youtube.com/watch?v=dfo4r-VNCOA")

# sisters_act.show_trailer()
school_of_rock = media.Movie("school of rock",
										 "jack black played a guy who is kicked out of his band and subsequently disguises himself as a teacher at a prestigious prep school. ",
										 "https://upload.wikimedia.org/wikipedia/en/thumb/1/11/School_of_Rock_Poster.jpg/220px-School_of_Rock_Poster.jpg",
										 "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

midnight_in_paris = media.Movie("midnight in paris",
										 "an american men goes to paris and find himseld ",
										 "https://upload.wikimedia.org/wikipedia/en/thumb/9/9f/Midnight_in_Paris_Poster.jpg/215px-Midnight_in_Paris_Poster.jpg",
										 "https://www.youtube.com/watch?v=-NoGpkSTK8k")

barcelona = media.Movie("vicky christina barcelona",
										 "directed by Woody Allen",
										 "https://upload.wikimedia.org/wikipedia/en/thumb/2/28/Vicky_cristina_barcelona.jpg/220px-Vicky_cristina_barcelona.jpg",
										 "https://www.youtube.com/watch?v=x4VuLUKbnW8")

movies = [toy_story, avatar, school_of_rock, sisters_act, midnight_in_paris, barcelona]
fresh_tomatoes.open_movies_page(movies)
