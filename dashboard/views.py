from django.shortcuts import render, redirect
from .models import ConsumerBehavior
import joblib
from django.http import HttpResponse
import numpy as np

# Loading the trained model
pipe_lr = joblib.load(open('pkl model/adaboost.pkl', 'rb'))

def index(request):
    return render(request, 'dashboard/index.html')

def make_prediction(request):
    return render(request, 'dashboard/make_prediction.html')

def prediction_history(request):
    data = ConsumerBehavior.objects.all()
    context = {
        'data': data,
    }
    return render(request, 'dashboard/prediction_history.html', context)

def prediction(request):
    if request.method == 'POST':
        # Collect all form data
        form_data = {
            'gender': request.POST.get('gender'),
            'age': request.POST.get('age'),
            'ethnic': request.POST.get('ethnic'),
            'occupation': request.POST.get('occupation'),
            'income': request.POST.get('income'),
            'use_social_media': request.POST.get('use_social_media'),
            'experience_purchasing': request.POST.get('experience_purchasing'),
            'reviews_affect': request.POST.get('reviews_affect'),
            'internet_hours': request.POST.get('internet_hours'),
            'attention_ads': request.POST.get('attention_ads'),
            'PB1': request.POST.get('PB1'),
            'PB2': request.POST.get('PB2'),
            'PB3': request.POST.get('PB3'),
            'PB4': request.POST.get('PB4'),
            'ATTD1': request.POST.get('ATTD1'),
            'ATTD2': request.POST.get('ATTD2'),
            'ATTD3': request.POST.get('ATTD3'),
            'ATTD4': request.POST.get('ATTD4'),
            'SN1': request.POST.get('SN1'),
            'SN2': request.POST.get('SN2'),
            'SN3': request.POST.get('SN3'),
            'SN4': request.POST.get('SN4'),
            'PBC1': request.POST.get('PBC1'),
            'PBC2': request.POST.get('PBC2'),
            'PBC3': request.POST.get('PBC3'),
            'PBC4': request.POST.get('PBC4')
        }

        # Ensure all form data is valid (not None)
        for key, value in form_data.items():
            if value is None:
                return HttpResponse(f"Form field '{key}' is missing.", status=400)

        # Convert applicable form data to integers
        try:
            numerical_data = [
                int(form_data['ATTD1']), int(form_data['ATTD2']), int(form_data['ATTD3']), int(form_data['ATTD4']),
                int(form_data['SN1']), int(form_data['SN2']), int(form_data['SN3']), int(form_data['SN4']),
                int(form_data['PBC1']), int(form_data['PBC2']), int(form_data['PBC3']), int(form_data['PBC4'])
            ]
        except ValueError:
            return HttpResponse("Form contains invalid data.", status=400)

        # Ensure numerical_data is in the correct shape (2D array with shape (1, num_features))
        numerical_data = np.array(numerical_data).reshape(1, -1)

        # Predict using the pipeline
        prediction = pipe_lr.predict(numerical_data)[0]

        # Get the probability estimates
        probability = pipe_lr.predict_proba(numerical_data)[0]

        # Assuming the model has two classes: 'high' and 'low'
        labels = pipe_lr.classes_
        probability_dict = {labels[i]: probability[i] for i in range(len(labels))}
        prediction_confidence = probability_dict[prediction]

        # Save the form data and prediction result
        behavior = ConsumerBehavior(**form_data)
        behavior.prediction = prediction
        behavior.prediction_confidence = prediction_confidence
        behavior.save()

        context = {
            'form_data': form_data,
            'labels': labels,
            'probability_dict': probability_dict,
            'prediction': prediction,
            'prediction_confidence': prediction_confidence,
        }
        return render(request, 'dashboard/prediction.html', context)
    

def feedback(request):
    if request.method == 'POST':
        # saving predictions to the database
        behavior = ConsumerBehavior()  # Updated model reference
        behavior.gender = request.POST.get('gender')
        behavior.age = request.POST.get('age')
        behavior.ethnic = request.POST.get('ethnic')
        behavior.occupation = request.POST.get('occupation')
        behavior.income = request.POST.get('income')
        behavior.use_social_media = request.POST.get('use_social_media')
        behavior.experience_purchasing = request.POST.get('experience_purchasing')
        behavior.reviews_affect = request.POST.get('reviews_affect')
        behavior.internet_hours = request.POST.get('internet_hours')
        behavior.attention_ads = request.POST.get('attention_ads')
        behavior.PB1 = request.POST.get('PB1')
        behavior.PB2 = request.POST.get('PB2')
        behavior.PB3 = request.POST.get('PB3')
        behavior.PB4 = request.POST.get('PB4')
        behavior.ATTD1 = request.POST.get('ATTD1')
        behavior.ATTD2 = request.POST.get('ATTD2')
        behavior.ATTD3 = request.POST.get('ATTD3')
        behavior.ATTD4 = request.POST.get('ATTD4')
        behavior.SN1 = request.POST.get('SN1')
        behavior.SN2 = request.POST.get('SN2')
        behavior.SN3 = request.POST.get('SN3')
        behavior.SN4 = request.POST.get('SN4')
        behavior.PBC1 = request.POST.get('PBC1')
        behavior.PBC2 = request.POST.get('PBC2')
        behavior.PBC3 = request.POST.get('PBC3')
        behavior.PBC4 = request.POST.get('PBC4')
       
        behavior.save()

        return redirect('make-prediction')