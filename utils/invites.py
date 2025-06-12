# utils/invites.py

def generate_invitation(data):
    """
    Generates a simple invitation message based on input dictionary data.

    Expected keys in `data`:
        - guest_name
        - event_name
        - date
        - time
        - location
    """
    try:
        guest_name = data.get('guest_name', 'Guest')
        event_name = data.get('event_name', 'Our Special Event')
        date = data.get('date', 'a future date')
        time = data.get('time', 'some time')
        location = data.get('location', 'a wonderful venue')

        message = (
            f"Dear {guest_name},\n\n"
            f"You are cordially invited to the **{event_name}**!\n"
            f"📅 Date: {date}\n"
            f"⏰ Time: {time}\n"
            f"📍 Location: {location}\n\n"
            "We look forward to celebrating with you!\n\n"
            "Best Regards,\n"
            "The Event Team"
        )
        return message

    except Exception as e:
        return f"Error generating invitation: {str(e)}"
