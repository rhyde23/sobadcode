#Reggie Hyde

#Libraries
import pygame, pickle, random
from os import listdir

#Imports of other functions I will need from the project
from file_path_converter import convert_path
from schedule import get_schedule
from schedule import get_games_in_a_month
from months_in_order import get_month_number
from months_in_order import get_days_in_a_month
from months_in_order import get_number_month
from team_rating_calculator import calculate_rating
from match_sim_calculator import  match_sim
from goals_randomizer import randomize_goals
from randomize_realistic_minutes import randomize_goals_minutes

#The "pi" variable just represents whether or not the script is running on Linux
pi = False

#Initialize pygame and pygame fonts
pygame.init()
pygame.font.init()

#Define fonts
myfont = pygame.font.SysFont('Currier', 25)
myfont2 = pygame.font.SysFont('Currier', 50)
myfont3 = pygame.font.SysFont('Currier', 15)
myfont4 = pygame.font.SysFont('Currier', 20)

#Display width
display_width = 792
half = int(display_width/2)

#Set up display
display = pygame.display.set_mode((display_width, 612))
pygame.display.set_caption('Project')

#Define RGB Color Codes
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
key_color = (58, 166, 221)
gray = (229, 229, 229, 255)
light_blue = (58, 166, 221, 255)

#The "teams_in_league" array contains all of the teams in alphabetical order
teams_in_league = [
    'Arsenal',
    'Aston Villa',
    'Brighton & Hove Albion',
    'Burnley',
    'Chelsea',
    'Crystal Palace',
    'Everton',
    'Fulham',
    'Leeds United',
    'Leicester City',
    'Liverpool',
    'Manchester City',
    'Manchester United',
    'Newcastle United',
    'Sheffield United',
    'Southampton',
    'Tottenham Hotspur',
    'West Bromwich Albion',
    'West Ham United',
    'Wolverhampton Wanderers'
]


#######################################################################################################################################

#Saves Screen Stuff

#######################################################################################################################################

#The "save_number" is the variable that dictates which save the user is hovering over
save_number = 0

#Function that loads the save screen given the save number
def get_save_image(save_number) :
    path = ''.join(['C:\\Users\\rhyde23\\Desktop\\Project\\Images\\', 'Save', str(save_number), '.png'])
    if pi :
        path = convert_path(path)
    return pygame.image.load(path).convert()

#The "save_background_images" array is an array of loaded images that will light up each save button when the mouse is over it
save_background_images = []
for i in range(10) :
    current_save_image = get_save_image(i+1)
    save_background_images.append(current_save_image)

#The current image from "save_background_images"
current_save_image = save_background_images[save_number]

#Same basic concept of loading saves, but this time it's loading the basic information for each save like the save name
save_names = []
for i in range(10) :
    path = ''.join(['C:\\Users\\rhyde23\\Desktop\\Project\\Saves\\', 'File', str(i+1), 'BasicInfo.dat'])
    if pi :
        path = convert_path(path)
    basic_info = pickle.load(open(path, 'rb'))
    save_names.append(basic_info['SaveName'])

#Render the fonts for each button 
save_names_texts = []
for save_name in save_names :
    save_names_texts.append(myfont.render(save_name, True, (0, 0, 0)))

#"clicker_mode" indicates the coordinates of where the user clicked, I used this for early development
clicker_mode = False
current_clicked = (0, 0)

#Forming the array "buttons", which is an array of the y coordinates that dictates whether the user is hovering over a button
y_difference = 37
x_start, x_end = 43, 761
buttons = []
for i in range(10) :
    first_y = 154+(i*y_difference)
    second_y = first_y+y_difference
    buttons.append([first_y, second_y])

#"offset" is to make the y coordinates of text centered
offset = [12, 13, 14, 16, 17, 19, 20, 22, 23, 25]

#"save_selected" is final variable of this screen, and it's set to None right now
save_selected = None

#######################################################################################################################################

#Name Save Stuff

#IMPORTANT NOTE: THIS LOOP CONTROLS THE USER INPUT FOR THE NAME OF THE SAVE AND THE MANAGER NAME

#######################################################################################################################################


#The "keyboard_order" dictionary loads all of the images that light up the keys on the virtual keyboard 
if not pi :
    keyboard_order = {
        pygame.K_m:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-002.png').convert(),
        pygame.K_n:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-003.png').convert(),
        pygame.K_b:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-004.png').convert(),
        pygame.K_v:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-005.png').convert(),
        pygame.K_c:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-006.png').convert(),
        pygame.K_x:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-007.png').convert(),
        pygame.K_z:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-008.png').convert(),
        pygame.K_l:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-009.png').convert(),
        pygame.K_k:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-010.png').convert(),
        pygame.K_j:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-011.png').convert(),
        pygame.K_h:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-012.png').convert(),
        pygame.K_g:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-013.png').convert(),
        pygame.K_f:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-014.png').convert(),
        pygame.K_d:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-015.png').convert(),
        pygame.K_s:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-016.png').convert(),
        pygame.K_a:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-017.png').convert(),
        pygame.K_p:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-018.png').convert(),
        pygame.K_o:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-019.png').convert(),
        pygame.K_i:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-020.png').convert(),
        pygame.K_u:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-021.png').convert(),
        pygame.K_y:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-022.png').convert(),
        pygame.K_t:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-023.png').convert(),
        pygame.K_r:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-024.png').convert(),
        pygame.K_e:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-025.png').convert(),
        pygame.K_w:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-026.png').convert(),
        pygame.K_q:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-027.png').convert(),
        pygame.K_BACKSPACE:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-028.png').convert(),
        pygame.K_0:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-029.png').convert(),
        pygame.K_9:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-030.png').convert(),
        pygame.K_8:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-031.png').convert(),
        pygame.K_7:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-032.png').convert(),
        pygame.K_6:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-033.png').convert(),
        pygame.K_5:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-034.png').convert(),
        pygame.K_4:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-035.png').convert(),
        pygame.K_3:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-036.png').convert(),
        pygame.K_2:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-037.png').convert(),
        pygame.K_1:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-038.png').convert(),
    }
    
if pi :
    keyboard_order = {
        pygame.K_m:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-002.png')).convert(),
        pygame.K_n:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-003.png')).convert(),
        pygame.K_b:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-004.png')).convert(),
        pygame.K_v:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-005.png')).convert(),
        pygame.K_c:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-006.png')).convert(),
        pygame.K_x:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-007.png')).convert(),
        pygame.K_z:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-008.png')).convert(),
        pygame.K_l:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-009.png')).convert(),
        pygame.K_k:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-010.png')).convert(),
        pygame.K_j:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-011.png')).convert(),
        pygame.K_h:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-012.png')).convert(),
        pygame.K_g:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-013.png')).convert(),
        pygame.K_f:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-014.png')).convert(),
        pygame.K_d:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-015.png')).convert(),
        pygame.K_s:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-016.png')).convert(),
        pygame.K_a:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-017.png')).convert(),
        pygame.K_p:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-018.png')).convert(),
        pygame.K_o:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-019.png')).convert(),
        pygame.K_i:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-020.png')).convert(),
        pygame.K_u:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-021.png')).convert(),
        pygame.K_y:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-022.png')).convert(),
        pygame.K_t:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-023.png')).convert(),
        pygame.K_r:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-024.png')).convert(),
        pygame.K_e:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-025.png')).convert(),
        pygame.K_w:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-026.png')).convert(),
        pygame.K_q:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-027.png')).convert(),
        pygame.K_BACKSPACE:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-028.png')).convert(),
        pygame.K_0:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-029.png')).convert(),
        pygame.K_9:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-030.png')).convert(),
        pygame.K_8:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-031.png')).convert(),
        pygame.K_7:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-032.png')).convert(),
        pygame.K_6:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-033.png')).convert(),
        pygame.K_5:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-034.png')).convert(),
        pygame.K_4:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-035.png')).convert(),
        pygame.K_3:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-036.png')).convert(),
        pygame.K_2:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-037.png')).convert(),
        pygame.K_1:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-038.png')).convert(),
    }

