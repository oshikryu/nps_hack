from camp_checker import notify_when_available
# ---------------------------------------- #
# modify arguments here

_args = {
    "camp_key": "upper_pines", # maps to CAMP_MAP value
    "year": '2020',
    "month": '09',
    "day": '01' # TODO: month query only accepts the first of the month
};
# ---------------------------------------- #

notify_when_available(**_args)
