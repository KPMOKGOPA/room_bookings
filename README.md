#  Room Booking REST API (Django)

A RESTful API for managing conference room bookings, developed by **Kabelo Phuti Mokgopa**.  
This API handles booking management for four conference/board rooms while **preventing overlapping reservations**.

---

##  Key Features

- **Room Management:** Supports 4 conference/board rooms
- **Booking Operations:**
  - Create new bookings
  - View all bookings
  - Update existing bookings
  - Delete bookings
- **Smart Conflict Detection:** Prevents overlapping bookings for the same room
- **Validation:** Ensures logical booking times (e.g., end time after start time)
- **RESTful Design:** Clean API endpoints for easy integration
- **SQLite Database:** Lightweight and portable solution perfect for this application's scale
- **Browsable Interface:** Fully browsable API via web browser – rooms and bookings can be created, edited, and deleted through the web UI

---

##  API Endpoints

| Endpoint                                       | Method        | Description                             |
|-----------------------------------------------|---------------|-----------------------------------------|
| `http://127.0.0.1:8000/api/`                   | GET           | API root endpoint                       |
| `http://127.0.0.1:8000/api/room_booking/`      | GET           | List all bookings                       |
| `http://127.0.0.1:8000/api/room_booking/`      | POST          | Create new booking                      |
| `http://127.0.0.1:8000/api/room_booking/1/`    | GET           | Retrieve specific booking (ID: 1)       |
| `http://127.0.0.1:8000/api/room_booking/1/`    | PUT/PATCH     | Update specific booking (ID: 1)         |
| `http://127.0.0.1:8000/api/room_booking/1/`    | DELETE        | Delete specific booking (ID: 1)         |
| `http://127.0.0.1:8000/api/rooms/`             | GET/POST      | View or create rooms                    |
| `http://127.0.0.1:8000/api/rooms/<id>/`        | PUT/PATCH/DELETE | Update or delete a specific room   |

---

## Room Data Example

You can view and manage the available rooms at:

📍 `http://127.0.0.1:8000/api/rooms/`

Example JSON response:

```json
[
    {
        "id": 1,
        "name": "Room 1",
        "capacity": 6
    },
    {
        "id": 2,
        "name": "Room 2",
        "capacity": 8
    },
    {
        "id": 3,
        "name": "Room 3",
        "capacity": 12
    },
    {
        "id": 4,
        "name": "Room 4",
        "capacity": 25
    }
]
```

Rooms can be created, edited, and deleted through the browser interface 

---
##  Database

**SQLite** is used because:

- Perfect for small to medium applications
- Requires no additional server setup
- Excellent portability (single file database)
- Easily meets the data requirements of this system
- Zero configuration needed for development

---

## Getting Started

### Prerequisites

- Python 3.8+
- Django 3.2+
- Django REST Framework
- Virtualenv (recommended)

### Installation

```bash
# Clone the repository
git clone https://github.com/KPMOKGOPA/room-booking-django.git
cd room-booking-django

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows

# Install dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate

# (Optional) Create a superuser for admin access
python manage.py createsuperuser

# Run the development server
python manage.py runserver
```

##  Example Requests on terminal

### Create a Booking

```bash
curl -X POST http://127.0.0.1:8000/api/room_booking/ \
-H "Content-Type: application/json" \
-d '{
    "room": 4,
    "boooked_by ": "Kabelo PP",
    "start_time": "2023-07-15T09:00:00Z",
    "duration_minutes": 30

}'
```
### Editing a Booking 
```bash
curl -X PATCH http://127.0.0.1:8000/api/room_booking/1/ \
-H "Content-Type: application/json" \
-d '{
    "end_time": "2023-07-15T11:00:00Z"
}'
```


### Delete a Booking
```bash
curl -X DELETE http://127.0.0.1:8000/api/room_booking/1/
```


______________end_________________________________