#The "keyboard_letters" dictionary matches each key pressed with a letter to add to the string of user input
keyboard_letters = {
    pygame.K_m:'M',
    pygame.K_n:'N',
    pygame.K_b:'B',
    pygame.K_v:'V',
    pygame.K_c:'C',
    pygame.K_x:'X',
    pygame.K_z:'Z',
    pygame.K_l:'L',
    pygame.K_k:'K',
    pygame.K_j:'J',
    pygame.K_h:'H',
    pygame.K_g:'G',
    pygame.K_f:'F',
    pygame.K_d:'D',
    pygame.K_s:'S',
    pygame.K_a:'A',
    pygame.K_p:'P',
    pygame.K_o:'O',
    pygame.K_i:'I',
    pygame.K_u:'U',
    pygame.K_y:'Y',
    pygame.K_t:'T',
    pygame.K_r:'R',
    pygame.K_e:'E',
    pygame.K_w:'W',
    pygame.K_q:'Q',
    pygame.K_0:'0',
    pygame.K_9:'9',
    pygame.K_8:'8',
    pygame.K_7:'7',
    pygame.K_6:'6',
    pygame.K_5:'5',
    pygame.K_4:'4',
    pygame.K_3:'3',
    pygame.K_2:'1',
    pygame.K_1:'1',
}

#The "get_x_value" function basically just centers text or buttons or anything based on its width 
def get_x_value(width) :
    return int((display_width-width)/2)

#Setting the typed as an empty string and rendering the text and setting the x position
current_typed = ""
current_typed_text = myfont2.render(current_typed, True, light_blue)
current_typed_x = get_x_value(current_typed_text.get_width())

#Page-001.png is the default state of no keyboard presses
if pi :
    default_typed_screen = pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-001.png')).convert()

if not pi :
    default_typed_screen = pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-001.png').convert()

#Setting the current keyboard screen as the default one
current_typed_screen = default_typed_screen

#"space_bar_down" controls whether or not to display the space bar pressed image
space_bar_down = False

#The strings "enter_extension_string" and "string2" control what the user sees as they're naming either the save or the manager. These will change to "manager" because the Name Save screen is multipurpose
enter_extension_string = "the Save"
string2 = "save"

#This is rendering the text for the header of the screen that tells the user to enter a name for either the save or manager
name_save_header = myfont2.render("Enter a Name for "+enter_extension_string, True, light_blue)

#The x position is using the "get_x_value" function from earlier
name_save_header_x = get_x_value(name_save_header.get_width())

#This is rendering the text for the warning at the bottom of the screen that tells the user that they've reached 20 characters
too_many_chars_text = myfont.render("You've reached the max amount of characters!", True, red)

#The x position is using the "get_x_value" function from earlier
too_many_chars_x = get_x_value(too_many_chars_text.get_width())

#The "too_many_chars" variable will indicate if the user
too_many_chars = False

#The "enter_or_submit" variable will control if the user sees the text "Enter a name" or "Submit a name" on the multipurpose text location/button
enter_or_submit = True

#The "over_submit" variable represents whether or not the user is hovering over the submit button for naming the save or manager
over_submit = False

#When "entering_save" is True, the user is entering a save name. When it is False, the user is entering their manager name 
entering_save = True

#The "new_save_name" string is the product of this screen when "entering_save" is True
new_save_name = ''

#######################################################################################################################################

#Calendar Screen

#######################################################################################################################################

#Temporary Save Stuff

