from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Reviews, Movies

# Create your views here.

"""
Create a review for a movie by a user.

request: HttpRequest object
 - Method: POST
 - Body: {
    "movie_id": int,
    "review": str,
    "rating": int
 }

response: TBD
"""
@login_required
def create_review(request):
    if request.method != "POST":
        return JsonResponse({"error": "Invalid request method"}, status=400)

    try:
        movie_id = request.POST['movie_id']
        review = request.POST['review']
        rating = request.POST['rating']

        # Find movie
        movie = Movies.objects.get(id=movie_id)
        # Create review
        review = Reviews.objects.create(
            movie=movie,
            user=request.user,
            review=review,
            rating=rating
        )
        return JsonResponse({
            "message": "Review created successfully",
            "review": {
                "id": review.id,
                "movie": review.movie.name,
                "user": review.user.username,
                "review": review.review,
                "rating": review.rating,
                "created_at": review.created_at.isoformat(),
                "modified_at": review.modified_at.isoformat()
            }
        }, status=201)
    except KeyError as e:
        return JsonResponse({"error": f"Missing key: {e}"}, status=400)
    except Movies.DoesNotExist as e:
        return JsonResponse({"error": f"Movie not found"}, status=404)
    except Exception as e:
        print(e)
        return JsonResponse({"error": "Internal server error"}, status=500)

"""
Update a review for a movie by a user.

request: HttpRequest object
 - METHOD: GET
    - Body: {
        "review_id": int
    }
 - Response: {
    "review": {
        "review_id": int,
        "movie": str,
        "review": str,
        "rating": int
    }
 }

 - METHOD: POST
    - Body: {
        "review_id": int,
        "review": str,
        "rating": int
    }

GET gets the review data so the user can see it and update it.
POST updates the review data.
"""
@login_required
def update_review(request):
    if request.method == "GET":
        try:
            review_id = request.GET['review_id']
            review = Reviews.objects.get(id=review_id)
            return JsonResponse({
                "review": {
                    "review_id": review.id,
                    "movie": review.movie.name,
                    "review": review.review,
                    "rating": review.rating,
                }
            }, status=200)
        except KeyError as e:
            return JsonResponse({"error": f"Missing key: {e}"}, status=400)
        except Reviews.DoesNotExist as e:
            return JsonResponse({"error": f"Review not found"}, status=404)
        except Exception as e:
            return JsonResponse({"error": "Internal server error"}, status=500)

    elif request.method == "POST":
        try:
            review_id = request.POST['review_id']
            review = Reviews.objects.get(id=review_id)
            review.review = request.POST['review']
            review.rating = request.POST['rating']
            review.save()
            return JsonResponse({
                "message": "Review updated successfully",
            }, status=200)
        except KeyError as e:
            return JsonResponse({"error": f"Missing key: {e}"}, status=400)
        except Reviews.DoesNotExist as e:
            return JsonResponse({"error": f"Review not found"}, status=404)
        except Exception as e:
            return JsonResponse({"error": "Internal server error"}, status=500)

"""
Delete a review for a movie by a user.

request: HttpRequest object
    - Method: POST
    - Body: {
        "review_id": int
    }

response: TBD
"""
@login_required
def delete_review(request):
    try:
        review = Reviews.objects.get(id=request.POST['review_id'])
        review.delete()
        return JsonResponse({"message": "Review deleted successfully"}, status=200)
    except KeyError as e:
        return JsonResponse({"error": f"Missing key: {e}"}, status=400)
    except Exception as e:
        return JsonResponse({"error": "Internal server error"}, status=500)
