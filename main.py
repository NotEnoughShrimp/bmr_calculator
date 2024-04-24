def basal_metabolic_rate(age, gender, weight, height):
    if gender == 'male':
        bmr = ((10 * weight) + (6.25 * height) - (5 * age) + 5)
    else:
        bmr = ((10 * weight) + (6.25 * height) - (5 * age) - 161)
    return round(bmr, 2)

def imperial_to_metric(height, weight):
    height_in_cm = height * 2.54
    weight_in_kg = weight * 0.453592
    return height_in_cm, weight_in_kg

def calculate_TDEE(bmr, multiplier):
    total_daily_energy_expenditure = bmr * multiplier
    return round(total_daily_energy_expenditure, 2)

while True:
    try:
        age = int(input('Enter age: '))

        while True:
            gender = input('Enter gender: ').lower()
            if gender not in ['male', 'female']:
                print('Please enter "male" or "female".')
            else:
                break
        while True:
            measurement = input('metric (kg/cm) or imperial (lb/inch)? ').lower()
            if measurement not in ['metric', 'imperial']:
                print('Please enter "metric" or "imperial".')
            else:
                if measurement == 'imperial':
                    imperial_height = int(input('enter height in inches (1 foot = 12 inches): '))
                    imperial_weight = int(input('enter weight in pounds: '))
                    height, weight = imperial_to_metric(imperial_height, imperial_weight)
                else:
                    height = int(input('enter height in cm: '))
                    weight = int(input('enter weight in kg: '))
                break
        while True:
            activity_level = input('sedentary (Little to no exercise)\nlight (exercise 1-3 days/week)\nmoderate (3-5 exercise/activity/week)\nactive (hard exercise/ 6-7 days/week)\nvery (more than that): ').lower()
            if activity_level not in ['sedentary', 'lightly', 'moderate', 'active', 'very']:
                print('Invalid input. Please enter: sedentary, lightly, moderate, active, or very.')
            else:
                if activity_level == 'sedentary':
                    multiplier = 1.2
                elif activity_level == 'light':
                    multiplier = 1.375
                elif activity_level == 'moderate':
                    multiplier = 1.55
                elif activity_level == 'active':
                    multiplier = 1.725
                elif activity_level == 'very':
                    multiplier = 1.9
                break
        break
    except ValueError as e:
        print('Invalid entry: ', e)

bmr = basal_metabolic_rate(age, gender, weight, height)
print('This is your base BMR using the Mifflin-St Jeor Equation.')
print(bmr)
total_daily_energy_expenditure = calculate_TDEE(bmr, multiplier)
print(f'TDEE for: {activity_level} lifestyle')
print(total_daily_energy_expenditure)
