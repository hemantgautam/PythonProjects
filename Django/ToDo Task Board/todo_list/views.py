from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.http import require_http_methods
from .models import TodoList, BoardList
from .forms import TodoListForm, BoardListForm
from django.contrib import messages
from django.contrib.auth.models import User, auth


def home(request):
    is_user_login = False
    if request.user.is_authenticated:
        return redirect('boards')
    else:
        #user login request check
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('boards')
            else:
                messages.error(request, "Login Failed. Enter Correct Username and Password.")
                return redirect('home')
        else:
            return render(request, 'login.html')


# function to delete each item under specific Board
def delete_items(request, list_id):
    if request.user.is_authenticated:
        try:
            # Deleting the item from list by logged in user
            item = TodoList.objects.get(pk=list_id, userid=request.user.id)
            item.delete()
            messages.success(request, "Item has been Deleted")
            # This return will redirect back to the same page
            return redirect(request.META.get('HTTP_REFERER', '/'))
        except:
            return redirect('boards')
    else:
        return redirect('home')


# function to cross title of an item
def cross_off(request, list_id):
    if request.user.is_authenticated:
        try:
            # Updating the completed column of item to True
            item = TodoList.objects.get(pk=list_id, userid=request.user.id)
            item.completed = True
            item.save()
            return redirect(request.META.get('HTTP_REFERER', '/'))
        except:
            return redirect('boards')
    else:
        return redirect('home')


# function to uncross title of an item
def uncross(request, list_id):
    if request.user.is_authenticated:
        try:
            # Updating the completed column of item to False
            item = TodoList.objects.get(pk=list_id, userid=request.user.id)
            item.completed = False
            item.save()
            # This return will redirect back to the same page
            return redirect(request.META.get('HTTP_REFERER', '/'))
        except:
            return redirect('boards')
    else:
        return redirect('home')


# user logout functionality
def logout(request):
    auth.logout(request)
    return redirect('home')


# Store new created board into DB
def board(request, board_id):
    is_user_login = False
    if request.user.is_authenticated:
        is_user_login = True
        try:
            #check id board id in url is valid of not
            board_id_check = BoardList.objects.get(pk=board_id, userid=request.user.id)
            # Getting board id from url by using get_board_id function
            board_get_id = int(get_board_id(request.path))
            # Fetching Board list to show under every board
            board_list = BoardList.objects.filter(userid_id=request.user.id)
            # Fetching list of item for given board id
            todo_list = TodoList.objects.filter(userid=request.user.id, board_id=board_id)
            # checking the same board url for POST and GET method
            if request.method == "POST" and request.POST['form_name'] == "add_list":
                request.POST = request.POST.copy()
                # Assigning logged in user id value to form userid
                request.POST['userid'] = request.user.id
                # Getting board id from url by using get_board_id function
                request.POST['board_id'] = int(get_board_id(request.path))
                form = TodoListForm(request.POST or None)
                if form.is_valid():
                    form.save()
                    messages.success(request, "New item is added in the list")
                    return render(request, 'todolist.html',
                                  {'todo_list': todo_list,
                                   'is_user_login': is_user_login,
                                   'board_id': board_id,
                                   'board_list': board_list,
                                   'board_get_id': board_get_id
                                   })
                else:
                    return redirect('home')
            # This else condition is for GET method
            else:
                if todo_list is not None:
                    return render(request, 'todolist.html',
                                  {'todo_list': todo_list,
                                   'is_user_login': is_user_login,
                                   'board_id': board_id,
                                   'board_list': board_list,
                                   'board_get_id': board_get_id
                                   })
                else:
                    return redirect('boards')
        except:
            return redirect('boards')
    else:
        return redirect('home')


# function to list all the boards of logged in user
def boards(request):
    is_user_login = False
    if request.user.is_authenticated:
        is_user_login = True
        # Fetching all boards created by Logged in User
        board_list = BoardList.objects.filter(userid_id=request.user.id)
        return render(request, 'boards.html', {'board_list': board_list, 'is_user_login': is_user_login})
    else:
        return redirect('home')


# function to delete board, this will delete all items as well because of Foreign key
def deleteboard(request, board_id):
    if request.user.is_authenticated:
        try:
            # Deleting Board row from DB filtering PK and userid
            item = BoardList.objects.get(pk=board_id, userid=request.user.id)
            item.delete()
            messages.success(request, "Board has been Deleted")
            return redirect('boards')
        except:
            return redirect('boards')
    else:
        return redirect('home')


# function to add new board
def addboard(request):
    if request.method == "POST":
        if (request.POST['board_name']):
            request.POST = request.POST.copy()
            # Assigning logged in user id value to form userid
            request.POST['userid'] = request.user.id
            form = BoardListForm(request.POST or None)
            if form.is_valid():
                form.save()
                # fetching id of newly created board by user
                lastest_added_board_list = BoardList.objects.filter(userid_id=request.user.id).latest('id')
                redirect_url = 'board/' + str(lastest_added_board_list.id)
                messages.success(request, "New Board is added")
                return redirect(redirect_url)
            else:
                return redirect('addboard')
        else:
            messages.success(request, "Enter Board name")
            return redirect('addboard')

    elif request.method == "GET":
        return render(request, 'addboard.html')
    else:
        return redirect('home')


# function to get board id from url
def get_board_id(mixed_url):
    return (mixed_url.strip("/")).split("/")[1]


# @require_http_methods(["POST"])
def ajax_item_submit(request):
    # if request.is_ajax():
    #     title = request.POST.get('item')
    #     result = TodoList.objects.get(pk=101, userid=request.user.id)
    #     result.item = title
    #     result.save()
    #     message = "Item successfully updated"
    # else:
    message = "Not Ajax"
    return HttpResponse(message)