#The "current_data" dictionary is a temporary fake save for development using Arsenal 
current_data = {
    'TeamName':'Burnley',
    'ManagerName':'Reggie Hyde',
    'CurrentLineup':['Nick Pope', 'Matthew Lowton', 'James Tarkowski', 'Ben Mee', 'Charlie Taylor', 'Johann Berg Gudmundsson', 'Ashley Westwood', 'Josh Brownhill', 'Dwight McNeil', 'Chris Wood', 'Matej Vydra'],
    'CurrentFormation':'4-4-2 (Flat)',
    'CurrentBudget':100000000,
    'CurrentTeamOverall':79,
    'CurrentDate':'September 1 2021',
    'CurrentEmails':[['Welcome to Arsenal, Manager Hyde. Here is your email inbox where you will receive important messages. Be sure to check your email to stay updated on the Premier League.', 'urmom', '6/1/2020']],
    'UnreadEmails':0,
    'CurrentStandings':{team_name_for_standings:0 for team_name_for_standings in teams_in_league},
    'CurrentStandingsInOrder':teams_in_league,
    'StandingsData':{},
    'TopScorers':{},
    'TopScorersInOrder':[],
    'TopAssistors':{},
    'TopAssistorsInOrder':[],
    'Arsenal_Players':{},
    'Arsenal_Formation':'4-2-3-1 (Wide)',
    'Arsenal_Lineup':['Bernd Leno', 'Hector Bellerin', 'David Luiz', 'Gabriel', 'Kieran Tierney', 'Thomas Partey', 'Granit Xhaka', 'Bukayo Saka', 'Gabriel Martinelli', 'Martin Odegaard', 'Alexandre Lacazette'],
    'Aston Villa_Players':{},
    'Aston Villa_Formation':'4-2-3-1 (Wide)',
    'Aston Villa_Lineup':['Emiliano Martinez', 'Matty Cash', 'Ezri Konsa', 'Tyrone Mings', 'Matt Targett', 'Douglas Luiz', 'John McGinn', 'Bertrand Traore', 'Anwar El Ghazi', 'Jack Grealish', 'Ollie Watkins'],
    'Brighton & Hove Albion_Players':{},
    'Brighton & Hove Albion_Formation':'5-3-2 (Attacking)',
    'Brighton & Hove Albion_Lineup':['Christian Walton', 'Joel Veltman', 'Ben White', 'Lewis Dunk', 'Adam Webster', 'Dan Burn', 'Pascal Gros', 'Yves Bissouma', 'Leandro Trossard', 'Neal Maupay', 'Danny Welbeck'],
    'Burnley_Players':{},
    'Burnley_Formation':'4-4-2 (Flat)',
    'Burnley_Lineup':['Nick Pope', 'Matthew Lowton', 'James Tarkowski', 'Ben Mee', 'Charlie Taylor', 'Johann Berg Gudmundsson', 'Ashley Westwood', 'Josh Brownhill', 'Dwight McNeil', 'Chris Wood', 'Matej Vydra'],
    'Chelsea_Players':{},
    'Chelsea_Formation':'5-2-3 (Flat)',
    'Chelsea_Lineup':['Edouard Mendy', 'Reece James', 'Azpilicueta', 'Thiago Silva', 'Antonio Rudiger', 'Ben Chilwell', 'NGolo Kante', 'Jorginho', 'Mason Mount', 'Timo Werner', 'Christian Pulisic'],
    'Crystal Palace_Players':{},
    'Crystal Palace_Formation':'4-3-3 (Defensive)',
    'Crystal Palace_Lineup':['Guaita', 'Joel Ward', 'Cheikhou Kouyate', 'Gary Cahill', 'Patrick van Aanholt', 'Luka Milivojevic', 'Eberechi Eze', 'Jairo Riedewald', 'Andros Townsend', 'Christian Benteke', 'Wilfried Zaha'],
    'Everton_Players':{},
    'Everton_Formation':'4-2-3-1 (Wide)',
    'Everton_Lineup':['Jordan Pickford', 'Seamus Coleman', 'Yerry Mina', 'Michael Keane', 'Lucas Digne', 'Abdoulaye Doucoure', 'Allan', 'James Rodriguez', 'Richarlison', 'Gylfi Sigurdsson', 'Dominic Calvert-Lewin'],
    'Fulham_Players':{},
    'Fulham_Formation':'4-2-3-1 (Wide)',
    'Fulham_Lineup':['Alphonse Areola', 'Kenny Tete', 'Joachim Andersen', 'Tosin Adarabioyo', 'Ola Aina', 'Mario Lemina', 'Andre-Franck Zambo Anguissa', 'Bobby Decordova-Reid', 'Ademola Lookman', 'Ruben Loftus-Cheek', 'Ivan Cavaleiro'],
    'Leeds United_Players':{},
    'Leeds United_Formation':'4-5-1 (Defensive)',
    'Leeds United_Lineup':['Illan Meslier', 'Luke Ayling', 'Diego Llorente', 'Liam Cooper', 'Ezgjan Alioski', 'Kalvin Phillips', 'Raphinha', 'Stuart Dallas', 'Tyler Roberts', 'Jack Harrison', 'Patrick Bamford'],
    'Leicester City_Players':{},
    'Leicester City_Formation':'5-3-2 (Attacking)',
    'Leicester City_Lineup':['Kasper Schmeichel', 'Ricardo Pereira', 'Wesley Fofana', 'Jonny Evans', 'Caglar Soyuncu', 'Timothy Castagne', 'Youri Tielemans', 'Wilfred Ndidi', 'James Maddison', 'Kelechi Iheanacho', 'Jamie Vardy'],
    'Liverpool_Players':{},
    'Liverpool_Formation':'4-3-3 (False 9)',
    'Liverpool_Lineup':['Alisson', 'Trent Alexander-Arnold', 'Nathaniel Phillips', 'Ozan Kabak', 'Andrew Robertson', 'Fabinho', 'Thiago', 'Georginio Wijnaldum', 'Roberto Firmino', 'Mohamed Salah', 'Sadio Mane'],
    'Manchester City_Players':{},
    'Manchester City_Formation':'4-3-3 (Defensive)',
    'Manchester City_Lineup':['Ederson', 'Joao Cancelo', 'John Stones', 'Ruben Dias', 'Oleksandr Zinchenko', 'Rodri', 'Kevin De Bruyne', 'Ilkay Gundogan', 'Riyad Mahrez', 'Gabriel Jesus', 'Phil Foden'],
    'Manchester United_Players':{},
    'Manchester United_Formation':'4-2-3-1 (Wide)',
    'Manchester United_Lineup':['Dean Henderson', 'Aaron Wan-Bissaka', 'Victor Lindelof', 'Harry Maguire', 'Luke Shaw', 'Scott McTominay', 'Fred', 'Mason Greenwood', 'Marcus Rashford', 'Bruno Fernandes', 'Edinson Cavani'],
    'Newcastle United_Players':{},
    'Newcastle United_Formation':'5-3-2 (Flat)',
    'Newcastle United_Lineup':['Martin Dubravka', 'Jacob Murphy', 'Federico Fernandez', 'Jamaal Lascelles', 'Paul Dummett', 'Matt Ritchie', 'Miguel Almiron', 'Isaac Hayden', 'Jonjo Shelvey', 'Allan Saint-Maximin', 'Joelinton'],
    'Sheffield United_Players':{},
    'Sheffield United_Formation':'5-3-2 (Flat)',
    'Sheffield United_Lineup':['Aaron Ramsdale', 'George Baldock', 'Chris Basham', 'John Egan', 'Kean Bryan', 'Enda Stevens', 'Sander Berge', 'Oliver Norwood', 'John Fleck', 'Oliver Burke', 'David McGoldrick'],
    'Southampton_Players':{},
    'Southampton_Formation':'4-4-2 (Flat)',
    'Southampton_Lineup':['Alex McCarthy', 'Kyle Walker-Peters', 'Jan Bednarek', 'Jannik Vestergaard', 'Ryan Bertrand', 'Stuart Armstrong', 'James Ward-Prowse', 'Oriol Romeu', 'Moussa Djenepo', 'Danny Ings', 'Che Adams'],
    'Tottenham Hotspur_Players':{},
    'Tottenham Hotspur_Formation':'4-2-3-1 (Wide)',
    'Tottenham Hotspur_Lineup':['Hugo Lloris', 'Serge Aurier', 'Toby Alderweireld', 'Eric Dier', 'Reguilon', 'Giovani Lo Celso', 'Pierre-Emile Hojbjerg', 'Gareth Bale', 'Heung Min Son', 'Dele Alli', 'Harry Kane'],
    'West Bromwich Albion_Players':{},
    'West Bromwich Albion_Formation':'4-5-1 (Defensive)',
    'West Bromwich Albion_Lineup':['Sam Johnstone', 'Darnell Furlong', 'Semi Ajayi', 'Kyle Bartley', 'Conor Townsend', 'Okay Yokuslu', 'Matheus Pereira', 'Jake Livermore', 'Ainsley Maitland-Niles', 'Matt Phillips', 'Mbaye Diagne'],
    'West Ham United_Players':{},
    'West Ham United_Formation':'4-2-3-1 (Wide)',
    'West Ham United_Lineup':['Lukasz Fabianski', 'Vladimir Coufal', 'Craig Dawson', 'Angelo Ogbonna', 'Aaron Cresswell', 'Tomas Soucek', 'Declan Rice', 'Pablo Fornals', 'Said Benrahma', 'Jesse Lingard', 'Michail Antonio'],
    'Wolverhampton Wanderers_Players':{},
    'Wolverhampton Wanderers_Formation':'5-2-3 (Flat)',
    'Wolverhampton Wanderers_Lineup':['Rui Patricio', 'Nelson Semedo', 'Willy Boly', 'Conor Coady', 'Romain Saiss', 'Rayan Ait Nouri', 'Ruben Neves', 'Joao Moutinho', 'Adama Traore', 'Fabio Silva', 'Pedro Neto'],
}


mr_manager_team, mr_manager_name = myfont.render(current_data['TeamName'], True, white), myfont3.render(current_data['ManagerName'], True, white)

#This loop will load Arsenal and Aston Villa into the "current_data" dictionary 
for team in teams_in_league :
    if pi :
        team_path = convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\'+team+'.dat')
    else :
        team_path = 'C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\'+team+'.dat'
    key = team+'_Players'
    current_data[key] = pickle.load(open(team_path, 'rb'))
    current_data['StandingsData'][team] = [0, 0, 0, 0, 0, 0, 0]

#The "red_cover" pygame surface is used to represent what day it is in the calendar. It is a transparent red rectangle that covers the current date on the calendar
red_cover = pygame.Surface((71,71)) 
red_cover.set_alpha(128)           
red_cover.fill((255,0,0))          

