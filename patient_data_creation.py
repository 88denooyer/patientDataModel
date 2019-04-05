"""
pAI developing Patient Model Groups

Beginning:
    Grouping Pain Tolerance
        Everyday Occurrence Pain:
            1. Headache (not migraine)
                a. Stops activity for the day (debilitating)                (4
                b. Need a break from activity to take Advil and recover     (3
                c. No need to stop work, takes Advil                        (2
                d. No need for Advil, migraine will pass                    (1
            2. Closed a door or drawer on finger
                a. Definitely broken. End of the world. Head to the hospital        (4
                b. Immobilizes finger for the day                                   (3
                c. Take an Advil for the pain since it'll probably hurt later       (2
                d. No Advil. That didn't even hurt. You should see the other guy    (1
            3. Bee String (NOT ALLERGIC - IF YOU'RE ALLERGIC AND HAVE BEEN STUNG BY A BEE CONSULT A DOCTOR IMMEDIATELY)
                a. Can't use this body part for the day, even after an anti-inflammatory (Benadryl + Advil) (5
                b. Benadryl and Advil plus some rest and the day will go on                                 (4
                c. Benadryl for the reaction and some ice                                                   (3
                d. Ice and continue with the day                                                            (2
                e. What bee sting?                                                                          (1
        Emergency / Rare Occurrence Pain (up to one week after surgery or injury):
            1. Wisdom teeth removal
                a. Regular prescription painkiller use and pain still causes sleep loss         (5
                b. Painkiller use helped with eating and sleeping... still very painful         (4
                c. Painkiller use just to sleep, Advil during the day                           (3
                d. No painkiller use a 1 day after surgery, Advil use throughout the day        (2
                e. No painkiller use at all, Advil just to eat and sleep                        (1
            2. Broken bone - ignore immediate injury, consider after hospital visit (arm, leg, hand, etc.)
                a. Regular prescription painkiller use and pain still causes sleep loss         (5
                b. Painkillers use just to sleep, Advil during the day                          (4
                c. No painkiller use 1-3 days after injury                                      (3
                d. Advil just to help with sleep and daily activity                             (2
                e. No painkiller use at all, maybe use Advil to help sleep                      (1

    Pain Percentages:
        Headache - 15%
        Finger in door or drawer - 10%
        Bee sting    - 5%
        Wisdom teeth - 30%
        Broken bone  - 30%

    Grouping Flexibility
        Flexibility of uninjured appendage (assuming leg for now):
            1. Toe touch
                a. Hands reach knee                 (1
                b. Hands reach middle of shin       (2
                c. Hands reach ankle                (3
                d. Hands reach toes                 (4
                e. Palm on floor                    (5
            2. Knee bend
                a. Bending knee so foot is barely off ground                                (1
                b. Bending knee so angle of bend is ~45 degrees (form a right angle)        (2
                c. Bending knee so you can reach back and grab foot                         (3
                d. Heel can touch to butt                                                   (4
        Flexibility of injured appendage (assuming leg for now):
            1. Toe touch
                a. Hands reach knee                 (1
                b. Hands reach middle of shin       (2
                c. Hands reach ankle                (3
                d. Hands reach toes                 (4
                e. Palm on floor                    (5
            2. Knee bend
                a. Bending knee so foot is barely off ground                                (1
                b. Bending knee so angle of bend is ~45 degrees (form a right angle)        (2
                c. Bending knee so you can reach back and grab foot                         (3
                d. Heel can touch to butt                                                   (4

=======================================================================================================================

Middle:
    Grouping Activity
        Physical activity (highest amount of activity before the injury is assumed to have affected activity):
            1. Gym - heavy weight lifting
                a. 6-7 days / week
                b. 4-5 days / week
                c. 2-3 days / week
                d. once a week
                e. never
            2. Gym - cardio or aerobic exercise
                a. 6-7 days / week
                b. 4-5 days / week
                c. 2-3 days / week
                d. once a week
                e. never
            3. Gym - yoga or flexibility conditioning
                a. 6-7 days / week
                b. 4-5 days / week
                c. 2-3 days / week
                d. once a week
                e. never

End:
    Classifying and Grouping Patient Answered Data
        Scores of the questions above
        How should the scores affect the patient's classification

    Pain and Flexibility
        Create weight and score for each category and question, respectively
            Calculate

"""
import io
import csv
import json
import random
import sys
from exitstatus import ExitStatus

"""
pain max - 4.83
pain mid - 2.4
pain min - 1
"""

