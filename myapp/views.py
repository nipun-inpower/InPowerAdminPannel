from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from myapp.models import Blog, BlogCategory, Communities
import requests
from django.shortcuts import render
from django.http import HttpResponse
import json
from django.shortcuts import redirect

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
# Create your views here.
def dashboard(request):
    image_url = "https://nodejsbucketinpower2.s3.amazonaws.com/images/1725268563063-christine-siracusa-Cs5xVwB50Ps-unsplash.jpg"
    api_url = "http://localhost:3000/report"
    response = requests.get(api_url)

    api_urluser = "http://localhost:3000/userall"
    responseuser = requests.get(api_urluser)

    
    
    if response.status_code == 200:
        posts_data = response.json()  # Parsing the JSON response
        post_count = len(posts_data)  # Count the number of posts
    else:
        post_count = {}  # Handle errors

    if responseuser.status_code == 200:
        users = responseuser.json()  # Parse the JSON response
        users_count = len(users) 
        print('users',users)
        
    else:
        users_count = []

    urlbadge = "http://localhost:3000/allbadges"
    responsebadge = requests.get(urlbadge)
    
    if responsebadge.status_code == 200:
        badges_data = responsebadge.json()  # Extract JSON data from the response
        badge_count = len(badges_data) 
    else:
        badge_count = []


    base_url = "http://localhost:3000/groups"
    responseuserbase_url = requests.get(base_url)
    if responseuserbase_url.status_code == 200:
        group_data = responseuserbase_url.json()  # Extract JSON data from the response
        group_count = len(group_data) 
    else:
        group_count = []

    
    

    return render(request, 'admin/dashboard.html', {'post_count': post_count,"users_count": users_count,"badge_count":badge_count,"group_count":group_count})

    


def user_list(request):
    # Fetch data from Express API
    api_url = "http://localhost:3000/userall"
    response = requests.get(api_url)

    # print('response',response.status_code)
    
    # Check if the request was successful
    if response.status_code == 200:
        users = response.json()  # Parse the JSON response
        for user in users:
            user['id'] = user.pop('_id')  # Rename '_id' to 'id'
    else:
        users = []

    # Pass the data to the template
    return render(request, 'admin/userListing.html', {'users': users})


def verify_user(request, id):
    response = requests.post('http://localhost:3000/verify/{}'.format(id))
    print('RRRRRRRR response',response.status_code)

    return redirect('users')
  
def groups(request):
    base_url = "http://localhost:3000/groups"
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyaWQiOiI2NmQ5YTdlZTdmZThmNjY2YmQ0YzFjOTkiLCJwaG9uZU51bWJlciI6IjU1NDc4NTIiLCJpYXQiOjE3MjYyODg3NzIsImV4cCI6MTcyNjI5MjM3Mn0.tTdv03AQW_BxvcID2iiurIxxcw71Mvbr6neZBy5ePYI"
    
    # Attempt with query parameter
    url_with_token = f"{base_url}?token={token}"
    try:
        # print(f"Attempting request with token in query parameter: {url_with_token}")
        # print(f"Response status code: {response.status_code}")
        # print(f"Response headers: {json.dumps(dict(response.headers), indent=2)}")
        # print(f"Response content: {response.content}")
        
        response = requests.get(url_with_token)
        response.raise_for_status()
        groups_data = response.json()
        return render(request, 'admin/groupsListing.html', {'groups': groups_data})
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    # If query parameter attempt fails, try the previous header attempts
    headers_variants = [
        {"Authorization": f"Bearer {token}"},
        {"Authorization": f"Token {token}"},
        {"Authorization": token},
        {"x-access-token": token},
        {"token": token},
        {"jwt": token},
    ]
    
    for headers in headers_variants:
        try:
            print(f"Attempting request with headers: {headers}")
            response = requests.get(base_url, headers=headers)
            print(f"Response status code: {response.status_code}")
            print(f"Response headers: {json.dumps(dict(response.headers), indent=2)}")
            print(f"Response content: {response.content}")
            
            response.raise_for_status()
            groups_data = response.json()
            return render(request, 'admin/groupsListing.html', {'groups': groups_data})
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error occurred: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    
    return HttpResponse("Failed to fetch groups. Please check server logs for details.", status=500)


def communities(request):
    
    blogCategories = Communities.objects.all()


    data = {
            'blogCategories': blogCategories,
            }
    return render(request, 'admin/communities.html', data)


