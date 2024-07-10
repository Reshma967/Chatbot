from flask import Flask, render_template, request, jsonify, session

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Sample data for departments, events, financial aid, hostel, bus, canteen, placements within a university
departments = {
    'Computer Science': {
        'location': 'Main Building, Delhi Campus',
        'programs': ['B.Tech CSE', 'M.Tech CSE', 'Ph.D. Computer Science'],
        'contact': 'cs@university.in',
        'head': 'Dr. Rajesh Kumar',
        'events': [
            {'title': 'Tech Symposium 2024', 'date': '2024-09-15', 'time': '10:00 AM', 'location': 'Auditorium'},
            {'title': 'Hackathon 2024', 'date': '2024-10-05', 'time': '09:30 AM', 'location': 'Computer Lab'}
        ],
        'financial_aid': {
            'types': ['Scholarships', 'Student Loans', 'Internships'],
            'contact': 'financialaid@university.in'
        },
        'tuition_fees': '₹1,50,000 per year',
        'hostel_info': {
            'name': 'CS Hostel',
            'location': 'Near Main Building',
            'facilities': ['Single rooms', 'Wi-Fi', 'Common lounge'],
            'contact': 'cshostel@university.in'
        },
        'bus_details': {
            'route': 'Campus Shuttle A',
            'timing': 'Every 30 minutes',
            'contact': 'transport@university.in'
        },
        'canteen_info': {
            'location': 'Student Plaza',
            'menu': ['North Indian', 'South Indian', 'Chinese', 'Continental'],
            'contact': 'canteen@university.in'
        },
        'placements': {
            'companies': ['Infosys', 'TCS', 'Wipro', 'Microsoft'],
            'average_salary': '₹6,00,000 per annum',
            'contact': 'placements@university.in'
        }
    },
    'Electrical Engineering': {
        'location': 'Engineering Block, Mumbai Campus',
        'programs': ['B.Tech EE', 'M.Tech EE', 'Ph.D. Electrical Engineering'],
        'contact': 'ee@university.in',
        'head': 'Dr. Sneha Sharma',
        'events': [
            {'title': 'Seminar on Renewable Energy', 'date': '2024-09-20', 'time': '11:00 AM', 'location': 'Seminar Hall'},
            {'title': 'Workshop on Power Systems', 'date': '2024-10-10', 'time': '02:00 PM', 'location': 'Lab 302'}
        ],
        'financial_aid': {
            'types': ['Scholarships', 'Grants', 'Work-Study Programs'],
            'contact': 'financialaid@university.in'
        },
        'tuition_fees': '₹1,80,000 per year',
        'hostel_info': {
            'name': 'EE Hostel',
            'location': 'Near Engineering Block',
            'facilities': ['Shared rooms', 'Study areas', 'Recreation rooms'],
            'contact': 'eehostel@university.in'
        },
        'bus_details': {
            'route': 'Campus Shuttle B',
            'timing': 'Every 45 minutes',
            'contact': 'transport@university.in'
        },
        'canteen_info': {
            'location': 'Student Cafeteria',
            'menu': ['Breakfast', 'Lunch', 'Dinner', 'Snacks'],
            'contact': 'canteen@university.in'
        },
        'placements': {
            'companies': ['GE', 'Siemens', 'BHEL', 'L&T'],
            'average_salary': '₹7,00,000 per annum',
            'contact': 'placements@university.in'
        }
    },
    'Mechanical Engineering': {
        'location': 'Engineering Complex, Chennai Campus',
        'programs': ['B.Tech Mechanical', 'M.Tech Mechanical', 'Ph.D. Mechanical Engineering'],
        'contact': 'me@university.in',
        'head': 'Dr. Manoj Kumar',
        'events': [
            {'title': 'Automobile Workshop', 'date': '2024-09-25', 'time': '09:30 AM', 'location': 'Workshop Area'},
            {'title': 'Industry Collaboration Meet', 'date': '2024-10-15', 'time': '11:00 AM', 'location': 'Conference Hall'}
        ],
        'financial_aid': {
            'types': ['Scholarships', 'Internships', 'Student Loans'],
            'contact': 'financialaid@university.in'
        },
        'tuition_fees': '₹1,75,000 per year',
        'hostel_info': {
            'name': 'Mechanical Hostel',
            'location': 'Near Engineering Complex',
            'facilities': ['Single and double rooms', 'Gymnasium', 'Library'],
            'contact': 'mehostel@university.in'
        },
        'bus_details': {
            'route': 'Campus Shuttle C',
            'timing': 'Every hour',
            'contact': 'transport@university.in'
        },
        'canteen_info': {
            'location': 'Student Food Court',
            'menu': ['Breakfast', 'Lunch', 'Dinner', 'Snacks'],
            'contact': 'canteen@university.in'
        },
        'placements': {
            'companies': ['Maruti Suzuki', 'Mahindra & Mahindra', 'Tata Motors', 'Ashok Leyland'],
            'average_salary': '₹6,50,000 per annum',
            'contact': 'placements@university.in'
        }
    },
    'Civil Engineering': {
        'location': 'Civil Engineering Block, Kolkata Campus',
        'programs': ['B.Tech Civil', 'M.Tech Civil', 'Ph.D. Civil Engineering'],
        'contact': 'civil@university.in',
        'head': 'Dr. Priya Singh',
        'events': [
            {'title': 'Urban Planning Seminar', 'date': '2024-09-30', 'time': '10:30 AM', 'location': 'Seminar Room 1'},
            {'title': 'Bridge Construction Workshop', 'date': '2024-10-20', 'time': '02:30 PM', 'location': 'Construction Yard'}
        ],
        'financial_aid': {
            'types': ['Scholarships', 'Grants', 'Work-Study Programs'],
            'contact': 'financialaid@university.in'
        },
        'tuition_fees': '₹1,60,000 per year',
        'hostel_info': {
            'name': 'Civil Hostel',
            'location': 'Near Civil Engineering Block',
            'facilities': ['Single rooms', 'Study areas', 'Recreation rooms'],
            'contact': 'civilhostel@university.in'
        },
        'bus_details': {
            'route': 'Campus Shuttle D',
            'timing': 'Every 45 minutes',
            'contact': 'transport@university.in'
        },
        'canteen_info': {
            'location': 'Student Mess',
            'menu': ['Breakfast', 'Lunch', 'Dinner', 'Snacks'],
            'contact': 'canteen@university.in'
        },
        'placements': {
            'companies': ['Larsen & Toubro', 'DLF', 'Gammon India', 'Punj Lloyd'],
            'average_salary': '₹6,20,000 per annum',
            'contact': 'placements@university.in'
        }
    }
}


