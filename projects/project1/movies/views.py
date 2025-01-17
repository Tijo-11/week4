from django.shortcuts import render
from django.http import HttpResponse

# Create a View to Set a Session Value
def set_favorite_movie(request):
    # Set a session value
    request.session.set_expiry(10)#time in seconds
    request.session['favorite_movie'] = 'Inception'
    # return HttpResponse("Your favorite movie has been set!")
     # Set a cookie
    response = HttpResponse("Your favorite movie has been set!")
    response.set_cookie('movie_cookie', 'Inception', max_age=5)  # Cookie expires in 5 seconds
    return response
    
# Create a View to Retrieve and Display the Session Value
def get_favorite_movie(request):
    # Get the session value
    favorite_movie = request.session.get('favorite_movie', 'No favorite movie set.')
    # return HttpResponse(f"Your favorite movie is: {favorite_movie}")
    # Get cookie value
    movie_cookie = request.COOKIES.get('movie_cookie', 'No movie cookie set.')

    return HttpResponse(f"Session movie: {favorite_movie}<br>Cookie movie: {movie_cookie}")

