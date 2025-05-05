from datetime import date, datetime, timedelta

def calculate_exercise_recommendation(caloric_intake, exercise_type):
    burn_rates = {
        'Aerobic': 8,
        'Anaerobic': 6
    }
    if exercise_type not in burn_rates:
        raise ValueError("Invalid exercise type")

    burn_rate = burn_rates[exercise_type]
    duration_minutes = caloric_intake / burn_rate
    calories_burned = int(duration_minutes * burn_rate)

    return {
        'recommended_exercise': f"{exercise_type} exercise",
        'calories_burned': calories_burned,
        'duration_minutes': round(duration_minutes, 2)
    }

def calculate_caloric_deficit(current_weight, target_weight, target_date, maintenance_kcal=2000):
    today = date.today()
    days = (target_date - today).days
    if days <= 0:
        days = 1

    weight_diff = current_weight - target_weight
    total_deficit_kcal = weight_diff * 7700

    if weight_diff <= 0:
        return {
            'daily_caloric_intake': maintenance_kcal,
            'estimated_days': 0
        }

    daily_deficit = total_deficit_kcal / days
    suggested_intake = max(int(maintenance_kcal - daily_deficit), 1200)

    return {
        'daily_caloric_intake': suggested_intake,
        'estimated_days': days
    }

def calculate_if_schedule(fasting_type, eating_start_time):
    fasting_hours = {
        '18:6': 18,  # 18 hours fasting, 6 hours eating
        '16:8': 16,  # 16 hours fasting, 8 hours eating
        'OMAD': 23   # 23 hours fasting, 1 hour eating
    }

    if fasting_type not in fasting_hours:
        raise ValueError("Invalid fasting type")

    eating_start = datetime.combine(date.today(), eating_start_time)
    
    eating_duration = timedelta(hours=24 - fasting_hours[fasting_type])
    
    eating_end = eating_start + eating_duration
    
    fasting_start = eating_end
    
    fasting_end = eating_start

    return {
        'eating_window_start': eating_start.time(),
        'eating_window_end': eating_end.time(),
        'fasting_window_start': fasting_start.time(),
        'fasting_window_end': fasting_end.time()
    }