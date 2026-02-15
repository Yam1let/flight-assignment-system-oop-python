# ✈️ Flight Assignment System (OOP – Python)

## Overview

This project is a simple object-oriented flight management system built in Python.
It models the relationship between pilots and flights while enforcing operational constraints such as weekly flight hour limits.

The system demonstrates core OOP principles including encapsulation, object relationships, and business rule validation.

---

## Features

* Pilot registration with license tracking
* Flight creation with origin, destination, and duration
* Pilot-to-flight assignment system
* Weekly flight hour limit validation
* Error handling using Python exceptions

---

## Project Structure

The system is built using three main classes:

* `Pilot` → Represents a pilot and tracks assigned flights and total weekly hours
* `Flight` → Represents a flight with duration and assigned pilot
* `FlightAssignmentSystem` → Handles pilot assignment logic and validations

---

## Example Usage

```python
pilot1 = Pilot("Amelia Earhart", "PL-123")
flight1 = Flight("AER-451", "City A", "City B", 3.0)

system = FlightAssignmentSystem()
system.assign_pilot_to_flight(pilot1, flight1)

print(flight1.assigned_pilot.name)
print(pilot1.weekly_flight_hours)
```

---

## Concepts Applied

* Object-Oriented Programming (OOP)
* Class relationships
* State management
* Business rule enforcement
* Basic software design structure
---