pain_tolerance_key = ['high pain tolerance', 'medium pain tolerance', 'low pain tolerance']
flexibility_key = ['very flexible', 'somewhat flexible', 'barely flexible', 'brittle']
age_group_key = ['18-24', '25-33', '34-42', '43-51', '52-60', '60+']

# ===================================================================================================================

fname_activity = ['athletic', 'active', 'moderate', 'inactive']
fname_date = ['1-1-2019', '1-2-2019', '1-3-2019', '1-4-2019', '1-5-2019', '1-6-2019', '1-7-2019']
fname_pain = ['high', 'medium', 'low']
fname_time = ['0900', '1200', '1700']

file_fields = ['date', 'time', 'p_id', 'p_pain', 'p_flex', 'p_type']

"""
def define_patient(type):
    status = 0
    return status
"""


# helper to return the number corresponding to the date in the json file
def send_date(date):
    if date == '1-1-2019':
        return '1'
    if date == '1-2-2019':
        return '2'
    if date == '1-3-2019':
        return '3'
    if date == '1-4-2019':
        return '4'
    if date == '1-5-2019':
        return '5'
    if date == '1-6-2019':
        return '6'
    if date == '1-7-2019':
        return '7'
    else:
        print("You don't want to know what happens past that date...")
        sys.exit(0)


def get_first_pain(activity_index, pain_index, day):
    # write if case for each input type
    # something like if activity == 'athletic' && pain_index == 'high && day =='1-1-2019'
    # return data['athletic-hk]['pain'][0]['1'][0]
    with open('./final_data_key.json') as data_file:
        data = json.load(data_file)
        for date in fname_date:
            for activity in fname_activity:
                for pain in fname_pain:
                    if date == day and activity == activity_index and pain == pain_index:
                        # print(data['high'][send_date(fname_date[2])]['athletic'][1])
                        return data[pain][send_date(date)][activity][0]


def get_second_pain(activity_index, pain_index, day):
    # this will be the same as the above function but will return the SECOND number of the pain index
    with open('./final_data_key.json') as data_file:
        data = json.load(data_file)
        for date in fname_date:
            for activity in fname_activity:
                for pain in fname_pain:
                    if date == day and activity == activity_index and pain == pain_index:
                        return data[pain][send_date(date)][activity][1]


def get_first_flex(activity_index, pain_index, day):
    with open('./final_data_key.json') as data_file:
        data = json.load(data_file)
        for date in fname_date:
            for activity in fname_activity:
                for pain in fname_pain:
                    if date == day and activity == activity_index and pain == pain_index:
                        return data[pain][send_date(date)][activity][2]


def get_second_flex(activity_index, pain_index, day):
    with open('./final_data_key.json') as data_file:
        data = json.load(data_file)
        for date in fname_date:
            for activity in fname_activity:
                for pain in fname_pain:
                    if date == day and activity == activity_index and pain == pain_index:
                        return data[pain][send_date(date)][activity][3]


def generate_data():
    count = 0
    for activity in fname_activity:
        for date in fname_date:
            for pain in fname_pain:
                for time in fname_time:
                    with open(activity + '_' + pain + '_' + date + '_' + time + '.csv', 'a', newline='') as file_path:
                        writer = csv.DictWriter(file_path, fieldnames=file_fields)
                        writer.writerow({'date': 'date', 'time': 'time', 'p_id': 'patient_id', 'p_pain': 'pain',
                                         'p_flex': 'flex', 'p_type': 'activity'})
                        for i in range(600):
                            p_ident = i + 817435
                            this_date = date
                            this_time = time

                            this_activity = activity
                            writer.writerow({'date': this_date,
                                             'time': this_time,
                                             'p_id': p_ident,
                                             'p_pain': random.randint((get_first_pain(activity, pain, date) * 100),
                                                                      (get_second_pain(activity, pain, date) - 1) * 100) / 100.00,
                                             'p_flex': random.randint((get_first_flex(activity, pain, date) * 100),
                                                                      (get_second_flex(activity, pain, date) - 1) * 100) / 100.00,
                                             'p_type': this_activity
                                             })
                    # print(activity, pain, date, time)
                    count = count + 1
    print(count)

"""
def get_flex_score(tt_ui, kb_ui, tt_i, kb_i):
    total = tt_ui + kb_ui + tt_i + kb_i
    return total
"""


def main():
    generate_data()


if __name__ == "__main__":
    main()
