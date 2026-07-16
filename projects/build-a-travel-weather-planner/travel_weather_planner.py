# Variables
distance_mi = 4
is_raining = False
has_bike = True
has_car = False
has_ride_share_app = False

# Conditional logic
if not distance_mi:
    print(False)

elif distance_mi <= 1:
    print(not is_raining)

elif distance_mi > 1 and distance_mi <= 6:
    print(has_bike and not is_raining)

elif distance_mi > 6:
    print(has_car or has_ride_share_app)

else:
    print(False)

