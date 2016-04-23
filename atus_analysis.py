import pandas as pd
import matplotlib.pyplot as plt


def read_in_data():
    activity = pd.read_csv('data/atusact_2014.dat')
    respondent = pd.read_csv('data/atusresp_2014.dat')
    roster = pd.read_csv('data/atusrost_2014.dat')
    who = pd.read_csv('data/atuswho_2014.dat')
    cps = pd.read_csv('data/atuscps_2014.dat')
    elder_care = pd.read_csv('data/atusrostec_2014.dat')
    activity_sum = pd.read_csv('data/atussum_2014.dat')
    return activity, respondent, roster, who, cps, elder_care, activity_sum


# def get_six_digit_codes(df):
#     six_digit_list = []
#     for row in df.itertuples():
#         if row.TUTIER1 < 10:
#             first_code = '0{}'.format(row.TUTIER1)
#         else:
#             first_code = TUTIER2
#         if row.TUTIER2 < 10:
#             second_code = '0{}'.format(row.TUTIER2)
#         else:
#             second_code = TUTIER2
#         if row.TUTIER3 < 10:
#             third_code = '0{}'.format(row.TUTIER3)
#         else:
#             third_code = TUTIER3
#         six_digit_list.append('{}{}{}'.format(first_code, second_code,
#                                               third_code))
#     return six_digit_list

def get_minutes_child_care(grouped):
    minutes_caring = {}
    for name, group in grouped:
        for row in group.itertuples():
            if row.codes[:2] in ['31', '32', '33']:
                if name in minutes_caring:
                    minutes_caring[name] = minutes_caring[name] + row.TUACTDUR24
                else:
                    minutes_caring[name] = row.TUACTDUR24
    child_care_time = pd.Series(minutes_caring)
    return child_care_time
