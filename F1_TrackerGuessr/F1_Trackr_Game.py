from js import console,document
import random
print("Hello World from the Web")

last_coords = None          # (lat, lon)
click_history = []          # [(lat, lon), (lat, lon), ...]

def process_coords(lat, lon):
    """Called from JS on every map click."""
    global last_coords
    last_coords = (float(lat), float(lon))
    click_history.append(last_coords)

# helpers you can call later from Python or JS
def get_last_coords():
    return last_coords               # e.g., (38.272689, 50.097656)

def get_click_history():
    return click_history[:]          # shallow copy

def clear_coords():
    global last_coords, click_history
    last_coords = None
    click_history = []


#list of images
images = [
    "images/Turn14_AbuDhabi.png",
    "images/CanadaGP.png",
    "images/yas_marina.jpg"
]
#these coordinates line up with the images list respective indexes
coordinates = [
    "24°28'04\"N 54°36'22\"E",
    "37°51'04\"S 144°58'13\"E"
    "24°28'43\"N 54°36'19\"E"


]

def process_coords(lat, lon):
    """Called from JS on each click."""
    global last_coords
    last_coords = (float(lat), float(lon))
    click_history.append(last_coords)

    # optional UI/console
    console.log(f"[PY] stored: {last_coords}")
    el = document.getElementById("coords")
    if el:
        el.innerText = f"{last_coords[0]:.6f}, {last_coords[1]:.6f}"

def print_last_coords():
    if last_coords is None:
        console.log("[PY] no clicks yet")
    else:
        lat, lon = last_coords
        console.log(f"[PY] last_coords = {lat:.6f}, {lon:.6f}")

#creating a variable to display the image randomly picked from the images list
randomImg = random.choice(images)

#creating an index variable that mirrors the index number that the random image is representing
index = images.index(randomImg)

#this variable is used to get the coordinates which match the specific image used for the game
img_coords = coordinates[index]

def marker_coordinates(lat, lon):
    return lat, lon

def latlon_decimal_image(img_coords):
    #turning the string into a list with all the elements
    charCoor = list(img_coords)
    #creating a for loop to remove all elements that are NOT integers or spaces
    coorNewList = []
    for i in range(len(charCoor)):
        if charCoor[i].isdigit() or charCoor[i] == " ":
            coorNewList.append(charCoor[i])
        else: 
            continue
        #joining all the elements together to form a new string before turning it into a list with 2 elements
    coorNewString = "".join(coorNewList)
    LatLonList = coorNewString.split()
    #creating a function to convert each element in the list to a decimal degree
    def dms_to_dd(dms_str):
        d = int(dms_str[0:2])
        m = int(dms_str[2:4])
        s = int(dms_str[4:6])
        return d + m/60 + s/3600

    lat_dd = dms_to_dd(LatLonList[0])
    lon_dd = dms_to_dd(LatLonList[1])
   

    return lat_dd, lon_dd
    
print(latlon_decimal_image(coordinates[index]))
print_last_coords()

document.getElementById("random-img").src = randomImg

