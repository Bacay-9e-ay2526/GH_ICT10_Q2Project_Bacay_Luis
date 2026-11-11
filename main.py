# 2nd Quarter Project - Combined Code (Basketball Varsity & Chemistry Elements)
from pyscript import document, display


# 1. Verify if a student is on the varsity tryout roster
def candidate_checker(e):
    # List of approved varsity candidates
    roster_list = [
        'luis bacay',
        'chester roxas',
        'joseph co',
        'enzo villegas',
        'Brenton Dela Fuente',
        'zhaimer mamacotao',
        'paulo liwag',
        'matteo ressurection',
    ]

    # Retrieve input values from text fields
    player_first = document.getElementById('first_name').value
    player_last = document.getElementById('last_name').value
    prospect_name = player_first + ' ' + player_last
    is_rostered = prospect_name.lower() in roster_list

    # Status messages tuple indexed by boolean (False=0, True=1)
    status_messages = (
        f'Sorry {prospect_name}, your name is not on the varsity roster.',
        f'Congratulations {prospect_name}! You made the basketball varsity team.',
    )

    document.getElementById('result').innerHTML = status_messages[is_rostered]


# 2. Combine grade level squads and add a new player to the team roster
def result_checker(e):
    document.getElementById('output').innerHTML = ' '

    # Squad sets categorized by grade level
    freshmen_squad = {'Joshua Ortiz', 'Mark Gervacio', 'Bjorn Amargo'}
    sophomore_squad = {'Joel Gonzales', 'Dylan Harper', 'Cooper Flag', 'Paolo Liwag'}
    junior_squad = {'Dwayne Wade', 'Chester Roxas', 'Kyrie Irving'}
    senior_squad = { 
        'Lebron James',
        'Steph Curry',
        'Micheal Jordan',
        'Ezekiel Bacay',
    }

    # Get input and format new team member
    fname_input = document.getElementById('first_name').value
    lname_input = document.getElementById('last_name').value
    incoming_player = fname_input + ' ' + lname_input
    incoming_set = {incoming_player}

    # Union of all sets to create complete roster and count total members
    complete_roster = (
        freshmen_squad
        | sophomore_squad
        | junior_squad
        | senior_squad
        | incoming_set
    )
    roster_count = len(complete_roster)

    formatted_roster = '<br>'.join(sorted(complete_roster))

    document.getElementById('output').innerHTML = (
        f'Team Roster:<br>{formatted_roster}'
    )
    display(f'Total Team Members: {roster_count}', target='output')


# 3. Non-Metal Elements Data Reference & Search
non_metals_data = {
    "H":  ("Hydrogen",   1,  1.008),
    "He": ("Helium",     2,  4.0026),
    "C":  ("Carbon",     6,  12.011),
    "N":  ("Nitrogen",   7,  14.007),
    "O":  ("Oxygen",     8,  15.999),
    "F":  ("Fluorine",   9,  18.998),
    "Ne": ("Neon",       10, 20.180),
    "P":  ("Phosphorus", 15, 30.974),
    "S":  ("Sulfur",     16, 32.06),
    "Cl": ("Chlorine",   17, 35.45),
    "Ar": ("Argon",      18, 39.948),
    "Se": ("Selenium",   34, 78.971),
    "Br": ("Bromine",    35, 79.904),
    "Kr": ("Krypton",    36, 83.798),
    "I":  ("Iodine",     53, 126.90),
    "Xe": ("Xenon",      54, 131.29),
    "Rn": ("Radon",      86, 222)
}

def search_element_info(e):
    # Clear output area before displaying new results
    document.getElementById('result_output').innerHTML = ''
    
    # Retrieve user input, format to title case (e.g., 'rn' -> 'Rn')
    user_symbol_input = document.getElementById('input_symbol').value.strip().title()
    
    # Retrieve element data using .get() with fallback default values
    element_details = non_metals_data.get(
        user_symbol_input,
        ("Element not found", "-", "-")
    )

    # Render results or error message dynamically back into the HTML output panel
    if element_details[0] == 'Element not found':
        document.getElementById('result_output').innerHTML = f"""
            <b>Symbol:</b> {user_symbol_input}<br>
            <span style="color: red;">Element not found. Please enter a valid non-metal symbol.</span>
        """
    else:
        document.getElementById('result_output').innerHTML = f"""
            <b>Symbol:</b> {user_symbol_input}<br>
            <b>Element:</b> {element_details[0]}<br>
            <b>Atomic Number:</b> {element_details[1]}<br>
            <b>Atomic Mass:</b> {element_details[2]}
        """