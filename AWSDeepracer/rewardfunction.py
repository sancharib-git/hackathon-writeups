def reward_function(params):
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    all_wheels_on_track = params['all_wheels_on_track']
    offtrack = params['is_offtrack']
    speed = params['speed']
    steering = abs(params['steering_angle']) # We don't care whether it is left or right steering
    SPEED_THRESHOLD = 1.0 
    STEERING_THRESHOLD = 20.0

    
    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width
    
    # If off-track, penalize right away
    if offtrack:
        reward = 1e-5
    
    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward = 1
    elif distance_from_center <= marker_2:
        reward = 0.5
    elif distance_from_center <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3  # likely crashed/ close to off track

    if not all_wheels_on_track:
		# Penalize if the car goes off track
        reward = 1e-3
    elif speed < SPEED_THRESHOLD:
		# Penalize if the car goes too slow
        reward = reward + 0.5
    else:
		# High reward if the car stays on track and goes fast
        reward = reward + 1.0
        
    #If too much zig-zag reduce reward
    if steering > STEERING_THRESHOLD:
        reward *= 0.5

    return float(reward)
