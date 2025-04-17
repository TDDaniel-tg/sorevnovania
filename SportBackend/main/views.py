from django.shortcuts import render

def home(request):
    return render(request, 'main/index.html')

def male_standards(request):
    standards = [
        {
            'title': 'Про жим лежа софт экипировка однопетельная',
            'image': 'images/Про, жим лежа софт экипировка однопетельная муж.jpg',
            'description': 'Профессиональная дисциплина жима лежа с использованием софт экипировки однопетельного типа. Требует высокой техники выполнения и специальной подготовки.',
            'is_pro': True,
            'difficulty': 'Продвинутый уровень',
            'categories': [
                {'weight': 'До 59 кг', 'norm': 120},
                {'weight': 'До 66 кг', 'norm': 130},
                {'weight': 'До 74 кг', 'norm': 140},
                {'weight': 'До 83 кг', 'norm': 150},
                {'weight': 'До 93 кг', 'norm': 160},
                {'weight': 'До 105 кг', 'norm': 170},
                {'weight': 'До 120 кг', 'norm': 180},
                {'weight': 'Свыше 120 кг', 'norm': 190},
            ]
        },
        {
            'title': 'Про народный бицепс',
            'image': 'images/Про, народный бицепс муж.jpg',
            'description': 'Профессиональная дисциплина подъема штанги на бицепс. Требует точной техники и контроля движения.',
            'is_pro': True,
            'difficulty': 'Продвинутый уровень',
            'categories': [
                {'weight': 'До 59 кг', 'norm': 80},
                {'weight': 'До 66 кг', 'norm': 85},
                {'weight': 'До 74 кг', 'norm': 90},
                {'weight': 'До 83 кг', 'norm': 95},
                {'weight': 'До 93 кг', 'norm': 100},
                {'weight': 'До 105 кг', 'norm': 105},
                {'weight': 'До 120 кг', 'norm': 110},
                {'weight': 'Свыше 120 кг', 'norm': 115},
            ]
        },
        {
            'title': 'Про строгий подъем на бицепс',
            'image': 'images/Про, строгий подьем на бицепс муж.jpg',
            'description': 'Профессиональная дисциплина строгого подъема штанги на бицепс. Требует идеальной техники и полного контроля движения.',
            'is_pro': True,
            'difficulty': 'Продвинутый уровень',
            'categories': [
                {'weight': 'До 59 кг', 'norm': 70},
                {'weight': 'До 66 кг', 'norm': 75},
                {'weight': 'До 74 кг', 'norm': 80},
                {'weight': 'До 83 кг', 'norm': 85},
                {'weight': 'До 93 кг', 'norm': 90},
                {'weight': 'До 105 кг', 'norm': 95},
                {'weight': 'До 120 кг', 'norm': 100},
                {'weight': 'Свыше 120 кг', 'norm': 105},
            ]
        },
        {
            'title': 'Про силовое двоеборье',
            'image': 'images/Про, силовое двоеборье муж.jpg',
            'description': 'Профессиональная дисциплина, включающая жим лежа и становую тягу. Требует комплексной подготовки и выносливости.',
            'is_pro': True,
            'difficulty': 'Продвинутый уровень',
            'categories': [
                {'weight': 'До 59 кг', 'norm': 300},
                {'weight': 'До 66 кг', 'norm': 320},
                {'weight': 'До 74 кг', 'norm': 340},
                {'weight': 'До 83 кг', 'norm': 360},
                {'weight': 'До 93 кг', 'norm': 380},
                {'weight': 'До 105 кг', 'norm': 400},
                {'weight': 'До 120 кг', 'norm': 420},
                {'weight': 'Свыше 120 кг', 'norm': 440},
            ]
        },
        {
            'title': 'Про становая тяга без экип',
            'image': 'images/Про, становая тяга без экип муж.jpg',
            'description': 'Профессиональная дисциплина становой тяги без использования экипировки. Требует отличной техники и силы.',
            'is_pro': True,
            'difficulty': 'Продвинутый уровень',
            'categories': [
                {'weight': 'До 59 кг', 'norm': 200},
                {'weight': 'До 66 кг', 'norm': 220},
                {'weight': 'До 74 кг', 'norm': 240},
                {'weight': 'До 83 кг', 'norm': 260},
                {'weight': 'До 93 кг', 'norm': 280},
                {'weight': 'До 105 кг', 'norm': 300},
                {'weight': 'До 120 кг', 'norm': 320},
                {'weight': 'Свыше 120 кг', 'norm': 340},
            ]
        },
        {
            'title': 'Про военный народный жим',
            'image': 'images/Про, военный народный жим муж.jpg',
            'description': 'Профессиональная дисциплина военного жима. Требует специальной подготовки и техники выполнения.',
            'is_pro': True,
            'difficulty': 'Продвинутый уровень',
            'categories': [
                {'weight': 'До 59 кг', 'norm': 90},
                {'weight': 'До 66 кг', 'norm': 95},
                {'weight': 'До 74 кг', 'norm': 100},
                {'weight': 'До 83 кг', 'norm': 105},
                {'weight': 'До 93 кг', 'norm': 110},
                {'weight': 'До 105 кг', 'norm': 115},
                {'weight': 'До 120 кг', 'norm': 120},
                {'weight': 'Свыше 120 кг', 'norm': 125},
            ]
        },
        {
            'title': 'Про жим лежа без экип',
            'image': 'images/Про жим лежа, без экип муж.jpg',
            'description': 'Профессиональная дисциплина жима лежа без использования экипировки. Требует чистой техники и силы.',
            'is_pro': True,
            'difficulty': 'Продвинутый уровень',
            'categories': [
                {'weight': 'До 59 кг', 'norm': 110},
                {'weight': 'До 66 кг', 'norm': 120},
                {'weight': 'До 74 кг', 'norm': 130},
                {'weight': 'До 83 кг', 'norm': 140},
                {'weight': 'До 93 кг', 'norm': 150},
                {'weight': 'До 105 кг', 'norm': 160},
                {'weight': 'До 120 кг', 'norm': 170},
                {'weight': 'Свыше 120 кг', 'norm': 180},
            ]
        },
        {
            'title': 'Военный жим',
            'image': 'images/военный.jpg',
            'description': 'Классическая дисциплина военного жима. Требует хорошей техники и контроля.',
            'is_pro': False,
            'difficulty': 'Базовый уровень',
            'categories': [
                {'weight': 'До 59 кг', 'norm': 80},
                {'weight': 'До 66 кг', 'norm': 85},
                {'weight': 'До 74 кг', 'norm': 90},
                {'weight': 'До 83 кг', 'norm': 95},
                {'weight': 'До 93 кг', 'norm': 100},
                {'weight': 'До 105 кг', 'norm': 105},
                {'weight': 'До 120 кг', 'norm': 110},
                {'weight': 'Свыше 120 кг', 'norm': 115},
            ]
        },
        {
            'title': 'Становая тяга без экип',
            'image': 'images/становая тяга без экип муж.jpg',
            'description': 'Классическая дисциплина становой тяги без экипировки. Требует правильной техники и базовой силы.',
            'is_pro': False,
            'difficulty': 'Базовый уровень',
            'categories': [
                {'weight': 'До 59 кг', 'norm': 180},
                {'weight': 'До 66 кг', 'norm': 200},
                {'weight': 'До 74 кг', 'norm': 220},
                {'weight': 'До 83 кг', 'norm': 240},
                {'weight': 'До 93 кг', 'norm': 260},
                {'weight': 'До 105 кг', 'norm': 280},
                {'weight': 'До 120 кг', 'norm': 300},
                {'weight': 'Свыше 120 кг', 'norm': 320},
            ]
        },
        {
            'title': 'Силовое двоеборье',
            'image': 'images/силовое двоеборье муж.jpg',
            'description': 'Классическая дисциплина, включающая жим лежа и становую тягу. Требует базовой подготовки.',
            'is_pro': False,
            'difficulty': 'Базовый уровень',
            'categories': [
                {'weight': 'До 59 кг', 'norm': 250},
                {'weight': 'До 66 кг', 'norm': 270},
                {'weight': 'До 74 кг', 'norm': 290},
                {'weight': 'До 83 кг', 'norm': 310},
                {'weight': 'До 93 кг', 'norm': 330},
                {'weight': 'До 105 кг', 'norm': 350},
                {'weight': 'До 120 кг', 'norm': 370},
                {'weight': 'Свыше 120 кг', 'norm': 390},
            ]
        },
        {
            'title': 'Строгий подъем на бицепс любители',
            'image': 'images/строгий подъем на бицепс любители муж.jpg',
            'description': 'Дисциплина для любителей строгого подъема штанги на бицепс. Требует базовой техники.',
            'is_pro': False,
            'difficulty': 'Базовый уровень',
            'categories': [
                {'weight': 'До 59 кг', 'norm': 60},
                {'weight': 'До 66 кг', 'norm': 65},
                {'weight': 'До 74 кг', 'norm': 70},
                {'weight': 'До 83 кг', 'norm': 75},
                {'weight': 'До 93 кг', 'norm': 80},
                {'weight': 'До 105 кг', 'norm': 85},
                {'weight': 'До 120 кг', 'norm': 90},
                {'weight': 'Свыше 120 кг', 'norm': 95},
            ]
        },
        {
            'title': 'Народный бицепс про',
            'image': 'images/народный бицепс про муж.jpg',
            'description': 'Профессиональная дисциплина народного бицепса. Требует продвинутой техники.',
            'is_pro': True,
            'difficulty': 'Продвинутый уровень',
            'categories': [
                {'weight': 'До 59 кг', 'norm': 70},
                {'weight': 'До 66 кг', 'norm': 75},
                {'weight': 'До 74 кг', 'norm': 80},
                {'weight': 'До 83 кг', 'norm': 85},
                {'weight': 'До 93 кг', 'norm': 90},
                {'weight': 'До 105 кг', 'norm': 95},
                {'weight': 'До 120 кг', 'norm': 100},
                {'weight': 'Свыше 120 кг', 'norm': 105},
            ]
        },
        {
            'title': 'Жим лежа софт экип',
            'image': 'images/жим лежа софт экип муж.jpg',
            'description': 'Дисциплина жима лежа с использованием софт экипировки. Требует базовой подготовки.',
            'is_pro': False,
            'difficulty': 'Базовый уровень',
            'categories': [
                {'weight': 'До 59 кг', 'norm': 100},
                {'weight': 'До 66 кг', 'norm': 110},
                {'weight': 'До 74 кг', 'norm': 120},
                {'weight': 'До 83 кг', 'norm': 130},
                {'weight': 'До 93 кг', 'norm': 140},
                {'weight': 'До 105 кг', 'norm': 150},
                {'weight': 'До 120 кг', 'norm': 160},
                {'weight': 'Свыше 120 кг', 'norm': 170},
            ]
        },
        {
            'title': 'Народный жим',
            'image': 'images/народный жим муж.jpg',
            'description': 'Классическая дисциплина народного жима. Требует базовой техники.',
            'is_pro': False,
            'difficulty': 'Базовый уровень',
            'categories': [
                {'weight': 'До 59 кг', 'norm': 80},
                {'weight': 'До 66 кг', 'norm': 85},
                {'weight': 'До 74 кг', 'norm': 90},
                {'weight': 'До 83 кг', 'norm': 95},
                {'weight': 'До 93 кг', 'norm': 100},
                {'weight': 'До 105 кг', 'norm': 105},
                {'weight': 'До 120 кг', 'norm': 110},
                {'weight': 'Свыше 120 кг', 'norm': 115},
            ]
        },
        {
            'title': 'Армлифтинг',
            'image': 'images/Армлифтинг муж.jpg',
            'description': 'Специализированная дисциплина армлифтинга. Требует специальной подготовки.',
            'is_pro': False,
            'difficulty': 'Специальная подготовка',
            'categories': [
                {'weight': 'До 59 кг', 'norm': 90},
                {'weight': 'До 66 кг', 'norm': 95},
                {'weight': 'До 74 кг', 'norm': 100},
                {'weight': 'До 83 кг', 'norm': 105},
                {'weight': 'До 93 кг', 'norm': 110},
                {'weight': 'До 105 кг', 'norm': 115},
                {'weight': 'До 120 кг', 'norm': 120},
                {'weight': 'Свыше 120 кг', 'norm': 125},
            ]
        },
    ]
    return render(request, 'main/male.html', {'standards': standards})

def female_standards(request):
    standards = [
        # Аналогичный список нормативов для женщин
    ]
    return render(request, 'main/female.html', {'standards': standards})

def disciplines(request):
    return render(request, 'main/disciplin.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html') 