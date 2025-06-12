# utils/seating.py
def generate_seating_plan(num_guests):
    seating_plan = {
        "tables": [],
        "notes": "Each table accommodates 4 guests. Round layout suggested for visibility."
    }

    guests_remaining = num_guests
    table_number = 1

    while guests_remaining > 0:
        table_size = min(4, guests_remaining)
        seating_plan["tables"].append({
            "table_id": f"T{table_number}",
            "seats": table_size
        })
        guests_remaining -= table_size
        table_number += 1

    return seating_plan
