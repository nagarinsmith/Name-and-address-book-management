class Activity:
    def __init__(self, activityId, personIds, date, time, description):
        self.__activityId = activityId
        self.__personIds = personIds
        self.__date = date
        self.__time = time
        self.__description = description

    def setActivityId(self, activityId):
        self.__activityId = activityId

    def getActivityId(self):
        return self.__activityId

    def setPersonIds(self, personIds):
        self.__personIds = personIds

    def getPersonIds(self):
        return self.__personIds

    def setDate(self, date):
        self.__date = date

    def getDate(self):
        return self.__date

    def setTime(self, time):
        self.__time = time

    def getTime(self):
        return self.__time

    def setDescription(self, description):
        self.__description = description

    def getDescription(self):
        return self.__description