#The "coords_of_days" dictionary was produced by the commented-out loop at the bottom of the script. Each day on the calendar corresponds to a coordinate where the "red_cover" surface is drawn.
coords_of_days = {
    '1': (55, 190),
    '2': (127, 190),
    '3': (199, 190),
    '4': (271, 190),
    '5': (343, 190),
    '6': (415, 190),
    '7': (487, 190),
    '8': (56, 262),
    '9': (128, 262),
    '10': (200, 262),
    '11': (272, 262),
    '12': (344, 262),
    '13': (416, 262),
    '14': (487, 262),
    '15': (56, 335),
    '16': (128, 335),
    '17': (200, 335),
    '18': (272, 335),
    '19': (344, 335),
    '20': (416, 335),
    '21': (487, 335),
    '22': (56, 407),
    '23': (128, 407),
    '24': (200, 407),
    '25': (272, 407),
    '26': (344, 407),
    '27': (416, 407),
    '28': (487, 407),
    '29': (56, 479),
    '30': (128, 479),
    '31': (200, 479)
}

#The "unpack_date" function splits up date strings into the month, day, and year
def unpack_date(date) :
    splitted = date.split(' ') 
    return [splitted[0], int(splitted[1]), int(splitted[2])]

#The "build_date" function is essentially the opposite of "unpack_date". It takes the month, day, and year and builds date strings
def build_date(month, day, year) :
    return ' '.join([month, str(day), str(year)])

#The "advance_one_day" function builds the date string one day in the future for the sim
def advance_one_day(date) :
    month, day, year = unpack_date(date)
    month_number = get_month_number(month)
    change_screen = False
    if day == get_days_in_a_month(month) :
        if month == 'December' :
            month, day, year = 'January', 1, year+1
        else :
            month, day, year = get_number_month(month_number+1), 1, year
        change_screen = True
    else :
        month, day, year = month, day+1, year
    return build_date(month, day, year), change_screen

#The "get_coords_of_logo_and_text" function renders the logo and the the team for the match sim screen
def get_coords_of_logo_and_text(team, left_or_right) :
    x_difference = 35
    logo = team_simming_logos[team]
    logo_text = myfont.render(team, True, white)
    logo_text_width = logo_text.get_width()
    
    score_factor = 50
    
    if left_or_right == 0 :
        logo_full_width = sum([logo_text_width, 70, x_difference])
        logo_x = int(((half-score_factor)-logo_full_width)/2)
        logo_text_x = sum([logo_x, 40, x_difference])
    else :
        logo_full_width = sum([logo_text_width, 70])
        logo_text_x = (half+score_factor)+(int((display_width-(half+score_factor))-logo_full_width)/2)
        logo_x = sum([logo_text_x, logo_text_width])
    return logo, logo_text, logo_x, logo_text_x, 30, 57

#The "mouse_over_button" function returns whether or not the mouse is hovering over a rectangle
def mouse_over_button(pos, x, y, width, height) :
    return pos[0] >= x and pos[0] <= x+width and pos[1] >= y and pos[1] <= y+height

#The "display_button" function displays a button from the buttons array and returns whether or not the mouse is hovering over it 
def display_button(button, pos) :
    x, y, width, height = button[0], button[1], button[2], button[3]
    over_button = mouse_over_button(pos, x, y, width, height)
    if over_button :
        color = button[5]
        text = button[7]
    else :
        color = button[4]
        text = button[6]
    text_width, text_height = button[-2], button[-1]
    text_x, text_y = x+int((width-text_width)/2), y+int((height-text_height)/2)
    pygame.draw.rect(display, color, pygame.Rect(x, y, width, height))
    display.blit(text, (text_x, text_y))
    return over_button

#The "display_score" function displays the current score of the game
def display_score(left_score, right_score) :
    off = 30
    y = 47
    left_score_width = score_texts_width[left_score]
    display.blit(score_texts[left_score], (half-off-left_score_width, y))
    display.blit(score_texts[right_score], (half+off, y))

def get_scorers_text_and_coords(scorers, text_x) :
    scorers_texts, scorers_texts_coordinates, already_done = [], [], []
    current_text_y = 130
    for scorer in scorers :
        if not scorer in already_done : 
            scorers_texts.append(myfont.render(scorer, True, white))
            scorers_texts_coordinates.append((text_x, current_text_y))
            already_done.append(scorer)
            current_text_y += 50
    return scorers_texts, scorers_texts_coordinates

def put_standings_in_correct_order() :
    standings_dictionary = current_data['CurrentStandings']
    current_data['CurrentStandingsInOrder'] = sorted(standings_dictionary, key=lambda x:standings_dictionary[x], reverse=True)

def update_top_scorers(user_scorers, user_team, opponent_scorers, opponent_team) :
    top_scorers_dict, top_scorers_in_order = current_data['TopScorers'], current_data['TopScorersInOrder']
    max_top_scorers = 3
    top_scorers_added = 0
    for new_top_scorer in user_scorers :
        if not new_top_scorer in top_scorers_dict :
            top_scorers_dict[new_top_scorer] = current_data[user_team+'_Players'][new_top_scorer]['Goals']
            top_scorers_added += 1
    
    for new_top_scorer in opponent_scorers :
        if not new_top_scorer in top_scorers_dict :
            top_scorers_dict[new_top_scorer] = current_data[opponent_team+'_Players'][new_top_scorer]['Goals']
            top_scorers_added += 1
    
    new_dict = sorted(top_scorers_dict, key=lambda x:top_scorers_dict[x], reverse=True)
    if len(new_dict) >= max_top_scorers :
        new_dict = new_dict[:max_top_scorers]
    
    current_data['TopScorers'], current_data['TopScorersInOrder'] = {key:top_scorers_dict[key] for key in new_dict}, new_dict


def update_standings_info(team1, team2, winner, team_one_score, team_two_score) :
    current_data['StandingsData'][team1][0] += 1
    current_data['StandingsData'][team2][0] += 1
    current_data['StandingsData'][team1][4] += team_one_score
    current_data['StandingsData'][team2][4] += team_two_score
    current_data['StandingsData'][team1][5] += team_two_score
    current_data['StandingsData'][team2][5] += team_one_score
    current_data['StandingsData'][team1][6] += (team_two_score-team_one_score)
    current_data['StandingsData'][team2][6] += (team_one_score-team_two_score)
    if winner == 'Draw' :
        current_data['StandingsData'][team1][2] += 1
        current_data['StandingsData'][team2][2] += 1
    else :
        if team1 == winner :
            current_data['StandingsData'][team1][1] += 1
            current_data['StandingsData'][team2][3] += 1
        else :
            current_data['StandingsData'][team2][1] += 1
            current_data['StandingsData'][team1][3] += 1
    

