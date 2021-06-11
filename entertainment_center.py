#https://classroom.udacity.com/courses/ud036
import media
import fresh_tomatoes

the_martian = media.Movie("The Martian",
                        "A story of a boy and his toys that come to life",
                        "https://images-na.ssl-images-amazon.com/images/I/51SfhEcgpML._SY445_.jpg",
                        "https://www.youtube.com/watch?v=ej3ioOneTy8")

#print(toy_story.storyline)

prison_break = media.Movie("Prison break",
                     "A marine on an alien planet",
                     "https://starzplay-img-prod-ssl.akamaized.net/474w/foxplus/PRISONBREAKY2005S01E001/PRISONBREAKY2005S01E001-474x677-PST.jpg",
                     "https://www.youtube.com/watch?v=der8A7Z9u7c")

#print(avatar.storyline)
#avatar.show_trailer()

chappie = media.Movie("Chappie", 
                        "Using rock music to learn",
                        "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRm6MlChsY79xdgnIit7SQDcsvilDIHFYGZAx8BZEaC0f-YtJor",
                        "https://www.youtube.com/watch?v=lyy7y0QOK-0")

pk = media.Movie("pk",
                    "A rat is a chef in Paris",
                    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRjmkQeUjBmvwOnmYpTWQKw1oeAp9mEedkA6MznJuEv7VEApmO5",
                    "https://www.youtube.com/watch?v=SOXWc32k4zA")

spirited_away = media.Movie("Spirited Away",
                    "Goging back in time to meet authors",
                    "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcS6MveoDoJOg9-wMvtHE4ak_-HDZeYS1egb9PwRcf8lhrtcppMc",
                    "https://www.youtube.com/watch?v=ByXuk9QqQkk")

coco = media.Movie("Coco",
                    "A reality real reality show",
                    "https://upload.wikimedia.org/wikipedia/en/9/98/Coco_%282017_film%29_poster.jpg",
                    "https://www.youtube.com/watch?v=Rvr68u6k5sI")   

movies = [the_martian, prison_break , chappie, pk, spirited_away, coco]
fresh_tomatoes.open_movies_page(movies)
