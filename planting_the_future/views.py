from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from .models import PlantedTree
from .forms import PlantedTreeForm
from rest_framework import generics
from .serializers import PlantedTreeSerializer
from rest_framework.permissions import IsAuthenticated

def user_planted_trees(request):
    # View to list all trees planted by the current user
    if not request.user.is_authenticated:
        return HttpResponseForbidden()
    
    planted_trees = PlantedTree.objects.filter(user=request.user)
    return render(request, 'user_planted_trees.html', {'planted_trees': planted_trees})

def planted_tree_detail(request, tree_id):
    # View to display the details of a specific planted tree
    planted_tree = get_object_or_404(PlantedTree, id=tree_id)
    return render(request, 'planted_tree_detail.html', {'planted_tree': planted_tree})

def add_planted_tree(request):
    # View to add a new planted tree
    if not request.user.is_authenticated:
        return HttpResponseForbidden()

    if request.method == 'POST':
        form = PlantedTreeForm(request.POST)
        if form.is_valid():
            planted_tree = form.save(commit=False)
            planted_tree.user = request.user
            planted_tree.save()
            return redirect('user_planted_trees')
    else:
        form = PlantedTreeForm()
    
    return render(request, 'add_planted_tree.html', {'form': form})

def account_planted_trees(request):
    # View to list all trees planted associated with the current user's accounts
    if not request.user.is_authenticated:
        return HttpResponseForbidden()

    accounts = request.user.accounts.all()
    planted_trees = PlantedTree.objects.filter(account__in=accounts)
    return render(request, 'account_planted_trees.html', {'planted_trees': planted_trees})

class UserPlantedTreesView(generics.ListAPIView):
    # API view to list all trees planted by the authenticated user
    serializer_class = PlantedTreeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PlantedTree.objects.filter(user=self.request.user)
