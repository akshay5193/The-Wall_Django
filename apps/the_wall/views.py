from django.shortcuts import render, redirect, HttpResponse
from apps.login_reg.models import User
from .models import Post, Comment


def wall_index(request):
    if request.session.get('user_id'):
        current_user = User.objects.get(id=request.session.get('user_id'))
        context = {
            'user_first_name': current_user.first_name,
            'all_posts': Post.objects.all(),
            'all_comments': Comment.objects.all(),
            'current_user_posts': Post.objects.filter(user_id=current_user.id),
            'current_user_id': current_user.id,
            'current_user_comments': Comment.objects.filter(user_id=current_user.id)
            # 'post_comments': Comment.objects.filter(post_id=user_posts)
        }

        return render(request, "the_wall/wall_index.html", context)
    return redirect('/')

    # if request.session.get('user_id'):
    #     current_user = User.objects.get(id=request.session['user_id'])
    #     context = {
    #         'user_first_name': current_user.first_name,
    #         'all_posts': Post.objects.all(),
    #         "current_user_id": current_user.id,
    #     }
    #     return render(request, 'the_wall/wall_index.html', context)
    # return redirect('/')


def logout(request):
    request.session.clear()
    return redirect('/')


def create_post(request):
    current_user = User.objects.get(id=request.session.get('user_id'))
    post = Post.objects.create(
        post_content=request.POST['post_content'], user_id=current_user.id)

    print(post)

    return redirect('/wall')


def add_comment(request, post_id):
    current_user = User.objects.get(id=request.session.get('user_id'))
    print(current_user.id)
    current_post = Post.objects.get(id=post_id)
    print(current_post.id)
    user_comment = Comment.objects.create(
        comment_content=request.POST['comment-text'], user=current_user, post_id=current_post.id)

    # print(user_comment.id, user_comment.comment_content,user_comment.post.id, user_comment.users.id)

    return redirect('/wall')


def delete_comment(request, comment_id):
    # comment_to_delete = Comment.objects.get(id=request.POST['comment_id'][0])
    # print(comment_to_delete)
    # comment_to_delete.delete()

    comment_to_delete = Comment.objects.get(id=comment_id)
    comment_to_delete.delete()

    return redirect('/wall')


def delete_post(request):
    post_to_delete = Post.objects.get(id=request.POST['post_id'][0])
    # print(post_to_delete)
    post_to_delete.delete()

    return redirect('/wall')