def sim_other_games(without_year, games_in_current_month) :
    if without_year in games_in_current_month :
        games_in_day = games_in_current_month[without_year]
        for other_game in games_in_day :
            team1, team2 = other_game
            print(team1, team2)
            if team1 != team and team2 != team :
                team1_players, team1_lineup, team1_formation, team2_players, team2_lineup, team2_formation = current_data[team1+'_Players'], current_data[team1+'_Lineup'], current_data[team1+'_Formation'], current_data[team2+'_Players'], current_data[team2+'_Lineup'], current_data[team2+'_Formation']
                team1_rating = calculate_rating(team1_players, team1_lineup, team1_formation)
                team2_rating = calculate_rating(team2_players, team2_lineup, team2_formation)
                winner, score_difference = match_sim(team1_rating, team2_rating, team1, team2)
                score, team1_scorers, team2_scorers = randomize_goals(team1_players, team2_players, team1_lineup, team2_lineup, team1, team2, team1_formation, team2_formation, winner, score_difference)
                s_one, s_two = score.split('-')
                final_team1_score, final_team2_score = int(s_one), int(s_two)
                for nop in team1_scorers :
                    current_data[team1+'_Players'][nop]['Goals'] += 1
                    if nop in current_data['TopScorersInOrder'] :
                        current_data['TopScorers'][nop] += 1
                    
                for nop in team2_scorers :
                    current_data[team2+'_Players'][nop]['Goals'] += 1
                    if nop in current_data['TopScorersInOrder'] :
                        current_data['TopScorers'][nop] += 1
                
                if winner == 'Draw' :
                    current_data['CurrentStandings'][team1] += 1
                    current_data['CurrentStandings'][team2] += 1
                else :
                    current_data['CurrentStandings'][winner] += 3
                    current_data['StandingsData'][winner]
                
                put_standings_in_correct_order()
                update_top_scorers(team1_scorers, team1, team2_scorers, team2)
                update_standings_info(team1, team2, winner, final_team1_score, final_team2_score)

#The "calendar_screens" array is going to be filled with every calendar month screen in order
calendar_screens = []

#This loop fills "calendar_screens" with every calendar month screen in order
for i in range(12) :
    path = 'C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Month-'+str(i+1)+'.png'
    if pi :
        path = convert_path(path)
    calendar_screens.append(pygame.image.load(path).convert())

#Get values from the save, which is fake right now
team = current_data['TeamName']
current_date = current_data['CurrentDate']
month, day, year = unpack_date(current_date)
month_number = get_month_number(month)

#Get the current calendar month screen
current_calendar_screen = calendar_screens[month_number]

#The "team_logos" and "team_simming_logos" dictionaries contain the team logos on the calendar and the team logos during the sim
team_logos = {}
team_simming_logos = {}
mini_team_logos = {}

#Load up "team_logos" and "team_simming_logos" with the pygame surfaces
for t in teams_in_league :
    path = 'C:\\Users\\rhyde23\\Desktop\\Project\\Images\\'+t+'.png'
    if pi :
        path = convert_path(path)
    loaded_image_logo = pygame.image.load(path).convert_alpha()
    team_logos[t] = pygame.transform.scale(loaded_image_logo, (40, 40))
    team_simming_logos[t] = pygame.transform.scale(loaded_image_logo, (70, 70))
    mini_team_logos[t] = pygame.transform.scale(loaded_image_logo, (18, 18))

#The "schedule_dict" dictionary contains all of the matchdays and every game in the matchday
schedule_dict = get_schedule()

#The "games_in_current_month" dictionary contains every game taking place in this month
games_in_current_month = {date:schedule_dict[date] for date in schedule_dict if date.split(' ')[0] == month}

#The "dates_of_games_in_month" dictionary contains all of the dates of the games in the current month that the user is playing in 
dates_of_games_in_month = get_games_in_a_month(month, schedule_dict, team)

#These two rendered texts are for the upcoming games on the calendar
GAME_text = myfont3.render("GAME", True, white)
GAMEVS_text = myfont3.render("VS", True, white)

#The "calendar_buttons" array contains all of the buttons that will be run through the "display_button" function
calendar_buttons = [
    [300, 120, 100, 30, white, red, myfont3.render("START SIM", True, red), myfont3.render("START SIM", True, white)],
    [300, 120, 100, 30, red, white, myfont3.render("END SIM", True, white), myfont3.render("END SIM", True, red)],
    [300, 120, 100, 30, white, red, myfont3.render("PLAY MATCH", True, red), myfont3.render("PLAY MATCH", True, white)],
]

#This loop adds the width and height of the text into each button in the "calendar_buttons" array
for i, calendar_button in enumerate(calendar_buttons) :
    calendar_buttons[i] = calendar_buttons[i] + [calendar_button[-2].get_width(), calendar_button[-2].get_height()]

#Loading the match sim background for when the user is in "match_simming"
match_sim_background_path = 'C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Match Sim.png'
if pi :
    match_sim_background_path = convert_path(match_sim_background_path)
match_sim_background = pygame.image.load(match_sim_background_path).convert()

#The "score_texts" array contains all of the rendered texts of the scoreboard for the Match Simming screen
score_texts = [
    myfont2.render("0", True, white),
    myfont2.render("1", True, white),
    myfont2.render("2", True, white),
    myfont2.render("3", True, white),
    myfont2.render("4", True, white),
    myfont2.render("5", True, white),
    myfont2.render("6", True, white),
    myfont2.render("7", True, white),
    myfont2.render("8", True, white),
    myfont2.render("9", True, white),
]

#The "score_texts_width" array contains all of the widths of the rendered scoreboard texts
score_texts_width = [t.get_width() for t in score_texts]

#These two arrays are the buttons for the match simming screen
start_simming_button = [300, 575, 100, 30, white, red, myfont3.render("START MATCH", True, red), myfont3.render("START MATCH", True, white)]
start_simming_button = start_simming_button + [start_simming_button[-2].get_width(), start_simming_button[-2].get_height()]
start_simming_button[0] = half-int(start_simming_button[2]/2)
return_simming_button = [300, 575, 100, 30, red, white, myfont3.render("RETURN TO MENU", True, white), myfont3.render("RETURN TO MENU", True, red)]
return_simming_button = return_simming_button + [return_simming_button[-2].get_width(), return_simming_button[-2].get_height()]
return_simming_button[0] = half-int(return_simming_button[2]/2)

#The "simming_minute_texts" array contains all of the rendered texts for every minute of the game
simming_minute_texts = [myfont.render(str(minute)+'\'', True, white) for minute in range(1, 91)]
simming_minute_texts_widths = [simming_minute_text.get_width() for simming_minute_text in simming_minute_texts]
simming_minute_texts_x = [half-int(simming_minute_text_width/2) for simming_minute_text_width in simming_minute_texts_widths]

#The "simming_scoring_minutes_texts" array contains all of the rendered texts for every minute of the game for the scorers
simming_scoring_minutes_texts = [myfont.render(str(minute)+'\'', True, white) for minute in range(1, 91)]

#Render a comma
comma_text = myfont.render(',', True, white)

#The "return_available" variable whether or not we should display the Return to Calendar Screen button
return_available = False

#These two variables tell us if the user is hovering over the Start Match button and the Return to Menu button, respectively
over_button1 = False
over_button2 = False

#The "calendar_calendar_button_index" integer picks the correct button from "calendar_buttons"
calendar_button_index = 0

#The "over_sim_button" variable tells us whether or not the user is hovering over the Start Simulation button
over_sim_button = False

#The "simming" variable tells us whether or not we are currently simming
simming = False

#The "stopped_on_matchday" variable tells us whether or not the next simming action will be to play the match
stopped_on_matchday = False

#The "simming_count" adds one every frame. When it gets to 50, one day is progressed
simming_count = 0

#The "match_simming" variable almost acts as a whole loop, but it is under "calendar"
match_simming = False

#######################################################################################################################################

#Standings Screen

#######################################################################################################################################


standings_background_path = 'C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Standings Background.png'
if pi :
    standings_background_path = convert_path(standings_background_path)
    
standings_background = pygame.image.load(standings_background_path).convert()

header_strings = ['GP', 'W', 'D', 'L', 'GF', 'GA', 'GD', 'Pts']
header_texts = [myfont3.render(header_string, True, white) for header_string in header_strings]
header_texts_width = [header_text.get_width() for header_text in header_texts]
header_texts_x = []
last_header_text_width = 0
last_header_text_x = 235
        