def creatCommunities(request):


    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        
        image_pic = request.FILES['image']

        fs=FileSystemStorage()
        profile_pic1=fs.save(image_pic.name,image_pic)
        image_one=fs.url(profile_pic1)

        blogCategory = Communities()
        blogCategory.name = name
        blogCategory.description = description
        blogCategory.image = image_one
        blogCategory.save()
        
        blogCategories = Communities.objects.all()
        data = {
            'blogCategories': blogCategories,
            }
        return render(request, 'admin/communities.html', data)
    else:
        blogCategories = Communities.objects.all()


        data = {
            'blogCategories': blogCategories,
            }
        return render(request, 'admin/communities.html', data)

def blogs_category(request):
    
    blogCategories = BlogCategory.objects.all()


    data = {
        'blogCategories': blogCategories,
        }
    return render(request, 'admin/blogs_category.html', data)


def blogs_category_delete(request,id):
    
    blog = BlogCategory.objects.filter(id=id)
    blog.delete()
    
    blogCategories = BlogCategory.objects.all()


    data = {
        'blogCategories': blogCategories,
        }
    return render(request, 'admin/blogs_category.html', data)


def creatBlogCategory(request):

    if request.method == 'POST':
        category_name = request.POST['category_name']
        categoryDescription = request.POST['categoryDescription']
        
        image_pic = request.FILES['image']

        fs=FileSystemStorage()
        profile_pic1=fs.save(image_pic.name,image_pic)
        image_one=fs.url(profile_pic1)

        blogCategory = BlogCategory()
        blogCategory.categoryName = category_name
        blogCategory.categoryDescription = categoryDescription
        blogCategory.image = image_one
        blogCategory.save()
        
        blogCategories = BlogCategory.objects.all()
        
        data = {
            'blogCategories': blogCategories,
            }
        return render(request, 'admin/blogs_category.html', data)
    else:
        blogCategories = BlogCategory.objects.all()


        data = {
            'blogCategories': blogCategories,
            }
        return render(request, 'admin/blogs_category.html', data)

def blogs(request):
    blogs = Blog.objects.all()
    blogCategories = BlogCategory.objects.all()
    
    data = {
        'blogs': blogs,
        'blogCategories': blogCategories,
        }
    return render(request, 'admin/blogs.html', data)


def blogs_delete(request,id):
    
    blog = Blog.objects.filter(id=id)
    blog.delete()
    
    blogs = Blog.objects.all()
    blogCategories = BlogCategory.objects.all()
    
    data = {
        'blogs': blogs,
        'blogCategories': blogCategories,
        }
    return render(request, 'admin/blogs.html', data)