@app.route('/')
def home():
    session.clear()  # Clear session on home page load
    return render_template('index.html')

@app.route('/enquire', methods=['POST'])
def enquire():
    user_input = request.json['query']
    response = handle_query(user_input)
    return jsonify(response)

def handle_greeting(query):
    greetings = ["hi", "hello", "hey", "how are you", "good morning", "good afternoon", "good evening"]
    farewells = ["bye", "goodbye", "see you", "take care", "farewell"]
    query_lower = query.lower()

    for greeting in greetings:
        if greeting in query_lower:
            if "how are you" in query_lower:
                return "I'm just a bot, but I'm here to help you! How can I assist you today?"
            return f"{greeting.capitalize()}! How can I assist you today?"

    for farewell in farewells:
        if farewell in query_lower:
            return f"{farewell.capitalize()}! Have a great day!"

    return None

def get_financial_aid():
    financial_aid_response = []
    for department, details in departments.items():
        if 'financial_aid' in details:
            financial_aid_response.append(f"{department} Financial Aid:")
            financial_aid_response.append(
                f"- Types: {', '.join(details['financial_aid']['types'])}"
            )
            financial_aid_response.append(
                f"- Contact: {details['financial_aid']['contact']}"
            )
    return "\n".join(financial_aid_response) if financial_aid_response else "No financial aid information found."

def get_tuition_fees():
    tuition_fees_response = []
    for department, details in departments.items():
        if 'tuition_fees' in details:
            tuition_fees_response.append(f"{department} Tuition Fees:")
            tuition_fees_response.append(
                f"- {details['tuition_fees']}"
            )
    return "\n".join(tuition_fees_response) if tuition_fees_response else "No tuition fees information found."

def get_upcoming_events():
    event_response = []
    for department, details in departments.items():
        if 'events' in details:
            for event in details['events']:
                event_response.append(
                    f"{event['title']} on {event['date']} at {event['time']}, {event['location']} - {department}"
                )
    return "\n".join(event_response) if event_response else "No upcoming events found."

