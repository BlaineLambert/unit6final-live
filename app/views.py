from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from app.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from app import models
from .forms import *



# Create your views here.
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form': form}
    return render(request, 'register.html', context)



def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password incorrect')
    return render(request, 'login.html')



def logout_func(request):
    logout(request)
    return redirect('login')



@login_required(login_url='login')
def filter(request, item):
    cities_for_states = [
        "Birmingham", "Montgomery", "Mobile",
        "Anchorage", "Fairbanks", "Juneau",
        "Phoenix", "Tucson", "Mesa",
        "Little Rock", "Fort Smith", "Fayetteville",
        "Los Angeles", "San Francisco", "San Diego",
        "Denver", "Colorado Springs", "Aurora",
        "Bridgeport", "New Haven", "Hartford",
        "Wilmington", "Dover", "Newark",
        "Miami", "Tampa", "Orlando",
        "Atlanta", "Augusta", "Savannah",
        "Honolulu", "Hilo", "Kailua",
        "Boise", "Meridian", "Nampa",
        "Chicago", "Aurora", "Rockford",
        "Indianapolis", "Fort Wayne", "Evansville",
        "Des Moines", "Cedar Rapids", "Davenport",
        "Wichita", "Overland Park", "Kansas City",
        "Louisville", "Lexington", "Bowling Green",
        "New Orleans", "Baton Rouge", "Shreveport",
        "Portland", "Lewiston", "Bangor",
        "Baltimore", "Frederick", "Rockville",
        "Boston", "Worcester", "Springfield",
        "Detroit", "Grand Rapids", "Warren",
        "Minneapolis", "St. Paul", "Rochester",
        "Jackson", "Gulfport", "Southaven",
        "Kansas City", "St. Louis", "Springfield",
        "Billings", "Missoula", "Great Falls",
        "Omaha", "Lincoln", "Bellevue",
        "Las Vegas", "Henderson", "Reno",
        "Manchester", "Nashua", "Concord",
        "Newark", "Jersey City", "Paterson",
        "Albuquerque", "Las Cruces", "Rio Rancho",
        "New York City", "Buffalo", "Rochester",
        "Charlotte", "Raleigh", "Greensboro",
        "Fargo", "Bismarck", "Grand Forks",
        "Columbus", "Cleveland", "Cincinnati",
        "Oklahoma City", "Tulsa", "Norman",
        "Portland", "Eugene", "Salem",
        "Philadelphia", "Pittsburgh", "Allentown",
        "Providence", "Warwick", "Cranston",
        "Charleston", "Columbia", "North Charleston",
        "Sioux Falls", "Rapid City", "Aberdeen",
        "Nashville", "Memphis", "Knoxville",
        "Houston", "San Antonio", "Dallas",
        "Salt Lake City", "West Valley City", "Provo",
        "Burlington", "Essex", "South Burlington",
        "Virginia Beach", "Norfolk", "Chesapeake",
        "Seattle", "Spokane", "Tacoma",
        "Charleston", "Huntington", "Morgantown",
        "Milwaukee", "Madison", "Green Bay",
        "Cheyenne", "Casper", "Laramie"," Water valley"
        ]

    us_states = [
    'Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware',
    'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky',
    'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri',
    'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina',
    'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota',
    'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming'
    ]
    zip_codes = [
        "35203", "35211", "35222",
        "36104", "36108", "36116",
        "36602", "36605", "36608",
        "99501", "99503", "99507",
        "99701", "99703", "99709",
        "99801", "99824", "99811",
        "85003", "85007", "85013",
        "85701", "85705", "85712",
        "85201", "85205", "85210",
        "72201", "72205", "72209",
        "72901", "72903", "72908",
        "72701", "72703", "72704",
        "90001", "90012", "90024",
        "94102", "94110", "94117",
        "92101", "92109", "92120",
        "80202", "80205", "80210",
        "80903", "80907", "80910",
        "80010", "80012", "80017",
        "06601", "06604", "06610",
        "06501", "06504", "06510",
        "06101", "06105", "06112",
        "19801", "19803", "19808",
        "19901", "19903", "19904",
        "19702", "19711", "19713",
        "33101", "33125", "33133",
        "33602", "33606", "33611",
        "32801", "32803", "32806",
        "30301", "30310", "30319",
        "30901", "30904", "30906",
        "31401", "31405", "31419",
        "96801", "96813", "96817",
        "96720", "96725", "96740",
        "96734", "96740", "96744",
        "83702", "83704", "83709",
        "83642", "83646", "83687",
        "83651", "83686", "83687",
        "60601", "60610", "60618",
        "60502", "60505", "60506",
        "61101", "61104", "61109",
        "46201", "46205", "46222",
        "46802", "46804", "46805",
        "47708", "47710", "47713",
        "50309", "50312", "50321",
        "52401", "52402", "52405",
        "52801", "52803", "52806",
        "67202", "67206", "67213",
        "66204", "66207", "66212",
        "66101", "66104", "66109",
        "40202", "40205", "40210",
        "40502", "40505", "40508",
        "42101", "42103", "42104",
        "70112", "70119", "70124",
        "70802", "70805", "70809",
        "71101", "71104", "71105",
        "04101", "04103", "04105",
        "04240", "04252", "04256",
        "04401", "04402", "04412",
        "21201", "21209", "21218",
        "21701", "21703", "21704",
        "20850", "20852", "20854",
        "21201", "21209", "21218",
        "21701", "21703", "21704",
        "20850", "20852", "20854",
        "02108", "02110", "02116",
        "01602", "01604", "01606",
        "01101", "01105", "01107",
        "48201", "48205", "48212",
        "49503", "49504", "49506",
        "48089", "48091", "48092",
        "55401", "55403", "55408",
        "55101", "55103", "55105",
        "55901", "55902", "55904",
        "39201", "39202", "39203",
        "39501", "39503", "39507",
        "38671", "38672", "38654",
        "64101", "64110", "64118",
        "63101", "63110", "63118",
        "65802", "65804", "65807",
        "59101", "59102", "59105",
        "59801", "59802", "59803",
        "59401", "59404", "59405",
        "68102", "68104", "68106",
        "68502", "68504", "68506",
        "68123", "68147", "68157",
        "89101", "89109", "89117",
        "89002", "89011", "89012",
        "89501", "89509", "89512",
        "03101", "03103", "03104",
        "03060", "03062", "03063",
        "03301", "03303", "03304",
        "43201", "43204", "43206",
        "44102", "44105", "44113",
        "45202", "45206", "45211",
        "73102", "73103", "73107",
        "74103", "74105", "74112",
        "73069", "73071", "73072",
        "97201", "97205", "97209",
        "97401", "97403", "97405",
        "97301", "97302", "97305",
        "19102", "19103", "19106",
        "15201", "15203", "15206",
        "18101", "18103", "18104",
        "02903", "02904", "02906",
        "02886", "02888", "02889",
        "02910", "02920", "02921",
        "29401", "29403", "29407",
        "29201", "29203", "29205",
        "29405", "29406", "29418",
        "57103", "57104", "57105",
        "57701", "57702", "57703",
        "57401", "57402", "57401",
        "37201", "37203", "37206",
        "38103", "38104", "38111",
        "37902", "37909", "37912",
        "77002", "77004", "77007",
        "78201", "78205", "78209",
        "75201", "75204", "75209",
        "84101", "84102", "84105",
        "84119", "84120", "84128",
        "84601", "84604", "84606",
        "05401", "05403", "05408",
        "05452", "05446", "05453",
        "05403", "05405", "05407",
        "23451", "23452", "23456",
        "23502", "23503", "23505",
        "23320", "23321", "23322",
        "98101", "98103", "98105",
        "99201", "99202", "99205",
        "98402", "98403", "98405",
        "25301", "25302", "25303",
        "25701", "25702", "25703",
        "26501", "26505", "26508",
        "53202", "53203", "53207",
        "53703", "53705", "53706",
        "54301", "54303", "54311",
        "82001", "82002", "82007",
        "82601", "82604", "82609",
        "82070", "82071", "82072",
        "38965"
    ]

    if item in us_states:
        properties = filter_by_state(item)
        
    elif item in zip_codes:
        properties = filter_by_zip(item)
        
    elif item in cities_for_states:
        properties = filter_by_city(item)
        
    else:
        properties = filter_by_address(item)

    return properties



