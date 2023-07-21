from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def nosotros (request):
    return render(request, 'nosotros.html', {
        "saludo": "Bienvenido al Blog",
        "texto": "Somos un grupo de personas interesadas en compartir información sobre economía financiera. El hoy requiere introducirse en el mundo de las finanzas, aprender sobre los aspectos que generan posibilidades de inversión. Aquí encontrarás información actualizada, y una mirada holística que ayudará a insertarte en el ámbito financiero, trazar y alcanzar tus objetivos de corto y largo plazo.",
        "autor":"Grupo 'Economía Financiera'"
    })
    