def creatBlog(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        categoryid = request.POST['categoryid']

        blogCategory = BlogCategory.objects.get(id=categoryid)


        
        image_pic = request.FILES['image']

        fs=FileSystemStorage()
        profile_pic1=fs.save(image_pic.name,image_pic)
        image_one=fs.url(profile_pic1)

        blog = Blog()
        blog.title = title
        blog.description = description
        blog.userName = 'Jack'
        blog.blogCategory = blogCategory
        blog.image = image_one
        blog.save()

        blogs = Blog.objects.all()
        blogCategories = BlogCategory.objects.all()
        
        data = {
            'blogs': blogs,
            'blogCategories': blogCategories,
            }
        return render(request, 'admin/blogs.html', data)
    else:
        blogs = Blog.objects.all()
        blogCategories = BlogCategory.objects.all()
        
        data = {
            'blogs': blogs,
            'blogCategories': blogCategories,
            }
        return render(request, 'admin/blogs.html', data)

def compliance(request):
    # Fetching data from API
    api_url = "http://localhost:3000/report"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        posts_data = response.json()  # Parsing the JSON response
        post_count = len(posts_data)  # Count the number of posts
    else:
        posts_data = {}  # Handle errors

    return render(request, 'admin/complience.html', {'posts': posts_data.get('posts', []),'post_count': post_count})
    
    # return render(request, 'admin/complience.html')

def selfie(request):
    # Fetch data from Express API
    api_url = "http://localhost:3000/userall"
    response = requests.get(api_url)

    # print('response',response.status_code)
    
    # Check if the request was successful
    if response.status_code == 200:
        users = response.json()  # Parse the JSON response
        for user in users:
            user['id'] = user.pop('_id')  # Rename '_id' to 'id'
    else:
        users = []

    # Pass the data to the template
    return render(request, 'admin/selfieListing.html', {'users': users})
    

def selfieApprove(request):
    
    return render(request, 'admin/userListing.html')

def suspect(request):
    
    return render(request, 'admin/userListing.html')

def category(request):
    
    return render(request, 'admin/category.html')

def creatCategory(request):
    
    return render(request, 'admin/category.html')

# def badges(request):
    
#     return render(request, 'admin/badgeListing.html')



def badges(request):
    url = "http://localhost:3000/allbadges"
    response = requests.get(url)
    
    if response.status_code == 200:
        badges_data = response.json()  # Extract JSON data from the response
    else:
        badges_data = []

    return render(request, 'admin/badgeListing.html', {'badges': badges_data})

def badges_create(request):
    
    if request.method == 'POST':
        badge_title = request.POST['badge_title']
        single_q_title = request.POST['single_q_title']
        q_title = request.POST['q_title']
        options = request.POST.getlist('options[]')
        answers = request.POST.getlist('vehicle1[]')

        options = request.POST.getlist('options[]')
        answers = request.POST.getlist('vehicle1[]')
        myanswer = None


        options_dict = {}
        for index, option in enumerate(options, 1):
            options_dict[f"Option{index}"] = option
            if str(index) in answers:
                myanswer = f"Option{index}"
            
        response_data = {
            "name": badge_title,
            "badgeIcon": "https://cdn-icons-png.flaticon.com/512/4341/4341875.png",
            "coverImage": "https://cdn-icons-png.flaticon.com/512/3314/3314401.png",
            "video": single_q_title,
            "questions": {
                "q1": {
                    "question": q_title,
                    "options": options_dict,
                    "answer": myanswer
                },
            }
        }


        # Sending the POST request to the Express.js server
        express_url = "http://localhost:3000/badges/create"
        response = requests.post(express_url, json=response_data)
        print('response_data',response_data)
        print('response',response)

        return render(request, 'admin/badgeListing.html')
    else:
        return render(request, 'admin/badgeListing.html')


def badge_delete(request):
    
    return render(request, 'admin/badgeListing.html')



# def badges_create(request):
    
#     if request.method == 'POST':
#         badge_title = request.POST['badge_title']
#         message = request.POST['message']
#         single_q_title = request.POST['single_q_title']
#         answers_title = request.POST['answers_title']
#         q_title = request.POST['q_title']
#         options = request.POST.getlist('options[]')
#         answers = request.POST.getlist('vehicle1[]')


#         image_pic = request.FILES['avatar']
#         fs=FileSystemStorage()
#         profile_pic1=fs.save(image_pic.name,image_pic)
#         image_one=fs.url(profile_pic1)
    

#         options = request.POST.getlist('options[]')
#         answers = request.POST.getlist('vehicle1[]')
#         myanswer = None

#         # for index, option in enumerate(options):
#         #     if str(index) in answers:
#         #         myanswer = option

#         options_dict = {}
#         for index, option in enumerate(options, 1):
#             options_dict[f"Option{index}"] = option
#             if str(index) in answers:
#                 myanswer = f"Option{index}"
            

       
#         print('badge_title',badge_title)
#         print('message',message)
#         print('single_q_title',single_q_title)
#         print('answers_title',answers_title)
#         print('q_title',q_title) 
#         print('myanswer',myanswer)
#         print('answers',answers)
#         print('options_dict',options_dict)
#         print('image_one',image_one)

#         # Parse incoming JSON


#         response_data = {
#             "name": badge_title,
#             "badgeIcon": "https://cdn-icons-png.flaticon.com/512/4341/4341875.png",
#             "coverImage": "https://cdn-icons-png.flaticon.com/512/3314/3314401.png",
#             "video": single_q_title,
#             "questions": {
#                 "q1": {
#                     "question": q_title,
#                     "options": options_dict,
#                     "answer": myanswer
#                 },
#                 # Add more questions if needed
#             }
#         }



#         print('response_data',response_data)
#         # Sending the POST request to the Express.js server
#         express_url = "http://localhost:3000/badges/create"
#         response = requests.post(express_url, json=response_data)
#         print('response',response)

#         # try:
#         #     response = requests.post(express_url, json=response_data)
#         #     response.raise_for_status()  # Raise an exception for HTTP errors
#         #     return JsonResponse({"status": "success", "response": response.json()})
#         # except requests.exceptions.RequestException as e:
#         #     return JsonResponse({"status": "error", "message": str(e)})
            
            
        
#         return render(request, 'admin/badgeListing.html')
#     else:
#         return render(request, 'admin/badgeListing.html')