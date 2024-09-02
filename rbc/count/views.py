from django.shortcuts import render
from .forms import ageeForm
import pickle
from sklearn.preprocessing import PolynomialFeatures

with open("C:/Users/SURENDHAN/Downloads/All Files & Datasets/rbcmodel.pkl", 'rb') as file:
    model = pickle.load(file)

degree = 8
poly = PolynomialFeatures(degree=degree)

def hi(request):
    result = None
    if request.method == 'POST':
        form = ageeForm(request.POST)
        if form.is_valid():
            agea = form.cleaned_data['age']
            transformed_input = poly.fit_transform([[agea]])
            result = model.predict(transformed_input)
            result = result[0]
            
        return render(request, 'count/index.html', {'form': form, 'result': result})
    else:
        form = ageeForm()
    return render(request, 'count/index.html', {'form': form, 'result': result})