for i, header_text in enumerate(header_texts) :
    header_x_coord = last_header_text_x+last_header_text_width+20
    print(header_x_coord, header_texts_width[i])
    header_texts_x.append(header_x_coord)
    last_header_text_width = header_texts_width[i]
    last_header_text_x = header_x_coord

standings_team_texts = {standings_team_text:myfont4.render(standings_team_text, True, white) for standings_team_text in teams_in_league}

small_text_numbers = {i:myfont4.render(str(i), True, white) for i in range(-150, 100)}
small_text_numbers_widths = {key:small_text_numbers[key].get_width() for key in small_text_numbers}

def display_standings_headers() :
    for i, header_text in enumerate(header_texts) :
        display.blit(header_text, (header_texts_x[i], 125))

def display_standings_data() :
    for i, team_in_order in enumerate(current_data['CurrentStandingsInOrder']) :
        y = (i*22)+140
        display.blit(standings_team_texts[team_in_order], (60, y))
        display.blit(mini_team_logos[team_in_order], (40, y))
        for enum, stat in enumerate(current_data['StandingsData'][team_in_order]) :
            small_stat_width = small_text_numbers_widths[stat]
            small_stat_x = header_texts_x[enum]+int((header_texts_width[enum]-small_stat_width)/2)
            display.blit(small_text_numbers[stat], (small_stat_x, y+2))
        #current_data['StandingsData'][team]








#######################################################################################################################################

#The "manager_loop" variable is always True, it runs every other loop
manager_loop = True

#All of these variables are the loops for every screen
saves_menu = False
name_save = False
calendar = True
lineups = False
standings = False
transfers = False
emails = False
training = False


#Temporary text
lineups_text = myfont.render('Lineups', True, black)
standings_text = myfont.render('Standings', True, black)
transfers_text = myfont.render('Transfers', True, black)
emails_text = myfont.render('Emails', True, black)
training_text = myfont.render('Training', True, black)