def booking(request, name):
    booked = booking_props(name)
    context = {'booked':booked}
    return render(request, 'userpage.html',context)



def homepage(request):
    if request.POST:
        if 'filterbtn' in request.POST:
            item = request.POST.get('filter')
            places = filter(request, item)
            context = {'places': places}
            return render(request, 'home.html', context)
    else:
        places = Properties.objects.all()
        context = {'places': places}
        return render(request, 'home.html', context)



@login_required(login_url='login')
def userpage(request):
    form = CreateAccount(initial={'user': request.user})
    if request.method == 'POST':
        if 'delete_property' in request.POST:
            property_id = request.POST['delete_property']
            property_to_delete = get_object_or_404(Properties, id=property_id, user_props=request.user.account)
            property_to_delete.delete()
            return redirect('user')
        if 'prop_sold' in request.POST:
            property_id = request.POST['prop_sold']
            property_to_sale = get_object_or_404(Properties, id=property_id, user_props=request.user.account)
            if property_to_sale.available == True:
                property_to_sale.available = False
                property_to_sale.save()
                return redirect('user')
            if property_to_sale.available == False:
                property_to_sale.available = True
                property_to_sale.save()
                return redirect('user')
        if 'create_account' in request.POST:
            form = CreateAccount(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('user')
            else:
                return redirect('home')
            
        else:
            user = request.user
            try:
                account = Account.objects.get(user = user.id)
                places = Properties.objects.filter(user_props = account)
            except Account.DoesNotExist:
                account = None
                places = None
            context = {'account': account, 'places': places, 'user': user}
            return render(request, 'userpage.html', context)
    else:
        user = request.user
        try:
            account = Account.objects.get(user = user.id)
            places = Properties.objects.filter(user_props = account)
        except Account.DoesNotExist:
            account = None
            places = None
        context = {'account': account, 'places': places, 'user': user, 'form': form}
        return render(request, 'userpage.html', context)



@login_required(login_url='login')
def add_property(request):
    form = AddProperty(initial={"user_props": request.user.account})
    if request.method == 'POST':
        form = AddProperty(request.POST, request.FILES)
        if form.is_valid():
            # form.user_props = request.user
            # form.price = request.POST.get('price')
            # form.address = request.POST.get('address')
            # form.city = request.POST.get('city')
            # form.zip_code = request.POST.get('zip_code')
            # form.size = request.POST.get('size')
            # form.available = request.POST.get('available')
            # form.picture = request.POST.get('picture')
            form.save()
            return redirect('home')
        else:
            return redirect('user')
    else:
        context = {'form': form}
        return render(request, 'add_property.html', context)



# us_states = [
#      'Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware',
#      'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky',
#      'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri',
#      'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina',
#      'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota',
#      'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming'
# ]



# state_abbreviations = [
#     'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA',
#     'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD',
#     'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ',
#     'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC',
#     'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY'
# ]



# cities_for_states = [
#      "Birmingham", "Montgomery", "Mobile",
#      "Anchorage", "Fairbanks", "Juneau",
#      "Phoenix", "Tucson", "Mesa",
#      "Little Rock", "Fort Smith", "Fayetteville",
#      "Los Angeles", "San Francisco", "San Diego",
#      "Denver", "Colorado Springs", "Aurora",
#      "Bridgeport", "New Haven", "Hartford",
#      "Wilmington", "Dover", "Newark",
#      "Miami", "Tampa", "Orlando",
#      "Atlanta", "Augusta", "Savannah",
#      "Honolulu", "Hilo", "Kailua",
#      "Boise", "Meridian", "Nampa",
#      "Chicago", "Aurora", "Rockford",
#      "Indianapolis", "Fort Wayne", "Evansville",
#      "Des Moines", "Cedar Rapids", "Davenport",
#      "Wichita", "Overland Park", "Kansas City",
#      "Louisville", "Lexington", "Bowling Green",
#      "New Orleans", "Baton Rouge", "Shreveport",
#      "Portland", "Lewiston", "Bangor",
#      "Baltimore", "Frederick", "Rockville",
#      "Boston", "Worcester", "Springfield",
#      "Detroit", "Grand Rapids", "Warren",
#      "Minneapolis", "St. Paul", "Rochester",
#      "Jackson", "Gulfport", "Southaven",
#      "Kansas City", "St. Louis", "Springfield",
#      "Billings", "Missoula", "Great Falls",
#      "Omaha", "Lincoln", "Bellevue",
#      "Las Vegas", "Henderson", "Reno",
#      "Manchester", "Nashua", "Concord",
#      "Newark", "Jersey City", "Paterson",
#      "Albuquerque", "Las Cruces", "Rio Rancho",
#      "New York City", "Buffalo", "Rochester",
#      "Charlotte", "Raleigh", "Greensboro",
#      "Fargo", "Bismarck", "Grand Forks",
#      "Columbus", "Cleveland", "Cincinnati",
#      "Oklahoma City", "Tulsa", "Norman",
#      "Portland", "Eugene", "Salem",
#      "Philadelphia", "Pittsburgh", "Allentown",
#      "Providence", "Warwick", "Cranston",
#      "Charleston", "Columbia", "North Charleston",
#      "Sioux Falls", "Rapid City", "Aberdeen",
#      "Nashville", "Memphis", "Knoxville",
#      "Houston", "San Antonio", "Dallas",
#      "Salt Lake City", "West Valley City", "Provo",
#      "Burlington", "Essex", "South Burlington",
#      "Virginia Beach", "Norfolk", "Chesapeake",
#      "Seattle", "Spokane", "Tacoma",
#      "Charleston", "Huntington", "Morgantown",
#      "Milwaukee", "Madison", "Green Bay",
#      "Cheyenne", "Casper", "Laramie"
#     ]



# zip_codes = [
#     "35203", "35211", "35222",
#     "36104", "36108", "36116",
#     "36602", "36605", "36608",
#     "99501", "99503", "99507",
#     "99701", "99703", "99709",
#     "99801", "99824", "99811",
#     "85003", "85007", "85013",
#     "85701", "85705", "85712",
#     "85201", "85205", "85210",
#     "72201", "72205", "72209",
#     "72901", "72903", "72908",
#     "72701", "72703", "72704",
#     "90001", "90012", "90024",
#     "94102", "94110", "94117",
#     "92101", "92109", "92120",
#     "80202", "80205", "80210",
#     "80903", "80907", "80910",
#     "80010", "80012", "80017",
#     "06601", "06604", "06610",
#     "06501", "06504", "06510",
#     "06101", "06105", "06112",
#     "19801", "19803", "19808",
#     "19901", "19903", "19904",
#     "19702", "19711", "19713",
#     "33101", "33125", "33133",
#     "33602", "33606", "33611",
#     "32801", "32803", "32806",
#     "30301", "30310", "30319",
#     "30901", "30904", "30906",
#     "31401", "31405", "31419",
#     "96801", "96813", "96817",
#     "96720", "96725", "96740",
#     "96734", "96740", "96744",
#     "83702", "83704", "83709",
#     "83642", "83646", "83687",
#     "83651", "83686", "83687",
#     "60601", "60610", "60618",
#     "60502", "60505", "60506",
#     "61101", "61104", "61109",
#     "46201", "46205", "46222",
#     "46802", "46804", "46805",
#     "47708", "47710", "47713",
#     "50309", "50312", "50321",
#     "52401", "52402", "52405",
#     "52801", "52803", "52806",
#     "67202", "67206", "67213",
#     "66204", "66207", "66212",
#     "66101", "66104", "66109",
#     "40202", "40205", "40210",
#     "40502", "40505", "40508",
#     "42101", "42103", "42104",
#     "70112", "70119", "70124",
#     "70802", "70805", "70809",
#     "71101", "71104", "71105",
#     "04101", "04103", "04105",
#     "04240", "04252", "04256",
#     "04401", "04402", "04412",
#     "21201", "21209", "21218",
#     "21701", "21703", "21704",
#     "20850", "20852", "20854",
#     "21201", "21209", "21218",
#     "21701", "21703", "21704",
#     "20850", "20852", "20854",
#     "02108", "02110", "02116",
#     "01602", "01604", "01606",
#     "01101", "01105", "01107",
#     "48201", "48205", "48212",
#     "49503", "49504", "49506",
#     "48089", "48091", "48092",
#     "55401", "55403", "55408",
#     "55101", "55103", "55105",
#     "55901", "55902", "55904",
#     "39201", "39202", "39203",
#     "39501", "39503", "39507",
#     "38671", "38672", "38654",
#     "64101", "64110", "64118",
#     "63101", "63110", "63118",
#     "65802", "65804", "65807",
#     "59101", "59102", "59105",
#     "59801", "59802", "59803",
#     "59401", "59404", "59405",
#     "68102", "68104", "68106",
#     "68502", "68504", "68506",
#     "68123", "68147", "68157",
#     "89101", "89109", "89117",
#     "89002", "89011", "89012",
#     "89501", "89509", "89512",
#     "03101", "03103", "03104",
#     "03060", "03062", "03063",
#     "03301", "03303", "03304",
#     "43201", "43204", "43206",
#     "44102", "44105", "44113",
#     "45202", "45206", "45211",
#     "73102", "73103", "73107",
#     "74103", "74105", "74112",
#     "73069", "73071", "73072",
#     "97201", "97205", "97209",
#     "97401", "97403", "97405",
#     "97301", "97302", "97305",
#     "19102", "19103", "19106",
#     "15201", "15203", "15206",
#     "18101", "18103", "18104",
#     "02903", "02904", "02906",
#     "02886", "02888", "02889",
#     "02910", "02920", "02921",
#     "29401", "29403", "29407",
#     "29201", "29203", "29205",
#     "29405", "29406", "29418",
#     "57103", "57104", "57105",
#     "57701", "57702", "57703",
#     "57401", "57402", "57401",
#     "37201", "37203", "37206",
#     "38103", "38104", "38111",
#     "37902", "37909", "37912",
#     "77002", "77004", "77007",
#     "78201", "78205", "78209",
#     "75201", "75204", "75209",
#     "84101", "84102", "84105",
#     "84119", "84120", "84128",
#     "84601", "84604", "84606",
#     "05401", "05403", "05408",
#     "05452", "05446", "05453",
#     "05403", "05405", "05407",
#     "23451", "23452", "23456",
#     "23502", "23503", "23505",
#     "23320", "23321", "23322",
#     "98101", "98103", "98105",
#     "99201", "99202", "99205",
#     "98402", "98403", "98405",
#     "25301", "25302", "25303",
#     "25701", "25702", "25703",
#     "26501", "26505", "26508",
#     "53202", "53203", "53207",
#     "53703", "53705", "53706",
#     "54301", "54303", "54311",
#     "82001", "82002", "82007",
#     "82601", "82604", "82609",
#     "82070", "82071", "82072",
#  ]
