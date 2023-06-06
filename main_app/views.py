from django.shortcuts import render

finches = [
    {
        "name": "Ruby",
        "breed": "Zebra Finch",
        "description": "Ruby is a lively and social finch with beautiful markings.",
        "age": 2
    },
    {
        "name": "Sunny",
        "breed": "Gouldian Finch",
        "description": "Sunny is a colorful finch known for its vibrant plumage.",
        "age": 1
    },
    {
        "name": "Charlie",
        "breed": "Bengalese Finch",
        "description": "Charlie is a small and energetic finch that loves to sing.",
        "age": 3
    }
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {
        'finches': finches
    })