#Here is where we actually run the UI
while manager_loop :
    while training :
        display.fill(white)
        display.blit(training_text, (0, 0))
        for event in pygame.event.get() :
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_RIGHT :
                    training = False
                    calendar = True
                if event.key == pygame.K_LEFT :
                    training = False
                    emails = True
        pygame.display.update()
    while emails :
        display.fill(white)
        display.blit(emails_text, (0, 0))
        for event in pygame.event.get() :
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_RIGHT :
                    emails = False
                    training = True
                if event.key == pygame.K_LEFT :
                    emails = False
                    transfers = True
        pygame.display.update()
    
    while transfers :
        display.fill(white)
        display.blit(transfers_text, (0, 0))
        for event in pygame.event.get() :
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_RIGHT :
                    transfers = False
                    emails = True
                if event.key == pygame.K_LEFT :
                    transfers = False
                    standings = True
        pygame.display.update()
    
    while standings :
        display.fill(white)
        display.blit(standings_background, (0, 0))
        display_standings_headers()
        display_standings_data()
        for event in pygame.event.get() :
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_RIGHT :
                    standings = False
                    transfers = True
                if event.key == pygame.K_LEFT :
                    standings = False
                    lineups = True
        pygame.display.update()
    
    while lineups :
        display.fill(white)
        display.blit(lineups_text, (0, 0))
        for event in pygame.event.get() :
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_RIGHT :
                    lineups = False
                    standings = True
                if event.key == pygame.K_LEFT :
                    lineups = False
                    calendar = True
        pygame.display.update()
    
    #Calendar Screen
    while calendar :
        
        #Fill background with white
        display.fill(white)
        
        #If the user simming a match
        if match_simming :
            
            #Get mouse position
            x, y = pygame.mouse.get_pos()
            
            #Display the Match Sim Background
            display.blit(match_sim_background, (0, 0))
            
            #Display the text that tells the user what the stadium is playing at
            display.blit(stadium_text, (stadium_text_x, 500))
            
            #Display the logo of the user's team logo
            display.blit(user_logo, (user_logo_x, user_logo_y))
            
            #Display the name of the user's team 
            display.blit(user_logo_text, (user_logo_text_x, user_logo_text_y))
            
            #Display the logo of the opponent's team logo
            display.blit(opponent_logo, (opponent_logo_x, opponent_logo_y))
            
            #Display the name of the opponent's team 
            display.blit(opponent_logo_text, (opponent_logo_text_x, opponent_logo_text_y))
            
            #Display the minute of the game
            display.blit(simming_minute_texts[current_minute-1], (simming_minute_texts_x[current_minute-1], 80))
            
            for sc_texts in currently_displaying :
                t, c = sc_texts
                display.blit(t, c)
            
            #Display the scoreboard. If the variable "next_left_or_right" variable == 0, it means that the user is the home
            if next_left_or_right == 0 :
                display_score(current_user_score, opponent_score)
            else :
                display_score(opponent_score, current_user_score)
            
            #If the user is currently simming
            if currently_simming :
                
                #This frame count variable adds one to the current minute when it reaches 20
                current_minute_count += 1
                
                #If the frames get to 20, add a minute 
                if current_minute_count == current_minute_max_count :
                    current_minute_count = 0
                    current_minute += 1
                    
                    #Accounts for if user's team scores in the current_minute
                    if current_minute in user_score_minutes :
                        current_user_score += 1
                        user_scorer = user_scorers[user_score_minutes.index(current_minute)]
                        if not user_scorer in user_names_already_displayed :
                            next_scorer_coords = user_scorers_texts_coords[user_ind]
                            next_scorer_text = user_scorers_texts[user_ind]
                            currently_displaying.append([next_scorer_text, next_scorer_coords])
                            l_x = next_scorer_coords[0]+next_scorer_text.get_width()+10
                            minn_text = simming_scoring_minutes_texts[current_minute-1]
                            currently_displaying.append([minn_text, (l_x, next_scorer_coords[1])])
                            user_scorers_texts_last_x.append(l_x+minn_text.get_width())
                            user_names_already_displayed.append(user_scorer)
                            user_ind += 1
                        else :
                            bruh_index = user_names_already_displayed.index(user_scorer)
                            comma_text_x = user_scorers_texts_last_x[bruh_index]
                            currently_displaying.append([comma_text, (comma_text_x, user_scorers_texts_coords[bruh_index][1])])
                            another_minute_x = comma_text_x+10
                            minn_text = simming_scoring_minutes_texts[current_minute-1]
                            currently_displaying.append([minn_text, (another_minute_x, user_scorers_texts_coords[bruh_index][1])])
                            user_scorers_texts_last_x[bruh_index] = another_minute_x+minn_text.get_width()

                    #Accounts for if opponent scores in the current_minute
                    if current_minute in opponent_score_minutes :
                        opponent_score += 1
                        opponent_scorer = opponent_scorers[opponent_score_minutes.index(current_minute)]
                        if not opponent_scorer in opponent_names_already_displayed :
                            next_scorer_coords = opponent_scorers_texts_coords[opponent_ind]
                            next_scorer_text = opponent_scorers_texts[opponent_ind]
                            currently_displaying.append([next_scorer_text, next_scorer_coords])
                            l_x = next_scorer_coords[0]+next_scorer_text.get_width()+10
                            minn_text = simming_scoring_minutes_texts[current_minute-1]
                            currently_displaying.append([minn_text, (l_x, next_scorer_coords[1])])
                            opponent_scorers_texts_last_x.append(l_x+minn_text.get_width())
                            opponent_names_already_displayed.append(opponent_scorer)
                            opponent_ind += 1
                        else :
                            bruh_index = opponent_names_already_displayed.index(opponent_scorer)
                            comma_text_x = opponent_scorers_texts_last_x[bruh_index]
                            currently_displaying.append([comma_text, (comma_text_x, opponent_scorers_texts_coords[bruh_index][1])])
                            another_minute_x = comma_text_x+10
                            minn_text = simming_scoring_minutes_texts[current_minute-1]
                            currently_displaying.append([minn_text, (another_minute_x, opponent_scorers_texts_coords[bruh_index][1])])
                            opponent_scorers_texts_last_x[bruh_index] = another_minute_x+minn_text.get_width()
                    
                    #If the game reaches 90 minutes, display the return button 
                    if current_minute == 90 :
                        currently_simming = False
                        return_available = True
                
            #These two instances are seeing if the user is hovering over the return button and the start simming button, respectively
            elif return_available :
                over_button2 = display_button(return_simming_button, (x, y))
            else :
                over_button1 = display_button(start_simming_button, (x, y))
            
            #This is the event loop detects for button clicks
            for event in pygame.event.get() :
                if event.type == pygame.MOUSEBUTTONDOWN :
                    
                    #If the user is hovering over the Start Sim Button, start the sim
                    if over_button1 :
                        currently_simming = True
                        over_button1 = False
                    
                    #If the user is hovering over the return button, reset all of the variables and go back to calendar screen
                    if over_button2 :
                        
                        #If the user clicks the Return Button, reset all of the variables for this screen for next time
                        
                        #Make the "match_simming" variable False so the user returns back to the normal calendar screen
                        match_simming = False
                        
                        #The "return_available" variable whether or not we should display the Return to Calendar Screen button
                        return_available = False

                        #These two variables tell us if the user is hovering over the Start Match button and the Return to Menu button, respectively
                        over_button1 = False
                        over_button2 = False

                        #The "calendar_calendar_button_index" integer picks the correct button from "calendar_buttons"
                        calendar_button_index = 0

                        #The "over_sim_button" variable tells us whether or not the user is hovering over the Start Simulation button
                        over_sim_button = False

                        #The "simming" variable tells us whether or not we are currently simming
                        simming = False

                        #The "stopped_on_matchday" variable tells us whether or not the next simming action will be to play the match
                        stopped_on_matchday = False

                        #The "simming_count" adds one every frame. When it gets to 50, one day is progressed
                        simming_count = 0

                        #The "match_simming" variable almost acts as a whole loop, but it is under "calendar"
                        match_simming = False
        else :
            display.blit(current_calendar_screen, (0, 0))
            display.blit(team_logos[team], (10, 10))
            display.blit(mr_manager_team, (60, 10))
            display.blit(mr_manager_name, (60, 30))
            x, y = pygame.mouse.get_pos()
            for game_date in dates_of_games_in_month :
                opponent, stadium, left_or_right = dates_of_games_in_month[game_date]
                m, d = game_date.split(' ')
                display_coords = coords_of_days[d]
                display_coords_logo = (display_coords[0]+15, display_coords[1]+30)
                display_coords_text = (display_coords[0]+22, display_coords[1]+10)
                display_coords_text2 = (display_coords[0]+30, display_coords[1]+20)
                display.blit(team_logos[opponent], display_coords_logo)
                display.blit(GAME_text, display_coords_text)
                display.blit(GAMEVS_text, display_coords_text2)
            for event in pygame.event.get() :
                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_RIGHT :
                        calendar = False
                        lineups = True
                    if event.key == pygame.K_LEFT :
                        calendar = False
                        training = True
                if event.type == pygame.MOUSEBUTTONDOWN :
                    if over_sim_button :
                        if stopped_on_matchday :
                            match_simming = True
                            stadium_text = myfont.render(next_stadium, True, white)
                            stadium_text_width = stadium_text.get_width()
                            stadium_text_x = int((display_width-stadium_text_width)/2)
                            user_logo, user_logo_text, user_logo_x, user_logo_text_x, user_logo_y, user_logo_text_y = get_coords_of_logo_and_text(team, next_left_or_right)
                            if next_left_or_right == 0 :
                                opponent_lor = 1
                            else :
                                opponent_lor = 0
                            opponent_logo, opponent_logo_text, opponent_logo_x, opponent_logo_text_x, opponent_logo_y, opponent_logo_text_y = get_coords_of_logo_and_text(next_opponent, opponent_lor)

                            
                            user_formation = current_data['CurrentFormation']
                            user_players = current_data[team+'_Players']
                            user_lineup = current_data['CurrentLineup']

                            opponent_formation = current_data[next_opponent+'_Formation']
                            opponent_players = current_data[next_opponent+'_Players']
                            opponent_lineup = current_data[next_opponent+'_Lineup']
                            
                            
                            user_rating = calculate_rating(user_players, user_lineup, user_formation)
                            opponent_rating = calculate_rating(opponent_players, opponent_lineup, opponent_formation)
                            print(user_rating, opponent_rating)

                            if next_left_or_right == 0 :
                                winner, score_difference = match_sim(user_rating, opponent_rating, team, next_opponent)
                                score, user_scorers, opponent_scorers = randomize_goals(user_players, opponent_players, user_lineup, opponent_lineup, team, next_opponent, user_formation, opponent_formation, winner, score_difference)
                                s_one, s_two = score.split('-')
                                final_user_score, final_opponent_score = int(s_one), int(s_two)
                                user_scorers_text_x, opponent_scorers_text_x = 75, half+20
                                update_standings_info(team, next_opponent, winner, final_user_score, final_opponent_score)
                            else :
                                winner, score_difference = match_sim(opponent_rating, user_rating, next_opponent, team)
                                score, opponent_scorers, user_scorers = randomize_goals(opponent_players, user_players, opponent_lineup, user_lineup, next_opponent, team, opponent_formation, user_formation, winner, score_difference)
                                s_one, s_two = score.split('-')
                                final_opponent_score, final_user_score = int(s_one), int(s_two)
                                opponent_scorers_text_x, user_scorers_text_x = 75, half+20
                                update_standings_info(next_opponent, team, winner, final_opponent_score, final_user_score)
                            
                            user_scorers_texts, user_scorers_texts_coords = get_scorers_text_and_coords(user_scorers, user_scorers_text_x)
                            opponent_scorers_texts, opponent_scorers_texts_coords = get_scorers_text_and_coords(opponent_scorers, opponent_scorers_text_x)
                            user_scorers_texts_last_x, opponent_scorers_texts_last_x = [], []
                            
                            user_ind, opponent_ind = 0, 0
                            
                            currently_displaying = []
                            user_names_already_displayed = []
                            opponent_names_already_displayed = []
                            
                            current_user_score, opponent_score = 0, 0
                            current_minute = 1
                            current_minute_count = 0
                            current_minute_max_count = 5
                            user_score_minutes, opponent_score_minutes = randomize_goals_minutes(final_user_score), randomize_goals_minutes(final_opponent_score)
                            
                            user_score_minutes = sorted(user_score_minutes)
                            opponent_score_minutes = sorted(opponent_score_minutes)
                            
                            currently_simming = False
                            
                            for nop in user_scorers :
                                current_data[team+'_Players'][nop]['Goals'] += 1
                                if nop in current_data['TopScorersInOrder'] :
                                    current_data['TopScorers'][nop] += 1
                                    
                            for nop in opponent_scorers :
                                current_data[next_opponent+'_Players'][nop]['Goals'] += 1
                                if nop in current_data['TopScorersInOrder'] :
                                    current_data['TopScorers'][nop] += 1
                            
                            if winner == 'Draw' :
                                current_data['CurrentStandings'][team] += 1
                                current_data['CurrentStandings'][next_opponent] += 1
                            else :
                                current_data['CurrentStandings'][winner] += 3
                            
                            put_standings_in_correct_order()
                            update_top_scorers(user_scorers, team, opponent_scorers, next_opponent)
                        else :
                            if not simming :
                                simming = True
                                calendar_button_index += 1
                            else :
                                simming = False
                                calendar_button_index -= 1
                                simming_count = 0
            display.blit(red_cover, coords_of_days[str(day)])
            over_sim_button = display_button(calendar_buttons[calendar_button_index], (x, y))
            if simming :
                simming_count += 1
                if simming_count == 20 :
                    current_date, next_month = advance_one_day(current_date)
                    month, day, year = unpack_date(current_date)
                    without_year = ' '.join([month, str(day)])
                    if without_year in games_in_current_month :
                        sim_other_games(without_year, games_in_current_month) 
                    if next_month :
                        month_number = get_month_number(month)
                        current_calendar_screen = calendar_screens[month_number]
                        dates_of_games_in_month = get_games_in_a_month(month, schedule_dict, team)
                        games_in_current_month = {date:schedule_dict[date] for date in schedule_dict if date.split(' ')[0] == month}
                    try :
                        next_opponent, next_stadium, next_left_or_right = dates_of_games_in_month[without_year]
                        
                        stopped_on_matchday = True

                        simming = False
                        calendar_button_index = 2
                        simming_count = 0
                    except :
                        pass
                    simming_count = 0
        pygame.display.update()
    while saves_menu :
        display.fill(white)
        display.blit(current_save_image, (0, 0))
        display.set_at(current_clicked, red)
        x, y = pygame.mouse.get_pos()
        for event in pygame.event.get() :
            if event.type == pygame.MOUSEBUTTONDOWN :
                coords = pygame.mouse.get_pos()
                if clicker_mode :
                    current_clicked = coords
                save_selected = save_number
                print(save_selected)
                saves_menu = False
                name_save = True
                
        
        for i, save_name_text in enumerate(save_names_texts) :
            text_y = buttons[i][0]+offset[i]
            display.blit(save_name_text, (100, text_y))
            
        if x >= x_start and x <= x_end :
            for i, button in enumerate(buttons) :
                if y >= button[0] and y <= button[1] :
                    save_number = i
                    current_save_image = save_background_images[save_number]
        pygame.display.update()
        
        
    while name_save :
        display.fill(white)
        display.blit(current_typed_screen, (0, 0))
        x, y = pygame.mouse.get_pos()
        for event in pygame.event.get() :
            if event.type == pygame.MOUSEBUTTONDOWN :
                coords = pygame.mouse.get_pos()
                if over_submit :
                    if entering_save :
                        new_save_name = current_typed
                        current_typed = ""
                        current_typed_text = myfont2.render(current_typed, True, light_blue)
                        current_typed_x = get_x_value(current_typed_text.get_width())
                        current_typed_screen = default_typed_screen

                        space_bar_down = False

                        enter_extension_string = "your Manager"
                        string2 = "manager"

                        name_save_header = myfont2.render("Enter a Name for "+enter_extension_string, True, light_blue)
                        name_save_header_x = get_x_value(name_save_header.get_width())

                        too_many_chars = False

                        enter_or_submit = True
                        over_submit = False

                        entering_save = False
                    else :
                        new_manager_name = current_typed
                        quit()
            if event.type == pygame.KEYDOWN :
                try :
                    key = event.key
                    if key == pygame.K_SPACE :
                        if len(current_typed) < 20 :
                            space_bar_down = True
                            current_typed += ' '
                        else :
                            too_many_chars = True
                    elif key == pygame.K_BACKSPACE :
                        current_typed = current_typed[:-1]
                        current_typed_screen = keyboard_order[key]
                        too_many_chars = False
                    else :
                        if len(current_typed) < 20 :
                            current_typed_screen = keyboard_order[key]
                            current_typed += keyboard_letters[key]
                        else :
                            too_many_chars = True
                    current_typed_text = myfont2.render(current_typed, True, light_blue)
                    current_typed_x = get_x_value(current_typed_text.get_width())
                except :
                    pass
                if current_typed != '' and enter_or_submit :
                    name_save_header = myfont2.render("Click here to submit "+string2+" name", True, light_blue)
                    name_save_header_x = get_x_value(name_save_header.get_width())
                    enter_or_submit = False
                if current_typed == '' and not enter_or_submit :
                    name_save_header = myfont2.render("Enter a Name for "+enter_extension_string, True, light_blue)
                    name_save_header_x = get_x_value(name_save_header.get_width())
                    enter_or_submit = True
                    over_submit = False
            if event.type == pygame.KEYUP :
                if key == pygame.K_SPACE :
                    space_bar_down = False
                current_typed_screen = default_typed_screen
        
        if x >= 42 and x <= 745 and y >= 51 and y <= 109 and (not enter_or_submit) and (not over_submit) :
            over_submit = True
            name_save_header = myfont2.render("Click here to submit "+string2+" name", True, gray)
        if over_submit and not (x >= 42 and x <= 745 and y >= 51 and y <= 109) :
            over_submit = False
            name_save_header = myfont2.render("Click here to submit "+string2+" name", True, light_blue)
        if space_bar_down :
            pygame.draw.rect(display, key_color, pygame.Rect(240, 505, 315, 50))
        else :
            pygame.draw.rect(display, white, pygame.Rect(240, 505, 315, 50))
        if over_submit :
            pygame.draw.rect(display, light_blue, pygame.Rect(42, 51, 703, 58))
        else :
            pygame.draw.rect(display, gray, pygame.Rect(42, 51, 703, 58))
        display.blit(name_save_header, (name_save_header_x, 60))
        display.blit(current_typed_text, (current_typed_x, 160))
        if too_many_chars :
            display.blit(too_many_chars_text, (too_many_chars_x, 575))
        pygame.display.update()

        
