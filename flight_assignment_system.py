"""
Flight Assignment System - OOP in Python
Author: Yam1let
"""

class Pilot:
    """
    Represents a pilot with a flight schedule and weekly flight hours tracking.
    """

    def __init__(self, name: str, license_number: str):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not isinstance(license_number, str):
            raise TypeError("license_number must be a string")

        self.name = name
        self.license_number = license_number
        self.flight_schedule = []
        self.weekly_flight_hours = 0.0


class Flight:
    """
    Represents a flight with origin, destination, and duration.
    """

    def __init__(self, flight_number: str, origin: str, destination: str, duration_hours: float):
        if not isinstance(flight_number, str):
            raise TypeError("flight_number must be a string")
        if not isinstance(origin, str):
            raise TypeError("origin must be a string")
        if not isinstance(destination, str):
            raise TypeError("destination must be a string")
        if not isinstance(duration_hours, float):
            raise TypeError("duration_hours must be a float")

        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.duration_hours = duration_hours
        self.assigned_pilot = None


class FlightAssignmentSystem:
    """
    Handles pilot assignment to flights with weekly hour restrictions.
    """

    def assign_pilot_to_flight(self, pilot: Pilot, flight: Flight, weekly_limit: float = 40.0):

        if not isinstance(pilot, Pilot):
            raise TypeError("pilot must be a Pilot instance")

        if not isinstance(flight, Flight):
            raise TypeError("flight must be a Flight instance")

        if flight.assigned_pilot is not None:
            raise ValueError("flight already has an assigned pilot")

        if pilot.weekly_flight_hours + flight.duration_hours > weekly_limit:
            raise ValueError("pilot exceeds weekly flight hour limit")

        flight.assigned_pilot = pilot
        pilot.flight_schedule.append(flight)
        pilot.weekly_flight_hours += flight.duration_hours


# Example usage
if __name__ == "__main__":

    pilot1 = Pilot("Amelia Earhart", "PL-123")
    flight1 = Flight("AER-451", "City A", "City B", 3.0)

    system = FlightAssignmentSystem()
    system.assign_pilot_to_flight(pilot1, flight1)

    print(flight1.assigned_pilot.name)
    print(pilot1.weekly_flight_hours)
    print(len(pilot1.flight_schedule))

