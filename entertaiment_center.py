import fresh_tomatoes
import media


# Iinstances
amelie = media.Movie(
    "2001",
    "PG-12",
    "Amelie",
    "A fanciful comedy about a young French girl",
    "https://upload.wikimedia.org/wikipedia/en/thumb/5/53/Amelie_poster.jpg/220px-Amelie_poster.jpg",  # noqa
    "https://www.youtube.com/watch?v=sECzJY07oK4")


he_is_not_that_into_you = media.Movie(
     "2009",
     "G",
     "He Is Not That Into You",
     "A story about the complexities of modern relationships",
     "https://upload.wikimedia.org/wikipedia/en/thumb/2/2e/Notintoyouposter.jpg/220px-Notintoyouposter.jpg",  # noqa
     "https://www.youtube.com/watch?v=3_DHhPckJNo")


love_actually = media.Movie(
     "2003",
     "G",
     "Love Actually",
     "A story of verious coupples in christmas season",
     "https://upload.wikimedia.org/wikipedia/en/thumb/e/eb/Love_Actually_movie.jpg/220px-Love_Actually_movie.jpg",  # noqa
     "https://www.youtube.com/watch?v=KdzH6a-XEGM")


sister_act = media.Movie(
     "1992",
     "G",
     "Sister Act",
     "A soul singer set up in the guise of a nun in convent",
     "https://upload.wikimedia.org/wikipedia/en/thumb/4/46/Sister_Act_2_Back_in_the_Habit_film_poster.jpg/220px-Sister_Act_2_Back_in_the_Habit_film_poster.jpg",  # noqa
     "https://www.youtube.com/watch?v=dfo4r-VNCOA")


midnight_in_paris = media.Movie(
     "2011",
     "G",
     "Midnight In Paris",
     "A story of american guy spends his holiday in Paris",
     "https://upload.wikimedia.org/wikipedia/en/thumb/9/9f/Midnight_in_Paris_Poster.jpg/215px-Midnight_in_Paris_Poster.jpg",  # noqa
     "https://www.youtube.com/watch?v=-NoGpkSTK8k")


barcelona = media.Movie(
     "2008",
     "G",
     "Vicky Cristina Barcelona",
     "A story of american girls spend a summer holiday in Barcelona",
     "https://upload.wikimedia.org/wikipedia/en/thumb/2/28/Vicky_cristina_barcelona.jpg/220px-Vicky_cristina_barcelona.jpg",  # noqa
     "https://www.youtube.com/watch?v=x4VuLUKbnW8")


breaking_bad = media.Drama(
     "2013",
     "G",
     "Breaking Bad",
     "A man becoming a drug seller to earn money for his fimily",
     "http://static.tvtome.com/images/genie_images/story/2012_usa/b/breakingbad_s5poster.jpg",  # noqa
     "https://www.youtube.com/watch?v=HhesaQXLuRY")


heroes_reborn = media.Drama(
     "2015",
     "G",
     "Heroes Reborn",
     "A story about people who have superpower",
     "http://ia.media-imdb.com/images/M/MV5BMjI0NTE5NDIxOV5BMl5BanBnXkFtZTgwMDQ3ODM2NjE@._V1_SY317_CR0,0,214,317_AL_.jpg",  # noqa
     "https://www.youtube.com/watch?v=4FLHB2zB_cA")


girls = media.Drama(
     "2012",
     "G",
     "Girls",
     "A story about girls living brooklin",
     "http://www.gstatic.com/tv/thumb/tvbanners/9020354/p9020354_b_v7_ac.jpg",
     "https://www.youtube.com/watch?v=RSXvQhR9CHQ")

# Append all movies and dramas infromation in a list and call the external rendering function
videos = [amelie, he_is_not_that_into_you, love_actually, sister_act,
          midnight_in_paris, barcelona, breaking_bad, heroes_reborn, girls]

# Call the external rendering function
fresh_tomatoes.open_videos_page(videos)