#The "guess_coords_of_day" function puts the red cover roughly where it should be, and then the loop below allows me to manually fix that. The calendar graphic is not centered
"""
def guess_coords_of_day(date) :
    month, day, year = unpack_date(date)
    mod = day % 7
    if mod == 0 :
        down, right = int((day-mod)/7)-1, 7
    else :
        down, right = int((day-mod)/7), mod
    return ((right-1)*73)+55, (down*73)+190
"""
        
        
#This commented-out code was for manually getting the coordinates for each day on the calendar for the "red_cover" surface. I will keep it just in case
"""
while calendar :
    display.fill(white)
    display.blit(current_calendar_screen, (0, 0))
    display.blit(red_cover, (day_x, day_y))
    for event in pygame.event.get() :
        if event.type == pygame.MOUSEBUTTONDOWN :
            coords = pygame.mouse.get_pos()
            print(coords)
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_RIGHT :
                day_x += 1
            elif event.key == pygame.K_LEFT :
                day_x -= 1
            elif event.key == pygame.K_DOWN :
                day_y += 1
            elif event.key == pygame.K_UP :
                day_y -= 1
            elif event.key == pygame.K_RETURN :
                coords_of_days[current_date] = [day_x, day_y]
                current_date, change_screen = advance_one_day(current_date)
                if change_screen :
                    print(coords_of_days)
                    quit()
                day_x, day_y = guess_coords_of_day(current_date)
    pygame.display.update()
"""

