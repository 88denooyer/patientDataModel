from pip._vendor.distlib.compat import raw_input

"""
return a user's pain score
develop a key based on pain scores
pain max = 4.83
pain mid = 2.4
pain min = 1

from user's result determine where their pain tolerance should be classified
once pain tolerance is classified (high, med, low)
get activity level
finally, classify patient in the data model sets

ex. results->
    pain scale = 1.5 (min, so high pain tolerance)
    activity scale = high activity level (athlete)
    place into group -> athletic high pain tolerance
    
    survey user's first and second day pains...
        create "tolerance" for how far the patient's inputs can deviate from the average of the day
            if the patient is just a little outside (negatively) that "tolerance"
                suggest change in workout
            if the patient is greatly outside (negatively) that "tolerance"
                suggest change
                bump from athletic high pain tolerance to athletic X pain tolerance or Y X pain tolerance
            if the patient is outside (positively) that "tolerance" do nothing (it isn't needed they're doing fine)
            
            
taken the pain graph
    if the patient pain falls in the upper % of the daily data,
        change patient archetype based on % difference
            TIER ONE: 35% from the average, this would be 17.5% from the half cluster
            TIER TWO: 55% from the average, this would be 27.5% from the half cluster
"""


def get_user_type(activity, pain):
    p_type = 1
    return p_type


def decide_fit(user_info, activity, p_tolerance):
    tolerance = get_user_type(activity, p_tolerance)


def get_pain_score(head, finger, bee, tooth, bone):
    h = head * 0.17
    f = finger * 0.13
    b = bee * 0.10
    t = tooth * 0.30
    bo = bone * 0.30
    total = h + f + b + t + bo
    return total


def main():
    print("Hello")


if __name__ == "__main__":
    main()
