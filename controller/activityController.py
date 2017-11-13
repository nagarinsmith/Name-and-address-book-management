class Activity:
    def __init__(self, activityId, personIds, date, time, description):
        self.__activityId = activityId
        self.__personIds = personIds
        self.__date = date
        self.__time = time
        self.__description = description