def get_clubs():
    clubs_response = "Clubs available in the university:\n"
    clubs_response += "- Coding Club\n"
    clubs_response += "- Robotics Club\n"
    clubs_response += "- Debate Club\n"
    clubs_response += "- Photography Club\n"
    # Add more clubs as needed
    return clubs_response

def get_hostel_details():
    hostel_response = []
    for department, details in departments.items():
        if 'hostel_info' in details:
            hostel_response.append(f"{department} Hostel Information:")
            hostel_response.append(
                f"- Name: {details['hostel_info']['name']}"
            )
            hostel_response.append(
                f"- Location: {details['hostel_info']['location']}"
            )
            hostel_response.append(
                f"- Facilities: {', '.join(details['hostel_info']['facilities'])}"
            )
            hostel_response.append(
                f"- Contact: {details['hostel_info']['contact']}"
            )
    return "\n".join(hostel_response) if hostel_response else "No hostel information found."

def get_bus_details():
    bus_response = []
    for department, details in departments.items():
        if 'bus_details' in details:
            bus_response.append(f"{department} Bus Details:")
            bus_response.append(
                f"- Route: {details['bus_details']['route']}"
            )
            bus_response.append(
                f"- Timing: {details['bus_details']['timing']}"
            )
            bus_response.append(
                f"- Contact: {details['bus_details']['contact']}"
            )
    return "\n".join(bus_response) if bus_response else "No bus details found."

def get_canteen_info():
    canteen_response = []
    for department, details in departments.items():
        if 'canteen_info' in details:
            canteen_response.append(f"{department} Canteen Information:")
            canteen_response.append(
                f"- Location: {details['canteen_info']['location']}"
            )
            canteen_response.append(
                f"- Menu: {', '.join(details['canteen_info']['menu'])}"
            )
            canteen_response.append(
                f"- Contact: {details['canteen_info']['contact']}"
            )
    return "\n".join(canteen_response) if canteen_response else "No canteen information found."

def get_department_info():
    department_info_response = []
    for department, details in departments.items():
        department_info_response.append(f"{department} Information:")
        department_info_response.append(
            f"- Location: {details['location']}"
        )
        department_info_response.append(
            f"- Head: {details['head']}"
        )
        department_info_response.append(
            f"- Contact: {details['contact']}"
        )
        department_info_response.append(
            f"- Programs Offered: {', '.join(details['programs'])}"
        )
    return "\n".join(department_info_response) if department_info_response else "No department information found."


def get_placements():
    placements_response = []
    for department, details in departments.items():
        if 'placements' in details:
            placements_response.append(f"{department} Placements:")
            placements_response.append(
                f"- Companies: {', '.join(details['placements']['companies'])}"
            )
            placements_response.append(
                f"- Average Salary: {details['placements']['average_salary']}"
            )
            placements_response.append(
                f"- Contact: {details['placements']['contact']}"
            )
    return "\n".join(placements_response) if placements_response else "No placements information found."

def handle_query(query):
    # Initialize session variables if not already set
    if 'history' not in session:
        session['history'] = []

    # Check for greetings and farewells first
    greeting_response = handle_greeting(query)
    if greeting_response:
        session['history'].append({'user': query, 'bot': greeting_response})
        return greeting_response

    # Check for specific inquiries
    response = "I'm not sure. Can you please clarify your question?"

    # Check for financial aid inquiry
    if 'financial aid' in query.lower():
        response = get_financial_aid()

    # Check for tuition fees inquiry
    elif 'tuition fee' in query.lower():
        response = get_tuition_fees()

    # Check for upcoming events inquiry
    elif 'event' in query.lower():
        response = get_upcoming_events()

    # Check for clubs inquiry
    elif 'club' in query.lower():
        response = get_clubs()

    # Check for hostel inquiry
    elif 'hostel' in query.lower():
        response = get_hostel_details()

    # Check for bus details inquiry
    elif 'bus' in query.lower() or 'transport' in query.lower():
        response = get_bus_details()

    # Check for canteen information inquiry
    elif 'canteen' in query.lower() or 'food' in query.lower():
        response = get_canteen_info()

    # Check for placements inquiry
    elif 'placement' in query.lower():
        response = get_placements()

    elif 'department' in query.lower():
        response = get_department_info()

    session['history'].append({'user': query, 'bot': response})
    return response

if __name__ == '__main__':
    app.run(debug=True)
